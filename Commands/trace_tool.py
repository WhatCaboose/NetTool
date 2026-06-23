import platform
import subprocess
import ipaddress
import re
from database.known_IXPs import known_IXP_networks
from .help_tool import help_command
from .asn_tool import get_asn_info
import socket
    
asn_cache = {}

SPECIAL_NETWORKS = {
    "10.0.0.0/8": "Private Network",
    "172.16.0.0/12": "Private Network",
    "192.168.0.0/16": "Private Network",
    "100.64.0.0/10": "Carrier-Grade NAT",
    "127.0.0.0/8": "Loopback",
    "169.254.0.0/16": "Link-Local",
    "192.0.0.0/24": "Special-Purpose Address",
    "198.18.0.0/15": "Benchmark Testing Network",
    "224.0.0.0/4": "Multicast",
    "240.0.0.0/4": "Reserved / Experimental",
}

def trace_command(target, *flags):

    max_hops = 15

    if "?" in flags:
        help_command("trace")
        return

    if "-h" in flags:
        try:
            index = flags.index("-h")
            max_hops = int(flags[index + 1])
        except (IndexError, ValueError):
            print("Invalid hop count.")
            return
    
    show_org = "--org" in flags or "-o" in flags
    
    system = platform.system().lower()

    if system == "windows":
        cmd = ["tracert", "-d", "-h", str(max_hops), target]
    elif system == "linux":
        cmd = ["traceroute", "-m", str(max_hops), target]
    else:
        print("Trace is not supported on this OS yet.")
        return

    print(f"\n--- TRACE ROUTE: {target} ---\n")

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        for line in process.stdout:
            clean_line = line.rstrip()

            if not show_org:
                print(clean_line)
                continue

            hop_ip = extract_ip(clean_line)

            if hop_ip:
                org = get_hop_org(hop_ip)
                print(f"{clean_line}   [{org}]")
            else:
                print(clean_line)
        
        process.wait()

    except subprocess.TimeoutExpired:
        print("Trace timed out.")

    except FileNotFoundError:
        print("Traceroute command not found.")
        if system == "linux":
            print("Try installing traceroute: sudo apt install traceroute")

def extract_ip(line):
    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
    return match.group(0).strip() if match else None

def format_asn_result(asn):
    asn_number = asn.get("asn", "N/A")
    name = asn.get("name", "Unknown")

    if asn_number == "N/A":
        return f"{name}"

    return f"AS{asn_number} | {name}"

def get_hop_org(ip):
    if ip in asn_cache:
        return asn_cache[ip]

    try:
        ip_obj = ipaddress.ip_address(ip)

        for network, label in SPECIAL_NETWORKS.items():
            if ip_obj in ipaddress.ip_network(network):
                asn_cache[ip] = label
                return label
            
        for network, label in known_IXP_networks.items():
            if ip_obj in ipaddress.ip_network(network):
                asn_cache[ip] = label
                return label
       
        else:
            asn = get_asn_info(ip)
            if asn:
                result = format_asn_result(asn)
            else:
                result = "Unknown ASN"

        asn_cache[ip] = result
        return result

    except ValueError:
        return "Invalid IP"