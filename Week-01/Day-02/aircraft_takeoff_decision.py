
def main():
    print("=== Aircraft Takeoff Decision System ===")

    try:
        runway_length = float(input("Enter runway length (meters): "))
        aircraft_weight = float(input("Enter aircraft weight (tons): "))
        visibility = float(input("Enter visibility (meters): "))
    except ValueError:
        print("Error: Please enter valid numerical values.")
        return

    
    if runway_length < 0 or aircraft_weight < 0 or visibility < 0:
        print("Error: Inputs cannot be negative values.")
        return

    if visibility < 1000:
        print("Result: Takeoff Delayed (Visibility is below 1000 m)")

    elif runway_length < 1800:
        print("Result: Takeoff Not Safe (Runway is shorter than 1800 m)")

    elif aircraft_weight > 250:
        print("Result: Reduce Weight Before Takeoff (Weight exceeds 250 tons)")

    else:
        print("Result: Takeoff Approved 🛫")


if __name__ == "__main__":
    main()