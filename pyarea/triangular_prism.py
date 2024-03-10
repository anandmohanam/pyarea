def area(base_length, height, prism_height):
    """
    Function to calculate the surface area of a triangular prism given the base length, height, and prism height.
    
    Parameters:
    base_length (float or int): Length of the base of the triangle.
    height (float or int): Height of the triangle.
    prism_height (float or int): Height of the triangular prism.
    
    Returns:
    float: Surface area of the triangular prism.
    """
    # Area of the triangular base
    base_area = 0.5 * base_length * height
    
    # Perimeter of the triangular base
    perimeter = 3 * base_length
    
    # Area of each rectangular face
    face_area = perimeter * prism_height
    
    # Total surface area
    surface_area = 2 * base_area + 3 * face_area
    return surface_area

# Example usage:
# base_length = float(input("Enter the base length of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# prism_height = float(input("Enter the height of the triangular prism: "))
# surface_area = area(base_length, height, prism_height)
# print("Surface area of the triangular prism:", surface_area)
