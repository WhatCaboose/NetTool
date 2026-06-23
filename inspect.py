import ipaddress

from .whois import whois_command
from .ip_classifier import ip_command
from .asn_tool import get_asn_info


def inspect_command(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)

        print("\n=== NETTOOL INSPECT ===")

        # 1. IP classification
        print("\n[IP CLASSIFICATION]")
        if ip.is_private:
            print("Type: Private")
        elif ip.is_loopback:
            print("Type: Loopback")
        elif ip.is_multicast:
            print("Type: Multicast")
        else:
            print("Type: Public")

        # 2. WHOIS (reuse logic, but ideally refactor later)
        print("\n[WHOIS]")
        whois_command(ip_str)

        asn_info = get_asn_info(ip_str)

        print("\n--- ASN INFO ---")
        if asn_info:
            print("ASN:", asn_info["asn"])
            print("Prefix:", asn_info["prefix"])
            print("Country:", asn_info["country"])
            print("Registry:", asn_info["registry"])
            print("Allocated:", asn_info["allocated"])
        else:
            print("ASN data unavailable")
    except ValueError:
        print("Invalid IP format")