import math

def area(radius, height):
    """
    Function to calculate the surface area of a cone given its radius and height.
    
    Parameters:
    radius (float or int): Radius of the base of the cone.
    height (float or int): Height of the cone.
    
    Returns:
    float: Surface area of the cone.
    """
    slant_height = math.sqrt(radius**2 + height**2)
    base_area = math.pi * radius**2
    lateral_area = math.pi * radius * slant_height
    return base_area + lateral_area

# Example usage:
# radius = float(input("Enter the radius of the base of the cone: "))
# height = float(input("Enter the height of the cone: "))
# surface_area =area(radius, height)
# print("Surface area of the cone:", surface_area)
