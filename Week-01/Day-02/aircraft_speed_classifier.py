
mach_speed = float(input("Enter aircraft speed (Mach): "))

if mach_speed < 0:
    classification = "Invalid speed"
elif mach_speed < 0.8:
    classification = "Aircraft is flying at Subsonic Speed"
elif 0.8 <= mach_speed <= 1.2:
    classification = "Aircraft is flying at Transonic Speed"
elif 1.2 < mach_speed <= 5:
    classification = "Aircraft is flying at Supersonic Speed"
else:
    classification = "Aircraft is flying at Hypersonic Speed"

print(f"Classification: {classification}")