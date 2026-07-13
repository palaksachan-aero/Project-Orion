# Week-01/Day-03/flight_envelope_analyzer.py


def main():
    print("=== Flight Envelope Analyzer v2.0 ===")
    print()

    aircraft_name = input("Aircraft Name: ").strip()
    if not aircraft_name:
        aircraft_name = "Unknown Test Platform"

    try:
        mach = float(input("Mach Number: "))
        altitude = float(input("Altitude (meters): "))
        temperature = float(input("Outside Air Temperature (°C): "))
    except ValueError:
        print()
        print("❌ CRITICAL ERROR: Flight parameters must be valid numerical values.")
        return

    
    if mach < 0 or mach > 25:  
        print("❌ CRITICAL ERROR: Impossible Mach number detected (Must be 0 to 25).")
        return
    if altitude < 0 or altitude > 50000:  
        print("❌ CRITICAL ERROR: Invalid altitude. Target outside operational atmosphere boundaries.")
        return
    if temperature < -273.15 or temperature > 1000:  
        print("❌ CRITICAL ERROR: Temperature input violates thermodynamic laws.")
        return

    
    if mach < 0.8:
        regime = "Subsonic"
    elif 0.8 <= mach <= 1.2:
        regime = "Transonic"
    elif 1.2 < mach <= 5.0:
        regime = "Supersonic"
    else:
        regime = "Hypersonic"

   
    if altitude <= 3000:
        alt_zone = "Low Altitude Flight"
    elif 3001 <= altitude <= 9000:
        alt_zone = "Medium Altitude Flight"
    elif 9001 <= altitude <= 15000:
        alt_zone = "High Altitude Flight"
    else:
        alt_zone = "Near Space Operations" 

   
    if temperature > 35:
        temp_cond = "Hot Atmosphere"
    elif 15 <= temperature <= 35:
        temp_cond = "Normal Atmosphere"
    elif 0 <= temperature < 15:
        temp_cond = "Cool Atmosphere"
    else:
        temp_cond = "Cold Atmosphere"

    
    warnings = []
    risk_level = "🟢 LOW"
    status = "Flight Parameters Accepted ✅"

   
    if (regime == "Supersonic" or regime == "Hypersonic") and altitude <= 3000:
        warnings.append("⚠️ HAZARD: High dynamic pressure! Structural load limits threatened at low altitude.")
        risk_level = "🔴 HIGH"
        status = "Flight Parameters Restrained ❌"

    
    elif temperature > 35 and alt_zone == "High Altitude Flight":
        warnings.append("⚠️ WARNING: Elevated air temperatures at altitude may severely reduce engine thrust density.")
        risk_level = "🟡 MODERATE"

    
    elif regime == "Subsonic" and alt_zone == "Near Space Operations":
        warnings.append("⚠️ WARNING: Approaching low-density limits. Stall speed converges with maximum Mach limit.")
        risk_level = "🟡 MODERATE"
        
    
    elif regime == "Hypersonic" and alt_zone == "Near Space Operations":
        warnings.append("⚡ NOTICE: Extreme thermal friction expected. Ensure thermal protection systems are active.")
        risk_level = "🟡 MODERATE"

    
    print()
    print("===================================\n"
          "       Flight Envelope Report      \n"
          "===================================")
    print(f"Aircraft    : {aircraft_name}")
    print(f"Mach Number : {mach:.2f}")
    print(f"Altitude    : {altitude:.0f} m")
    print(f"Temperature : {temperature:.1f} °C")
    print()
    print("Flight Regime:")
    print(regime)
    print()
    print("Altitude Zone:")
    print(alt_zone)
    print()
    print("Temperature Condition:")
    print(temp_cond)
    print()
    print("Risk Assessment:")
    print(risk_level)
    print()
    print("Overall Status:")
    print(status)
    print("-----------------------------------")

    if warnings:
        print("FLIGHT COMPUTER ALERTS:")
        for warning in warnings:
            print(warning)
        print("-----------------------------------")


if __name__ == "__main__":
    main()