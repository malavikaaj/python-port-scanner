import socket

def scan_ports(ip):
    print(f"Scanning {ip} for open ports...")
    open_ports = []
    
    for port in range(20, 1025):  # Scanning common ports (20-1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout to avoid long waits
        result = sock.connect_ex((ip, port))  # 0 means open
        if result == 0:
            open_ports.append(port)
        sock.close()

    print(f"Open ports on {ip}: {open_ports}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_ports(target_ip)
