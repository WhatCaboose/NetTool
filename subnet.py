def subnet_command(network_str):
	try:
		import ipaddress

		network = ipaddress.ip_network(network_str, strict=False)

		print("\n--- SUBNET INFO ---")
		print("Network:", network.network_address)
		print("Broadcast:", network.broadcast_address)
		print("Mask:", network.netmask)
		print("Usable:", get_usable_hosts(network))
	except ValueError:
		print("Invalid subnet format. try again.")

def get_usable_hosts(network):
    if network.version == 4:
        if network.prefixlen == 32:
            return 1
        if network.prefixlen == 31:
            return 2
        return max(network.num_addresses - 2, 0)

    if network.version == 6:
        return network.num_addresses