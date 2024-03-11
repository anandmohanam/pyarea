import math

def area(n, side_length):
    """
    Function to calculate the area of a regular polygon given the number of sides and the length of each side.
    
    Parameters:
    n (int): Number of sides of the regular polygon.
    side_length (float or int): Length of each side of the regular polygon.
    
    Returns:
    float: Area of the regular polygon.
    """
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

# Example usage:
# n = int(input("Enter the number of sides of the regular polygon: "))
# side_length = float(input("Enter the length of each side of the regular polygon: "))
# area =area(n, side_length)
# print("Area of the regular polygon:", area)
