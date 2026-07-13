# Week-01/Day-03/airport_console.py
import time

aircraft_data = {}


def clean_header(title):
    """Helper function to eliminate code repetition for menu and report headers"""
    print()
    print("==================================")
    print(f"      {title.upper()}      ")
    print("==================================")


def validate_positive_float(prompt, error_msg):
    """Reusable validator that ensures numeric input is positive and valid"""
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print(f"❌ Input Error: {error_msg} cannot be negative.")
                continue
            return val
        except ValueError:
            print("❌ Input Error: Please enter a valid numerical value.")


def register_aircraft():
    """Option 1: Collects and validates comprehensive aircraft registry profiles"""
    clean_header("Register Aircraft")

    
    aircraft_data["name"] = input("Aircraft Designation/Name: ").strip() or "NX-Alpha Prototype"
    aircraft_data["mach"] = validate_positive_float("Enter Speed (Mach): ", "Mach number")
    aircraft_data["altitude"] = validate_positive_float("Enter Altitude (meters): ", "Altitude")
    
    
    while True:
        fuel = validate_positive_float("Enter Fuel Percentage (0-100): ", "Fuel status")
        if fuel > 100:
            print("❌ Input Error: Fuel tank volume cannot exceed 100%.")
            continue
        aircraft_data["fuel"] = fuel
        break

   
    aircraft_data["log_num"] = input("Flight Log Number: ").strip() or "FL-9901"
    aircraft_data["date"] = input("Mission Date (DD-MM-YYYY): ").strip() or time.strftime("%d-%m-%Y")
    aircraft_data["pilot"] = input("Pilot-in-Command Name: ").strip() or "Test Pilot"
    aircraft_data["destination"] = input("Destination Airfield: ").strip() or "Station Alpha"

    print(f"\n✅ System Confirmation: {aircraft_data['name']} safely committed to operational memory.")


def display_aircraft():
    """Option 2: Pulls active profile from global data dictionary"""
    clean_header("Display Aircraft Profile")

    if not aircraft_data:
        print("⚠️ NO ACTIVE REGISTRY: No aircraft currently occupying the hangar workspace.")
        return

    print(f"Aircraft Name : {aircraft_data['name']}")
    print(f"Flight Log #  : {aircraft_data['log_num']}")
    print(f"Mission Date  : {aircraft_data['date']}")
    print(f"Pilot ID      : {aircraft_data['pilot']}")
    print(f"Destination   : {aircraft_data['destination']}")
    print(f"Mach Velocity : {aircraft_data['mach']:.2f} Mach")
    print(f"Altitude Zone : {aircraft_data['altitude']:.0f} m")
    print(f"Fuel Reserve  : {aircraft_data['fuel']:.1f}%")


def analyze_flight():
    """Option 3: Evaluates data pipelines using independent 'if' logic matrices"""
    clean_header("Analyze Flight Status")

    if not aircraft_data:
        print("⚠️ NO ACTIVE DATA: Initialize aircraft registration before running calculations.")
        return

   
    mach = aircraft_data["mach"]
    altitude = aircraft_data["altitude"]
    fuel = aircraft_data["fuel"]

  
    if mach < 0.8: regime = "Subsonic"
    elif 0.8 <= mach <= 1.2: regime = "Transonic"
    elif 1.2 < mach <= 5.0: regime = "Supersonic"
    else: regime = "Hypersonic"

  
    if fuel > 70: fuel_status = "Excellent"
    elif 40 <= fuel <= 70: fuel_status = "Good"
    elif 20 <= fuel < 40: fuel_status = "Low"
    else: fuel_status = "Critical"

  
    if altitude <= 3000: alt_zone = "Low Altitude"
    elif 3001 <= altitude <= 9000: alt_zone = "Medium Altitude"
    elif 9001 <= altitude <= 15000: alt_zone = "High Altitude"
    else: alt_zone = "Near Space Operations"

    
    warnings = []
    
    if fuel < 20:
        warnings.append("⚠ CRITICAL HAZARD: Fuel depletion imminent. Main engine flameout risk.")
    elif fuel < 40:
        warnings.append("⚠ WARNING: Fuel reserves below standard operating margins.")
        
    if (regime == "Supersonic" or regime == "Hypersonic") and alt_zone == "Low Altitude":
        warnings.append("⚠ AERODYNAMIC RISK: Flight profile causes high dynamic pressure loads on airframe.")
        
    if regime == "Subsonic" and alt_zone == "Near Space Operations":
        warnings.append("⚠ FLIGHT ENVELOPE CORNER: Low air density requires high angles of attack; stall risk.")
        
    if mach > 5.0:
        warnings.append("⚠ THERMAL PROTECTION: Entering extreme friction zone. Structural heat soaking active.")

    
    if len(warnings) >= 2 or fuel_status == "Critical":
        rec = "Immediate Landing Recommended"
        safety = "🔴 HIGH RISK"
        ready = "NO"
        success = "0% - 25% (Abysmal)"
        advisory = "vector straight to nearest clear runway threshold immediately."
    elif len(warnings) == 1 or fuel_status == "Low":
        rec = "Proceed With Caution"
        safety = "🟡 MODERATE RISK"
        ready = "YES"
        success = "50% - 75% (Conditional)"
        advisory = "Maintain present heading but minimize excessive maneuvering or throttles."
    else:
        rec = "Proceed"
        safety = "🟢 LOW RISK"
        ready = "YES"
        success = "95% - 100% (Optimal)"
        advisory = "Flight path profile matches predicted nominal trajectory matrix."

   
    print(f"Analyzing Target: {aircraft_data['name']} ({aircraft_data['log_num']})")
    print(f"Current Classifications: {regime} | {alt_zone} Flight | Fuel: {fuel_status}")
    print()
    print("Flight Computer Alerts Log:")
    if warnings:
        for alert in warnings:
            print(alert)
    else:
        print("✅ No immediate flight envelope structural anomalies detected.")
    
    print()
    print("----------------------------------")
    print("         MISSION SUMMARY          ")
    print("----------------------------------")
    print(f"Aircraft Ready          : {ready}")
    print(f"Overall Safety Margin   : {safety}")
    print(f"Mission Recommendation  : {rec}")
    print(f"Estimated Success Rate  : {success}")
    print(f"Pilot Advisory Notice   : Flight Command advises pilot to {advisory}")
    print("----------------------------------")


def main():
    """Main application runtime control loop using explicit states"""
    while True:
        print("\n==================================")
        print("      AIRPORT OPERATIONS CONSOLE  ")
        print("==================================")
        print("1. Register Aircraft Profile")
        print("2. Display Aircraft Registry")
        print("3. Analyze Flight Status Matrix")
        print("4. Safe Exit Program")
        print()
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            register_aircraft()
        elif choice == "2":
            display_aircraft()
        elif choice == "3":
            analyze_flight()
        elif choice == "4":
            print("\nClosing Airport Operations Console...")
            print("Ground support systems deactivated safely. Goodbye.")
            break
        else:
            print("\n❌ Invalid choice selection. Input integer value matching 1 through 4.")


if __name__ == "__main__":
    main()