import math

def area(outer_radius, inner_radius):
    """
    Function to calculate the area of a ring (annulus) given the outer radius and inner radius.
    
    Parameters:
    outer_radius (float or int): Outer radius of the ring.
    inner_radius (float or int): Inner radius of the ring.
    
    Returns:
    float: Area of the ring.
    """
    outer_area = math.pi * outer_radius ** 2
    inner_area = math.pi * inner_radius ** 2
    return outer_area - inner_area

# Example usage:
# outer_radius = float(input("Enter the outer radius of the ring: "))
# inner_radius = float(input("Enter the inner radius of the ring: "))
# area = area(outer_radius, inner_radius)
# print("Area of the ring:", area)
