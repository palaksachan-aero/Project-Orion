def main():
    print("=== Rocket Launch Decision System ===")

    try:
        wind_speed = float(input("Enter wind speed (km/h): "))
    except ValueError:
        print("Error: Please enter a valid number for wind speed.")
        return

    if wind_speed < 0:
        print("Error: Invalid wind speed. Speed cannot be negative.")
        return

    is_raining = input("Is it raining? (yes or no): ").strip().lower()

    if wind_speed > 30:
        print("Result: Launch Cancelled (Wind speed exceeds 30 km/h)")
    elif is_raining == "yes":
        print("Result: Launch Delayed (It is currently raining)")
    elif is_raining == "no":
        print("Result: Launch Approved 🚀")
    else:
        print("Result: Invalid input for rain. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()