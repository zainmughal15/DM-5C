def swap_variables(a, b):
    """
    Swaps the values of two variables using tuple unpacking.
    This method is concise and leverages Python's internal mechanics.
    """
    print(f"Before swap -> a: {a}, b: {b}")
    
    a, b = b, a  # Swap using tuple unpacking

    print(f"After swap  -> a: {a}, b: {b}")
    return a, b

# Example usage:
x = 10
y = 5
x, y = swap_variables(x, y)