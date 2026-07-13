
import msvcrt 
import time


def main():
    print("=== Rocket Countdown System v2.0 ===")
    print("Safety Feature: Press the 'A' key at any time to ABORT the launch.")
    print()

   
    try:
        countdown = int(input("Enter countdown value (seconds): "))
    except ValueError:
        print("Error: Countdown must be a positive integer.")
        return

    if countdown <= 0:
        print("Error: Countdown must be greater than zero.")
        return

    
    print()
    print("==========")
    print("Rocket Launch Sequence Initiated")
    print("==========")
    print()

    
    while countdown > 0:
        print(f"T - {countdown}")

        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()
            if key == "a":
                print()
                print("🚨🚨🚨 LAUNCH ABORTED BY MISSION CONTROL! 🚨🚨🚨")
                print("Safing systems activated. Core stage depressurizing.")
                return

        if countdown == 5:
            print(">> [SYSTEM] Core Stage Engine Start Sequence Initiated...")
        elif countdown == 3:
            print(">> [SYSTEM] Main Liquid Hydrogen Fuel Valves Open...")
        elif countdown == 1:
            print(">> [SYSTEM] Solid Rocket Booster Ignition Command Sent...")

        time.sleep(1)
        countdown -= 1

    print()
    print("Ignition...")
    time.sleep(0.5)
    print("Lift Off 🚀")


if __name__ == "__main__":
    main()