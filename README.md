
# (SLFI - Simple Local File Inclusion) LFI Detection Tool

A simple command-line tool for detecting Local File Inclusion (LFI) vulnerabilities in web applications. This tool leverages various payloads to test if the application is susceptible to LFI.

## Features

- **Payload Injection**: Attempts multiple payloads to check for LFI vulnerabilities.
- **File Targeting**: Checks for common sensitive files such as `/etc/passwd`, `/proc/self/environ`, and Windows-specific files.
- **Customizable**: Easily extend the payloads and file targets as needed.
- **Colorful Output**: Utilizes the `colorama` library for clear, colored terminal output.
- **Banner Display**: Displays an ASCII banner using the `pyfiglet` library.

## Requirements

Make sure you have Python 3.x installed. This tool requires the following packages:

- `requests`
- `colorama`
- `pyfiglet`

These packages can be installed automatically if missing.
```
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JustDanz/SLFI.git
   cd SLFI
   ```

2. Run the script to install required packages:
   ```bash
   python SLFI.py
   ```

## Usage

Run the tool with:
```bash
python SLFI.py
```

You will be prompted to enter the target URL (e.g., `http://example.com/page`). The tool will then perform the LFI checks.

### Example
```bash
Masukkan URL target (contoh: http://example.com/page):
```

## How It Works

1. The script prompts for a target URL.
2. It appends various payloads to the URL to attempt to access sensitive files.
3. For each payload, it checks the server response and searches for known patterns to identify potential LFI vulnerabilities.
4. Results are displayed in the terminal with color-coded output for easy reading.

## Notes

- Ensure you have permission to test the target application.
- Use this tool responsibly and ethically.
- The tool may produce false positives; manual verification is recommended.


## Author

Made By JustDanz

```

### Instructions to Customize
- Replace `https://github.com/JustDanz/SLFI.git` with the actual URL of your GitHub repository.
- Add more details if necessary, such as contribution guidelines or a detailed explanation of how to customize payloads.
- If you plan to add more features in the future, consider mentioning them in the README as "Upcoming Features" or "Roadmap".

```
## For English Command

# LFI Detection Tool

A simple command-line tool for detecting Local File Inclusion (LFI) vulnerabilities in web applications. This tool uses various payloads to test if the application is susceptible to LFI attacks.

## Features

- **Payload Injection**: Attempts multiple payloads to check for LFI vulnerabilities.
- **File Targeting**: Checks for common sensitive files such as `/etc/passwd`, `/proc/self/environ`, and Windows-specific files.
- **Customizable**: Easily extend the payloads and file targets as needed.
- **Colorful Output**: Utilizes the `colorama` library for clear, colored terminal output.
- **Banner Display**: Displays an ASCII banner using the `pyfiglet` library.

## Requirements

Make sure you have Python 3.x installed. This tool requires the following packages:

- `requests`
- `colorama`
- `pyfiglet`

These packages can be installed automatically if missing.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JustDanz/SLFI.git
   cd SLFI
   ```

2. Run the script to install required packages:
   ```bash
   python SLFI_English.py
   ```

## Usage

Run the tool with:
```bash
python SLFI_English.py
```

You will be prompted to enter the target URL (e.g., `http://example.com/page`). The tool will then perform the LFI checks.

### Example
```bash
Enter target URL (e.g., http://example.com/page):
```
