COMMAND_HELP = {
    "summary": {
        "description": "Show local system and network information.",
        "usage": "summary",
        "flags": {
            "?": "Show summary help."
        },
        "examples": [
            "summary"
        ]
    },

    "inspect": {
        "description": "Inspect an IP address using RDAP and ASN data.",
        "usage": "inspect <ip>",
        "flags": {
            "?": "Show inspect help."
        },
        "examples": [
            "inspect 8.8.8.8",
            "inspect 9.9.9.9"
        ]
    },

    "trace": {
        "description": "Run traceroute with optional ASN organization info.",
        "usage": "trace <host/IP> [flags]",
        "flags": {
            "-o, --org": "Show ASN and organization info for each hop.",
            "-h <number>": "Set maximum hop count. Default is 15.",
            "?": "Show trace help."
        },
        "examples": [
            "trace 8.8.8.8",
            "trace 8.8.8.8 -o",
            "trace google.com -o -h 30"
        ]
    },

    "dns": {
        "description": "Resolve DNS records or perform reverse DNS lookups.",
        "usage": "dns <hostname> [record] OR dns <ip> -r",
        "flags": {
            "-r, --reverse": "Perform reverse DNS lookup on an IP address.",
            "?": "Show DNS help."
        },
        "examples": [
            "dns google.com",
            "dns google.com MX",
            "dns google.com TXT",
            "dns 8.8.8.8 -r"
        ]
    },

    "subnet": {
        "description": "Calculate subnet information from CIDR notation.",
        "usage": "subnet <network/CIDR>",
        "flags": {
            "?": "Show subnet help."
        },
        "examples": [
            "subnet 192.168.1.0/24",
            "subnet 10.10.10.10/16"
        ]
    },

    "about": {
        "description": "Show NetTool version and project information.",
        "usage": "about",
        "flags": {
            "?": "Show about help."
        },
        "examples": [
            "about"
        ]
    },

    "help": {
        "description": "Show general or command-specific help.",
        "usage": "help OR <command> ?",
        "flags": {},
        "examples": [
            "help",
            "trace ?",
            "dns ?"
        ]
    },

    "exit": {
        "description": "Exit NetTool.",
        "usage": "exit",
        "flags": {},
        "examples": [
            "exit"
        ]
    }
}