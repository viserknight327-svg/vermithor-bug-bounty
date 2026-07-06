# Vermithor: AI-Powered Bug Bounty Tool

![Vermithor Logo](docs/vermithor_logo.png) <!-- Placeholder for a logo -->

Vermithor is an advanced, AI-powered command-line interface (CLI) tool designed to streamline and enhance the bug bounty hunting process. By integrating with established bug bounty tools and leveraging Large Language Models (LLMs), Vermithor assists security researchers in intelligent reconnaissance, vulnerability prioritization, and professional report generation.

## Features

*   **Intelligent Reconnaissance:** AI-driven analysis of recon data to identify high-value assets and suggest next steps.
*   **Vulnerability Prioritization:** AI-powered assessment of scan results to reduce false positives, estimate impact, and suggest manual verification.
*   **Automated Report Generation:** Drafts professional bug bounty reports for various platforms (HackerOne, Bugcrowd, etc.).
*   **Tool Orchestration:** Seamlessly integrates and orchestrates popular bug bounty tools like Subfinder, Nuclei, httpx, ffuf, and sqlmap.
*   **Modular and Extensible:** Designed with a modular architecture, allowing easy integration of new tools and AI capabilities.

## Getting Started

### Prerequisites

*   Python 3.8+
*   Go (for installing some bug bounty tools)
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/vermithor-bug-bounty.git
    cd vermithor-bug-bounty
    ```

2.  **Install external bug bounty tools:**

    ```bash
    chmod +x scripts/install_tools.sh
    ./scripts/install_tools.sh
    ```

    *Note: This script will install tools like Subfinder, httpx, Nuclei, Katana, ffuf, and sqlmap. You may need to restart your terminal or run `source ~/.bashrc` after installation to update your PATH.*

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**

    Vermithor uses LLMs for its AI capabilities. You need to set up API keys for your preferred LLM provider (e.g., OpenAI, Google Gemini, Anthropic Claude). You can do this via the `config` command:

    ```bash
    python vermithor/main.py config --set-key OPENAI_API_KEY your_openai_api_key_here
    # Or for other providers:
    # python vermithor/main.py config --set-key GEMINI_API_KEY your_gemini_api_key_here
    ```

## Usage

```bash
python vermithor/main.py --help
```

### Example Commands

*   **Intelligent Reconnaissance:**

    ```bash
    python vermithor/main.py recon example.com
    ```

*   **Analyze Scan Results:**

    ```bash
    python vermithor/main.py analyze path/to/nuclei_results.json
    ```

*   **Generate Bug Report:**

    ```bash
    python vermithor/main.py report path/to/finding_details.json
    ```

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on how to get involved.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Disclaimer

Vermithor is intended for educational and ethical hacking purposes only. Always ensure you have explicit permission before performing any security testing on a target. The developers are not responsible for any misuse or damage caused by this tool.
