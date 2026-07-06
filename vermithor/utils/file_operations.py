import json
import os

def read_json_file(file_path):
    """Reads and parses a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json_file(data, file_path):
    """Writes data to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def read_text_file(file_path):
    """Reads a plain text file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        return f.read()

def write_text_file(content, file_path):
    """Writes content to a plain text file."""
    with open(file_path, 'w') as f:
        f.write(content)
