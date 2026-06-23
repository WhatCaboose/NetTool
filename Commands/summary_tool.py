import socket
import platform
import subprocess
import ipaddress
import requests
from .myip import get_primary_ip, detect_interface_name 


def summary_command():
    print("\n--- NETTOOL SUMMARY ---")

    hostname = socket.gethostname()
    os_name = platform.system()

    local_ip = get_primary_ip()
    interface = detect_interface_name(local_ip)

    print("Hostname:", hostname)
    print("OS:", os_name)
    print("Interface:", interface if interface else "Unknown")
    print("Primary IPv4:", local_ip)

    if os_name.lower() == "windows":
        print("Default Gateway:", get_default_gateway())

        print("DNS Servers:", get_dns_servers())

        print("DHCP Enabled:", get_dhcp_enabled(interface))

        print("DHCP Server:", get_dhcp_server())
        
        print("Proxy:", get_proxy_info())

    wan_ip = get_wan_ip()
    print("WAN Address:", wan_ip)

    if is_cgnat(local_ip):
        print("CGNAT: Likely")
    else:
        print("CGNAT: No / Not detected")


def is_private_ip(ip_str):
    import ipaddress
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private
    except:
        return False
    
def run_powershell(command):
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    return result.stdout.strip()

def get_default_gateway():
    return run_powershell(
        "(Get-NetIPConfiguration | Where-Object {$_.IPv4DefaultGateway -ne $null} | Select-Object -First 1).IPv4DefaultGateway.NextHop"
    ) or "Unable to detect"


def get_dns_servers():
    output = run_powershell(
        "(Get-DnsClientServerAddress -AddressFamily IPv4 | "
        "Where-Object {$_.ServerAddresses.Count -gt 0} | "
        "Select-Object -First 1).ServerAddresses -join ', '"
    )
    return output or "Unable to detect"


def get_dhcp_enabled(interface_name):
    if not interface_name:
        return "Unable to detect"

    output = run_powershell(
        f"(Get-CimInstance Win32_NetworkAdapterConfiguration | "
        f"Where-Object {{$_.Description -like '*{interface_name}*' -or $_.Caption -like '*{interface_name}*'}} | "
        f"Select-Object -First 1).DHCPEnabled"
    )

    if output.lower() == "true":
        return "Yes"
    if output.lower() == "false":
        return "No"
    return "Unable to detect"


def get_dhcp_server():
    output = subprocess.run(
        ["ipconfig", "/all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    ).stdout

    for line in output.splitlines():
        if "DHCP Server" in line:
            return line.split(":")[-1].strip()

    return "Unable to detect"


def get_proxy_info():
    output = run_powershell("netsh winhttp show proxy")

    if "Direct access" in output:
        return "Direct access"

    return output or "Unable to detect"


def get_wan_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text.strip()
    except Exception:
        return "Unable to detect"


def is_cgnat(local_ip):
    try:
        ip = ipaddress.ip_address(local_ip)
        return ip in ipaddress.ip_network("100.64.0.0/10")
    except ValueError:
        return False