import sys

from toolkit.calculator import calculate
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print('  python -m toolkit calc "EXPRESSION"')
        print("  python -m toolkit convert VALUE --from UNIT --to UNIT")
        print("  python -m toolkit --help")
        sys.exit(0)

    command = sys.argv[1].lower()

    try:
        if command == "calc":
            expression = " ".join(sys.argv[2:])
            result = calculate(expression)
            print(result)
        elif command == 'convert':
            if len(sys.argv) < 7:
                print('Error: Insufficient arguments', file=sys.stderr)
                print("Usage: python -m toolkit convert VALUE --from UNIT --to UNIT")
                sys.exit(2)
            else:
                obj_value = sys.argv[2]
                from_unit = sys.argv[4]
                to_unit = sys.argv[6]
                value = float(obj_value)
                result = round(convert(value,from_unit,to_unit),4)
                print(f'{value} {from_unit} = {result} {to_unit}')
        elif command == "--help":
            print("Toolkit CLI")
            print("Commands:")
            print('calc "EXPRESSION" - Evaluate a mathematical expression')
            print("convert VALUE --from UNIT --to UNIT - Convert between units")
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