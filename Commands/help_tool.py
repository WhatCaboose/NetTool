from Utils.help_data import COMMAND_HELP


def help_command(command_name=None):
    if command_name is None:
        print("\n--- NETTOOL HELP ---")
        print("Type '<command> ?' for command-specific help.\n")

        for command, info in COMMAND_HELP.items():
            print(f"{command:<10} {info['description']}")
        return

    info = COMMAND_HELP.get(command_name)

    if info is None:
        print(f"No help found for '{command_name}'.")
        return

    print(f"\n--- {command_name.upper()} HELP ---")
    print("Description:", info["description"])
    print("Usage:", info["usage"])

    print("\nFlags:")
    for flag, description in info["flags"].items():
        print(f"{flag:<15} {description}")

    print("\nExamples:")
    for example in info["examples"]:
        print(example)