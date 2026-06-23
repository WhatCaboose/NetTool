import socket
import platform
import subprocess
import re

def myip_command():
    print("\n--- LOCAL IP INFO ---")
    print("Hostname:", socket.gethostname())

    local_ip = get_primary_ip()
    print("Primary IPv4:", local_ip)

    interface_name = detect_interface_name(local_ip)

    if interface_name:
        print("Interface:", interface_name)
    else:
        print("Interface: Unable to detect")

    print("OS", platform.system())

def get_primary_ip():
    """
    Finds the primary outbound IPv4 without sending real traffic.
    It opens a UDP socket twoard a public IP only to let the OS choose
    the default outbound interface.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "Unable to detect"
    
def detect_interface_name(local_ip):
    system = platform.system().lower()

    try:
        if system == "windows":
            return detect_windows_interface(local_ip)
        elif system == "linux":
            return detect_linux_interface(local_ip)
        else:
            return None
    except Exception:
        return None
    
def detect_windows_interface(local_ip):
    result = subprocess.run(
        [   "powershell",
            "-NoProfile",
            "-Command",
            f"Get-NetIPAddress -AddressFamily IPv4 | "
            f"Where-Object {{$_.IPAddress -eq '{local_ip}'}} | "
            f"Select-Object -ExpandProperty InterfaceAlias"
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    interface = result.stdout.strip()
    return interface if interface else None

def detect_linux_interface(local_ip):
    result = subprocess.run(
        ["ip", "-o", "-4", "addr", "show"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    for line in result.stdout.splitlines():
        if local_ip in line:
            match = re.search(r"\d+:\s+([^ ]+)", line)
            if match:
                return match.group(1)
    return None