#4. Calculate the volume of a sphere given its radius
import math
radius = float(input("Enter the radius of the sphere: "))  
def sphere_volume(radius):

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

volume = sphere_volume(radius)
print("The volume of the sphere is: ", volume)