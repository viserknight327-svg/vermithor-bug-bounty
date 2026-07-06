#!/bin/bash

# Vermithor Tool Installation Script
# This script installs common bug bounty tools used by Vermithor.

echo "[*] Updating system..."
sudo apt-get update -y

echo "[*] Installing dependencies..."
sudo apt-get install -y git curl wget jq python3 python3-pip

# Install Go (needed for many tools)
if ! command -v go &> /dev/null; then
    echo "[*] Installing Go..."
    wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    rm go1.22.0.linux-amd64.tar.gz
fi

# Install ProjectDiscovery tools
echo "[*] Installing ProjectDiscovery tools..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest

# Install other useful tools
echo "[*] Installing other bug bounty tools..."
go install github.com/ffuf/ffuf/v2@latest
sudo apt-get install -y sqlmap

# Add Go binaries to PATH
export PATH=$PATH:$(go env GOPATH)/bin
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc

echo "[+] Installation complete! Please restart your terminal or run 'source ~/.bashrc'."
