import math
def area(side_length, height):
    """
    Function to calculate the surface area of a pentagonal prism given the side length of the base and the height.
    
    Parameters:
    side_length (float or int): Length of the side of the pentagon.
    height (float or int): Height of the pentagonal prism.
    
    Returns:
    float: Surface area of the pentagonal prism.
    """
    # Area of the pentagonal base
    base_area = 5/2 * side_length**2 * (1 / math.tan(math.pi / 5))
    
    # Perimeter of the pentagonal base
    perimeter = 5 * side_length
    
    # Area of each rectangular face
    face_area = perimeter * height
    
    # Total surface area
    surface_area = 2 * base_area + 5 * face_area
    return surface_area

# Example usage:


# side_length = float(input("Enter the side length of the pentagon: "))
# height = float(input("Enter the height of the pentagonal prism: "))
# surface_area = area(side_length, height)
# print("Surface area of the pentagonal prism:", surface_area)
