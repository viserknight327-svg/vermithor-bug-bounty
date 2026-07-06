# Vermithor Usage Guide

This guide provides detailed instructions on how to use Vermithor for your bug bounty hunting activities.

## 1. Installation and Setup

Refer to the main [README.md](../README.md) for detailed instructions on how to install Vermithor and its dependencies, including external bug bounty tools and Python packages. Ensure you have configured your LLM API keys using the `vermithor config --set-key` command.

## 2. Command-Line Interface (CLI)

Vermithor is primarily operated via its command-line interface. You can always get help by running:

```bash
python vermithor/main.py --help
```

This will display the main commands and their descriptions.

### 2.1. `recon` Command

The `recon` command initiates an intelligent reconnaissance process on a specified target. It orchestrates external tools like Subfinder and httpx, then uses AI to analyze the gathered data.

**Usage:**

```bash
python vermithor/main.py recon <target_domain_or_ip>
```

**Example:**

```bash
python vermithor/main.py recon example.com
```

**Output:**

The `recon` command will output a structured summary of the attack surface, including prioritized targets for further investigation and suggested next steps. This output will be in a human-readable format and can also be saved to a file for later analysis.

### 2.2. `scan` Command

The `scan` command is used to run vulnerability scans on a target. In future iterations, this command will be enhanced to take AI-driven suggestions from the `recon` phase to perform more targeted scans.

**Usage:**

```bash
python vermithor/main.py scan <target_domain_or_ip>
```

**Example:**

```bash
python vermithor/main.py scan sub.example.com
```

**Output:**

This command will execute configured vulnerability scanners (e.g., Nuclei) and output their raw results. These results can then be fed into the `analyze` command.

### 2.3. `analyze` Command

The `analyze` command leverages Vermithor's AI capabilities to process raw scan results, prioritize findings, and identify potential false positives or vulnerability chains.

**Usage:**

```bash
python vermithor/main.py analyze <path_to_scan_results_file>
```

**Example:**

```bash
python vermithor/main.py analyze /path/to/nuclei_results.json
```

**Input File Format:**

The input file should ideally be a JSON file containing the raw output from vulnerability scanners. Vermithor's AI will parse and interpret this data.

**Output:**

The `analyze` command will provide a prioritized list of potential vulnerabilities, along with their estimated impact, confidence scores, and suggestions for manual verification or further testing. It may also highlight potential attack chains.

### 2.4. `report` Command

The `report` command assists in generating professional bug bounty reports based on confirmed findings. It uses AI to draft clear, concise, and platform-specific reports.

**Usage:**

```bash
python vermithor/main.py report <path_to_finding_data_file> [--platform <platform_name>]
```

**Example:**

```bash
python vermithor/main.py report /path/to/my_finding.json --platform hackerone
```

**Input File Format:**

The input file should be a JSON file detailing the vulnerability, its impact, steps to reproduce, proof-of-concept, and any other relevant information. A sample structure will be provided in the `templates/` directory.

**Output:**

The command will output a draft bug report, which you can then review, refine, and submit to the bug bounty platform.

### 2.5. `config` Command

The `config` command allows you to manage Vermithor's configuration, primarily for setting API keys for LLM providers.

**Usage:**

```bash
python vermithor/main.py config --set-key <PROVIDER> <API_KEY>
```

**Example:**

```bash
python vermithor/main.py config --set-key OPENAI_API_KEY sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
python vermithor/main.py config --set-key GEMINI_API_KEY your_gemini_api_key_here
```

*Note: Replace `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your actual API key.*

## 3. Workflow Example

Here's a typical workflow using Vermithor:

1.  **Initial Recon:**
    ```bash
    python vermithor/main.py recon target.com > recon_summary.txt
    ```
2.  **Review Recon Summary:** Read `recon_summary.txt` to identify interesting subdomains or IP addresses.
3.  **Targeted Scan:**
    ```bash
    python vermithor/main.py scan sub.target.com > scan_results.json
    ```
4.  **AI Analysis of Scan Results:**
    ```bash
    python vermithor/main.py analyze scan_results.json > prioritized_vulns.json
    ```
5.  **Manual Verification:** Based on `prioritized_vulns.json`, manually verify the most critical findings.
6.  **Generate Report:** Once a bug is confirmed, create a `finding_details.json` and generate a report:
    ```bash
    python vermithor/main.py report finding_details.json --platform bugcrowd > bug_report.md
    ```

This workflow demonstrates how Vermithor integrates AI to guide and accelerate your bug bounty efforts.
