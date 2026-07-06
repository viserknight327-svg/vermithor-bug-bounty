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

    # Config command
    config_parser = subparsers.add_parser("config", help="Manage Vermithor configuration")
    config_parser.add_argument("--set-key", nargs=2, metavar=("PROVIDER", "KEY"), help="Set an API key")

    args = parser.parse_args()

    if args.command == "recon":
        print(f"[*] Starting intelligent reconnaissance on: {args.target}")
        # Placeholder for recon logic
        pass
    elif args.command == "scan":
        print(f"[*] Running vulnerability scans on: {args.target}")
        # Placeholder for scan logic
        pass
    elif args.command == "analyze":
        print(f"[*] Analyzing scan results from: {args.file}")
        # Placeholder for analysis logic
        pass
    elif args.command == "report":
        print(f"[*] Generating bug report from: {args.file}")
        # Placeholder for report generation logic
        pass
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
