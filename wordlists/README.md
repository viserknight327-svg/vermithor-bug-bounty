# Wordlists

This directory contains various wordlists that can be used for fuzzing, bruteforcing, and content discovery during bug bounty hunting.

## Included Wordlists (Examples)

*   `subdomains.txt`: Common subdomain names.
*   `paths.txt`: Common web application paths and directories.
*   `params.txt`: Common HTTP parameter names.

## How to Use

These wordlists are intended to be used with tools like `ffuf`, `dirsearch`, or custom scripts for various enumeration and discovery tasks.

**Example with `ffuf`:**

```bash
ffuf -w wordlists/paths.txt:FUZZ -u https://example.com/FUZZ
```

## Contributing New Wordlists

We welcome contributions of high-quality, relevant wordlists. Please ensure that any submitted wordlists are publicly available and do not contain sensitive information.
