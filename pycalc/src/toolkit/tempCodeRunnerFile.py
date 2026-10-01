import sys

from toolkit.calculator import calculate
from toolkit.errors import ToolkitError


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python -m toolkit calc \"EXPRESSION\"")
        print("  python -m toolkit convert VALUE --from UNIT --to UNIT")
        print("  python -m toolkit --help")
        sys.exit(0) 

    command = sys.argv[1].lower()

    try:
        if command == "calc":
            expression = " ".join(sys.argv[2:])
            result = calculate(expression)
            print(result)
        elif command == "convert":
            print("Convert command is under development.", file=sys.stderr)
            sys.exit(2)
        elif command == "--help":
            print("Toolkit CLI")
            print("Commands:")
            print("  calc \"EXPRESSION\"    - Evaluate a mathematical expression")
            print("  convert VALUE --from UNIT --to UNIT - Convert between units")
        else:
            print(f"Error: Unknown command '{command}'", file=sys.stderr)
            sys.exit(2)
    except ToolkitError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
