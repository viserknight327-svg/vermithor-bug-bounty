import subprocess
import json
import os

def run_nuclei(target_file, templates=None):
    """
    Executes Nuclei on targets listed in a file.
    """
    if not os.path.exists(target_file):
        print(f"[!] Target file {target_file} not found.")
        return []

    print(f"[*] Running Nuclei on targets in {target_file}...")
    
    cmd = ["nuclei", "-l", target_file, "-silent", "-json-export", "nuclei_results.json"]
    
    if templates:
        cmd.extend(["-t", templates])

    try:
        # Run nuclei
        subprocess.run(cmd, check=True)
        
        results = []
        if os.path.exists("nuclei_results.json"):
            with open("nuclei_results.json", "r") as f:
                for line in f:
                    if line.strip():
                        results.append(json.loads(line))
            os.remove("nuclei_results.json")
        
        print(f"[+] Nuclei scan complete. Found {len(results)} potential issues.")
        return results
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running Nuclei: {e}")
        return []
    except FileNotFoundError:
        print("[!] Nuclei not found. Please install it using scripts/install_tools.sh.")
        return []
