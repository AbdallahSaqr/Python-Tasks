#5. Calculate the area of a trianlgle

base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")
# Check if the inputs are numeric
if base.isnumeric() and height.isnumeric():
    base = float(base)
    height = float(height)
else:
    print("Please enter valid numeric values for base and height.")
    exit()
# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return (base * height) / 2

area = area_of_triangle(base, height)
print("The area of the triangle is: ", area)