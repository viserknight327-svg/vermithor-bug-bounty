import subprocess
import json
import os

def run_httpx(subdomains):
    """
    Executes httpx on a list of subdomains to identify live hosts and gather metadata.
    """
    if not subdomains:
        return []

    print(f"[*] Running httpx on {len(subdomains)} subdomains...")
    
    # Create a temporary file for subdomains
    temp_file = "temp_subs.txt"
    with open(temp_file, "w") as f:
        f.write("\n".join(subdomains))

    try:
        # Run httpx with JSON output
        result = subprocess.run(
            ["httpx", "-l", temp_file, "-silent", "-json", "-status-code", "-title", "-tech-detect"],
            capture_output=True,
            text=True,
            check=True
        )
        
        live_hosts = []
        for line in result.stdout.strip().split('\n'):
            if line:
                try:
                    live_hosts.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        
        print(f"[+] httpx identified {len(live_hosts)} live hosts.")
        return live_hosts
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running httpx: {e}")
        return []
    except FileNotFoundError:
        print("[!] httpx not found. Please install it using scripts/install_tools.sh.")
        return []
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
