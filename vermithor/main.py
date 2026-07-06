import argparse
import sys
from vermithor.config import Config
from vermithor.ai_modules.recon_analyzer import ReconAnalyzer
from vermithor.ai_modules.vuln_prioritizer import VulnPrioritizer
from vermithor.ai_modules.report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Vermithor: AI-Powered Bug Bounty Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Recon command
    recon_parser = subparsers.add_parser("recon", help="Perform intelligent reconnaissance")
    recon_parser.add_argument("target", help="Target domain or IP")

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Run vulnerability scans")
    scan_parser.add_argument("target", help="Target domain or IP")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze scan results using AI")
    analyze_parser.add_argument("file", help="Path to scan results file")

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate a bug report")
    report_parser.add_argument("file", help="Path to finding data file")

    # Autopilot command
    autopilot_parser = subparsers.add_parser("autopilot", help="Run full automated hunting loop")
    autopilot_parser.add_argument("target", help="Target domain")

    # Config command
    config_parser = subparsers.add_parser("config", help="Manage Vermithor configuration")
    config_parser.add_argument("--set-key", nargs=2, metavar=("PROVIDER", "KEY"), help="Set an API key")

    args = parser.parse_args()

    if args.command == "recon":
        from vermithor.tools.subfinder_wrapper import run_subfinder
        from vermithor.tools.httpx_wrapper import run_httpx
        
        subdomains = run_subfinder(args.target)
        live_hosts = run_httpx(subdomains)
        
        analyzer = ReconAnalyzer()
        analysis = analyzer.analyze(live_hosts)
        print("\n=== AI Recon Analysis ===\n")
        print(analysis)

    elif args.command == "scan":
        from vermithor.tools.nuclei_wrapper import run_nuclei
        # In a real scenario, we'd use a file of targets
        # For this demo, we assume the target is a file or a single URL
        results = run_nuclei(args.target)
        print(f"[+] Scan results saved to nuclei_results.json (simulated)")

    elif args.command == "analyze":
        import json
        with open(args.file, 'r') as f:
            data = json.load(f)
        prioritizer = VulnPrioritizer()
        analysis = prioritizer.prioritize(data)
        print("\n=== AI Vulnerability Prioritization ===\n")
        print(analysis)

    elif args.command == "report":
        import json
        with open(args.file, 'r') as f:
            data = json.load(f)
        generator = ReportGenerator()
        report = generator.generate_report(data)
        print("\n=== Generated Bug Report ===\n")
        print(report)

    elif args.command == "autopilot":
        from vermithor.tools.subfinder_wrapper import run_subfinder
        from vermithor.tools.httpx_wrapper import run_httpx
        from vermithor.tools.nuclei_wrapper import run_nuclei
        import json

        print(f"[*] Autopilot engaged for: {args.target}")
        
        # 1. Recon
        subdomains = run_subfinder(args.target)
        live_hosts = run_httpx(subdomains)
        
        # 2. AI Recon Analysis
        analyzer = ReconAnalyzer()
        recon_analysis = json.loads(analyzer.analyze(live_hosts))
        
        # 3. Targeted Scan (using top prioritized target)
        if recon_analysis.get("prioritized_targets"):
            top_target = recon_analysis["prioritized_targets"][0]["target"]
            print(f"[*] AI prioritized {top_target}. Starting scan...")
            
            # Create temp file for nuclei
            with open("autopilot_targets.txt", "w") as f:
                f.write(top_target)
            
            scan_results = run_nuclei("autopilot_targets.txt")
            
            # 4. AI Vuln Analysis
            if scan_results:
                prioritizer = VulnPrioritizer()
                vuln_analysis = prioritizer.prioritize(scan_results)
                print("\n=== AI Autopilot Findings ===\n")
                print(vuln_analysis)
            else:
                print("[*] No vulnerabilities found by automated scanners.")
        else:
            print("[!] AI could not identify high-priority targets for scanning.")
    elif args.command == "config":
        if args.set_key:
            provider, key = args.set_key
            Config.set_api_key(provider, key)
            print(f"[+] API key for {provider} set successfully.")
        else:
            config_parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
