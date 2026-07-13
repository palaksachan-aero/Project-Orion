# Week-01/Day-03/rocket_countdown.py
import time


def main():
    print("=== Rocket Countdown System ===")

    try:
        countdown = int(input("Enter countdown value (seconds): "))
    except ValueError:
        print("Error: Invalid input. Countdown must be a whole number (integer).")
        return

    if countdown <= 0:
        print(
            "Error: Countdown must be a positive number greater than 0 to initialize sequence."
        )
        return

    print("\n==========")
    print("Rocket Launch Sequence")
    print("==========\n")

    while countdown > 0:
        print(f"T - {countdown}")
        time.sleep(1) 
        countdown -= 1

    
    print("Ignition...")
    time.sleep(0.5)
    print("Lift Off 🚀")


if __name__ == "__main__":
    main()