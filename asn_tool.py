import dns.resolver
import requests

def get_asn_name(asn):

    result = lookup_asn_name_cymru(asn)
    if result:
        return result

    return "Unknown"

def lookup_asn_name_cymru(asn):
    try:
        query = f"AS{asn}.asn.cymru.com"
        answers = dns.resolver.resolve(query, "TXT")

        raw = answers[0].to_text().strip('"')
        parts = [p.strip() for p in raw.split("|")]

        return parts[4] if len(parts) > 4 else None

    except Exception:
        return None
    
def get_asn_info(ip_str):
    result = lookup_team_cymru(ip_str)
    if result:
        return result

    result = lookup_ipinfo(ip_str)
    if result:
        return result

    return None

    
def lookup_team_cymru(ip_str):
    try:
        reversed_ip = ".".join(reversed(ip_str.split(".")))
        query = f"{reversed_ip}.origin.asn.cymru.com"

        answers = dns.resolver.resolve(query, "TXT")

        raw = answers[0].to_text().strip('"')
        parts = [p.strip() for p in raw.split("|")]

        asn = parts[0]
        asn_name = get_asn_name(asn)

        return {
            "asn": asn,
            "prefix": parts[1],
            "country": parts[2],
            "registry": parts[3],
            "allocated": parts[4],
            "name": asn_name,
            }

    except Exception:
        return None
    


def lookup_ipinfo(ip_str):
    try:
        url = f"https://ipinfo.io/{ip_str}/json"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()
        org = data.get("org", "")

        if not org:
            return None

        parts = org.split(" ", 1)

        asn = parts[0].replace("AS", "")
        name = parts[1] if len(parts) > 1 else "Unknown"

        return {
            "asn": asn,
            "prefix": "N/A",
            "country": data.get("country", "N/A"),
            "registry": "N/A",
            "allocated": "N/A",
            "name": name,
            }

    except Exception:
        return None
    