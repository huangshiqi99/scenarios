def list_operations(input_list: list) -> list:
    """
    Args:
    input_list: a list of integers to be manipulated
    
    Returns:
    The final manipulated list.
    """
    input_list = list(set(input_list))
    input_list.sort()
    return input_list
