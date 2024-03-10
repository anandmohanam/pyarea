import math

def area(side_length, height):
    """
    Function to calculate the surface area of a hexagonal pyramid given the side length of the base and the height.
    
    Parameters:
    side_length (float or int): Length of the side of the hexagonal base.
    height (float or int): Height of the hexagonal pyramid (distance from the center of the base to the apex).
    
    Returns:
    float: Surface area of the hexagonal pyramid.
    """
    # Area of the hexagonal base
    base_area = 3 * math.sqrt(3) * side_length ** 2 / 2
    
    # Area of each triangular face
    face_area = 0.5 * 6 * side_length * height
    
    # Total surface area
    surface_area = base_area + 6 * face_area
    return surface_area

# Example usage:
# side_length = float(input("Enter the side length of the hexagonal base: "))
# height = float(input("Enter the height of the hexagonal pyramid: "))
# surface_area = area(side_length, height)
# print("Surface area of the hexagonal pyramid:", surface_area)
