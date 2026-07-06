import subprocess
import json
import os

def run_subfinder(target):
    """
    Executes Subfinder on the target and returns a list of subdomains.
    """
    print(f"[*] Running Subfinder on {target}...")
    try:
        # Run subfinder and get output in JSON format
        result = subprocess.run(
            ["subfinder", "-d", target, "-silent", "-json"],
            capture_output=True,
            text=True,
            check=True
        )
        
        subdomains = []
        for line in result.stdout.strip().split('\n'):
            if line:
                try:
                    data = json.loads(line)
                    subdomains.append(data.get("host"))
                except json.JSONDecodeError:
                    continue
        
        print(f"[+] Subfinder found {len(subdomains)} subdomains.")
        return subdomains
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running Subfinder: {e}")
        return []
    except FileNotFoundError:
        print("[!] Subfinder not found. Please install it using scripts/install_tools.sh.")
        return []
