import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius**2)

print("\n--- Results ---")
print(f"Diameter:      {diameter:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area:          {area:.2f}")