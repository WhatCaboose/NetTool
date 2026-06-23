VERSION = "0.9.1"
RELEASE = "Beta"
PLATFORM = "Windows 10/11"
AUTHOR = "Nicholas Greenlee"


def about_command():
    print(f"""
--- ABOUT NETTOOL ---

NetTool v{VERSION}
Release: {RELEASE}
Platform: {PLATFORM}
Author: {AUTHOR}

Description:
NetTool is a command-line networking utility built for
network students, technicians, homelab users, and enthusiasts.

Core Features:
- Local network summary
- DNS and reverse DNS lookups
- IP ownership and ASN inspection
- ASN-enhanced traceroute
- Subnet calculations
- Built-in command help

Planned Features:
- Linux support
- Port mapping
- DNS comparison
- Diagnose mode

Motto:
"It doesn't need to be pretty. It needs to work."
""")