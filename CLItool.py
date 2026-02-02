import argparse

def main():
    """
    Entry point for a simple CLI tool that calculates area.
    Demonstrates professional argument handling.
    """
    parser = argparse.ArgumentParser(description="Tool to calculate Rectangle Area.")

    # Adding named arguments
    parser.add_argument("--width", type=float, required=True, help="Width of the rectangle")
    parser.add_argument("--height", type=float, required=True, help="Height of the rectangle")
    parser.add_argument("--unit", type=str, default="cm", help="Unit of measurement (default: cm)")

    args = parser.parse_args()

    # Perform the calculation
    area = args.width * args.height
    print(f"📐 The area is {area}{args.unit}²")

if __name__ == "__main__":
    # To test this, run in terminal: python script.py --width 10 --height 5
    main()
