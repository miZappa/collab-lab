"""Network device checker - SachinVermea style.
Network Automation / DevNet: validate IPs, try a TCP
connect to port 22/443, report up/down in a table.
Usage: python persona_sachin_netdev_check.py 10.0.0.1 8.8.8.8
"""
import ipaddress, socket, sys

def check(host, port=22, timeout=2):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return host, "INVALID-IP", "-"
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return host, "UP", str(port)
    except Exception as e:
        return host, "DOWN", type(e).__name__

def main():
    hosts = sys.argv[1:] or ["8.8.8.8", "1.1.1.1"]
    print(f"{'HOST':<16} {'STATUS':<12} {'DETAIL'}")
    for host in hosts:
        h, status, detail = check(host)
        print(f"{h:<16} {status:<12} {detail}")

if __name__ == "__main__":
    main()
