def area(length, width, height):
    """
    Function to calculate the surface area of a rectangular prism given its length, width, and height.
    
    Parameters:
    length (float or int): Length of the rectangular prism.
    width (float or int): Width of the rectangular prism.
    height (float or int): Height of the rectangular prism.
    
    Returns:
    float: Surface area of the rectangular prism.
    """
    # Calculate the surface area
    area = 2 * (length * width + length * height + width * height)
    return area

# Example usage:
# length = float(input("Enter the length of the rectangular prism: "))
# width = float(input("Enter the width of the rectangular prism: "))
# height = float(input("Enter the height of the rectangular prism: "))
# surface_area =area(length, width, height)
# print("Surface area of the rectangular prism:", surface_area)
