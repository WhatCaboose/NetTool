<<<<<<< HEAD
from Commands.subnet import subnet_command
from Commands.ip_classifier import ip_command
from Commands.summary_tool import summary_command
from Commands.inspect import inspect_command
from Commands.trace_tool import trace_command
from Commands.dns_tool import dns_command
from Commands.about_tool import about_command
from Commands.help_tool import help_command

COMMANDS = {
	"subnet": subnet_command,
	"summary": summary_command,
	"inspect": inspect_command,
	"trace": trace_command,
	"dns": dns_command,
	"about": about_command,
}

def process_command(user_input):
	parts = user_input.split()

	if not parts:
		return
	
	cmd = parts[0].lower()
	args = parts[1:]

	    	
	if cmd == "help":
		help_command()
		return
	
	if args and args[0] == "?":
		help_command(cmd)
		return
	
	command_function = COMMANDS.get(cmd)

	try:
		if args:
			command_function(*args)
		else:
			command_function()
	except TypeError:
		print(f"Usage error for '{cmd}'. Type 'help' for syntax.")


def main():
	print("NetTool: type 'help' for commands")
	while True:
		user_input = input("NetTool: ").strip()
	
		if user_input.lower() == "exit":
			print("Exiting NetTool...")
			break

		process_command(user_input)





if __name__ == "__main__":
=======
from Commands.subnet import subnet_command
from Commands.ip_classifier import ip_command
from Commands.summary_tool import summary_command
from Commands.inspect import inspect_command
from Commands.trace_tool import trace_command
from Commands.dns_tool import dns_command
from Commands.about_tool import about_command
from Commands.help_tool import help_command

COMMANDS = {
	"subnet": subnet_command,
	"summary": summary_command,
	"inspect": inspect_command,
	"trace": trace_command,
	"dns": dns_command,
	"about": about_command,
}

def process_command(user_input):
	parts = user_input.split()

	if not parts:
		return
	
	cmd = parts[0].lower()
	args = parts[1:]

	    	
	if cmd == "help":
		help_command()
		return
	
	if args and args[0] == "?":
		help_command(cmd)
		return
	
	command_function = COMMANDS.get(cmd)

	try:
		if args:
			command_function(*args)
		else:
			command_function()
	except TypeError:
		print(f"Usage error for '{cmd}'. Type 'help' for syntax.")


def main():
	print("NetTool: type 'help' for commands")
	while True:
		user_input = input("NetTool: ").strip()
	
		if user_input.lower() == "exit":
			print("Exiting NetTool...")
			break

		process_command(user_input)





if __name__ == "__main__":
>>>>>>> 86b9eb6969b796b62ee614f2ae224f95c95f22ff
	main()