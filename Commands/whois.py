import ipaddress
import requests


def whois_command(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)

        if ip.is_private or ip.is_loopback or ip.is_link_local:
            print("WHOIS only works for public IPs.")
            return

        url = f"https://rdap.arin.net/registry/ip/{ip}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("RDAP lookup failed.")
            return

        data = response.json()

        print("\n--- WHOIS RESULT ---")

        print("Handle:", data.get("handle", "N/A"))
        print("Start IP:", data.get("startAddress", "N/A"))
        print("End IP:", data.get("endAddress", "N/A"))

        # CIDR fix
        cidr_list = data.get("cidr0_cidrs", [])
        if cidr_list:
            cidr = cidr_list[0]
            print("CIDR:", f"{cidr.get('v4prefix')}/{cidr.get('length')}")
        else:
            print("CIDR:", "N/A")

        print("Name:", data.get("name", "N/A"))

        # Clean org extraction
        entities = data.get("entities", [])
        if entities:
            vcard = entities[0].get("vcardArray", [])
            if len(vcard) > 1:
                for item in vcard[1]:
                    if item[0] == "fn":
                        print("Organization:", item[3])

        print("\nReference:", data.get("links", [{}])[0].get("href", "N/A"))

    except ValueError:
        print("Invalid IP format")

    except Exception as e:
        print("RDAP lookup error:", e)