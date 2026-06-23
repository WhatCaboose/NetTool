def ip_command(ip_str):
	try:

		import ipaddress
		ip = ipaddress.ip_address(ip_str)

		if  ip.is_loopback:
			print("Loopback")
		elif ip.is_link_local:
			print("Link Local")
		elif ip.is_multicast:
			print("Multicast")
		elif ip.is_global:
			print("Public Internet IP")
		elif ip.is_reserved:
			print("Reserved/Experimental")
		elif ip.is_private:
			print("Private IP")

	except ValueError:
		print("Invalid IP format. Try again.")