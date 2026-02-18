import sys

def display_arguments(args: list) -> None:
	print("=== Command Quest ===")
	program_name: str = args[0]

	if len(args) == 1:
		print("No arguments provided!")
		print(f"Program name: {program_name}")
		print(f"Total arguments: {len(args)}")
		return
	print(f"Program name: {program_name}")
	print(f"Arguments received: {len(args) - 1}")
	i: int = 1
	while i < len(args):
		print(f"Argument {i}: {args[i]}")
		i += 1
	print(f"Total arguments: {len(args)}")


def main() -> None:
	display_arguments(sys.argv)


if __name__ == "__main__":
	main()