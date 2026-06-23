import ipaddress
import dns.resolver
import socket

SUPPORTED_RECORDS = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
DEFAULT_RECORDS = ["A", "AAAA"]

def dns_command(target, *args):
    reverse_mode = "-r" in args or "--reverse" in args

    if reverse_mode:
        reverse_dns_lookup(target)
        return

    record_type = None

    for arg in args:
        upper_arg = arg.upper()
        if upper_arg in SUPPORTED_RECORDS:
            record_type = upper_arg

    if record_type:
        query_record(target, record_type)
    else:
        for record in DEFAULT_RECORDS:
            query_record(target, record)

def query_record(hostname, record_type):
    try:
        answers = dns.resolver.resolve(hostname, record_type)

        print(f"\n{record_type} Records ({len(answers)}):")
        for answer in answers:
            print(answer.to_text())

    except Exception:
        print(f"\n{record_type} Records (0)")

def forward_dns_lookup(hostname):
    print("\n--- DNS LOOKUP ---")
    print("Hostname:", hostname)

    for record_type in ["A", "AAAA"]:
        try:
            answers = dns.resolver.resolve(hostname, record_type)

            print(f"\n{record_type} Records ({len(answers)}):")
            for answer in answers:
                print(answer.to_text())

        except Exception:
            print(f"\n{record_type} Records (0)")


def reverse_dns_lookup(ip_str):
    print("\n--- REVERSE DNS LOOKUP ---")
    print("IP:", ip_str)

    try:
        ipaddress.ip_address(ip_str)
    except ValueError:
        print("Invalid IP address.")
        return

    try:
        hostname = socket.gethostbyaddr(ip_str)[0]
        print("Hostname:", hostname)

    except socket.herror:
        print("Hostname: No PTR record")

    except socket.timeout:
        print("Hostname: Lookup timed out")

    except Exception:
        print("Hostname: Reverse DNS lookup failed")