**NetTool Beta 0.9.1**



"It doesn't need to be pretty. It needs to work."



**Overview**



NetTool is a lightweight network diagnostics and troubleshooting utility designed for technicians, students, and homelab enthusiasts.



The goal of NetTool is to provide useful information even when networks are misconfigured, unstable, or experiencing issues.



**Beta Notice:**



**WARNING:** This software is currently in beta.



NetTool is not signed by a Certificate Authority (CA). Windows may display SmartScreen or security warnings when launching the application.



For security reasons, only download official releases distributed by the author.



**Available Commands:**



* help
* summary
* inspect
* dns
* trace
* subnet
* about



**Key Features:**



* Enhanced traceroute with ASN identification (trace -o)
* DNS and reverse DNS lookups
* Local network summary and diagnostics
* Public IP and ISP information
* Subnet calculations
* Special-purpose address recognition
* Carrier-Grade NAT (CGNAT) detection



**Requirements:**



* Windows 10
* Windows 11
* Internet connection required for ASN and DNS lookups



**Known Issues:**



* Linux is not currently supported.
* Some antivirus products may generate false positives due to PyInstaller packaging and the application's networking functionality.
* ASN lookup accuracy depends on available external data sources.



**Version:**



NetTool Beta 0.9.1



Built and tested on Windows 11.

