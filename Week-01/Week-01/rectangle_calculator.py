import math

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)
diagonal = math.sqrt (length**2 + width**2)

print("\n--- Results ---")
print(f"Area:      {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
print(f"Diagonal:          {diagonal:.2f}")