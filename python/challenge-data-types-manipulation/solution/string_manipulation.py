def string_manipulation(input_string: str) -> str:
    """
    Args:
    input_string: a string to be manipulated
    
    Returns:
    The final manipulated string.
    """
    input_string = input_string.lower().replace(" ", "")
    return input_string[::-1]
