# Week-01/Day-03/rocket_countdown_v3.py
import msvcrt  
import time


def print_milestone(message):
    """Helper function to cleanly format control room system updates"""
    print(f">> [CONTROL] {message}")


def main():
    print("=== Rocket Countdown System v3.0 ===")
    print("MISSION: Falcon Heavy Integration Simulation")
    print("Safety Protocol: Press the 'A' key at any time to execute manual ABORT.")
    print()

    try:
        countdown = int(input("Initialize countdown sequence (Enter 30 for full simulation): "))
    except ValueError:
        print("Error: Countdown must be a positive integer.")
        return

    if countdown <= 0:
        print("Error: Countdown must be greater than zero.")
        return

    print()
    print("========================================")
    print("   TERMINAL COUNTDOWN SEQUENCE ACTIVE   ")
    print("========================================")
    print()

  
    while countdown > 0:
        print(f"T - {countdown} seconds")

        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()
            if key == "a":
                print()
                print("🚨🚨🚨 FLIGHT ABORT TRIPPED BY MISSION CONTROL! 🚨🚨🚨")
                print("Sequence terminated. Recocking propellant valves. Safe mode engaged.")
                return

        if countdown == 30:
            print_milestone("Commencing final terminal countdown loop...")
        elif countdown == 27:
            print_milestone("Weather Check: Clear skies. Upper-level winds within structural margins.")
        elif countdown == 24:
            print_milestone("Fuel Pressure Check: Liquid Oxygen (LOX) tanks pressurized and stable.")
        elif countdown == 20:
            print_milestone("Telemetry Check: Downlink secure. Ground stations reporting solid lock.")
        elif countdown == 16:
            print_milestone("Wind Check: Surface crosswinds nominal at 8 knots.")
        elif countdown == 12:
            print_milestone("Navigation Computer Ready: Internal flight path tracking alignment complete.")

      
        elif countdown == 10:
            print_milestone("Crew Ready: Astronauts cabin pressure sealed, all visors down. Go for flight.")
        elif countdown == 8:
            print_milestone("Ground Systems Ready: Strongback retraction sequence initiated.")
        elif countdown == 6:
            print_milestone("Launch Director Poll: [LD] is GO for launch.")
        elif countdown == 5:
            print_milestone("Mission Director Poll: [MD] is GO for launch.")
        elif countdown == 4:
            print_milestone("Flight Computer Command: Startup. Internal power systems activated.")
        elif countdown == 3:
            print_milestone("Engine Ignition Sequence Start... Core stage vectoring unlocked.")
        elif countdown == 2:
            print_milestone("Main Engine Start. Turbopumps at 100% rated performance.")
        elif countdown == 1:
            print_milestone("Solid Rocket Booster Ignition Command Sent. All systems are GO.")

        time.sleep(1)
        countdown -= 1

    print()
    print("==============================")
    print("🚀 LIFT OFF! Go Falcon! Go Orion! 🚀")
    print("==============================")


if __name__ == "__main__":
    main()