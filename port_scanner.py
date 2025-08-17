import socket
import sys

def scan_port(host, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    result = scanner.connect_ex((host, port))  # returns 0 if open
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    scanner.close()

def main():
    target = input("Enter the target IP or hostname: ")
    print(f"Starting scan on {target}...\n")

    try:
        for port in range(1, 1025):
            scan_port(target, port)
    except KeyboardInterrupt:
        print("\n[!] Scan canceled by user.")
        sys.exit()

if __name__ == "__main__":
    main()
