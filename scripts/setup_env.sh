#!/bin/bash

# Vermithor Environment Setup Script
# This script sets up the Python environment for Vermithor.

echo "[*] Setting up Python environment..."

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[*] Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

echo "[*] Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "[+] Python environment setup complete. Virtual environment activated."
echo "    To deactivate, run: deactivate"
