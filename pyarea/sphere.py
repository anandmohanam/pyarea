import math

def area(radius):
    """
    Function to calculate the surface area of a sphere given its radius.
    
    Parameters:
    radius (float or int): Radius of the sphere.
    
    Returns:
    float: Surface area of the sphere.
    """
    return 4 * math.pi * radius ** 2

# Example usage:
# radius = float(input("Enter the radius of the sphere: "))
# surface_area = area(radius)
# print("Surface area of the sphere:", surface_area)
