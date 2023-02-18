def tuple_operations(input_tuple: tuple) -> tuple:
    """
    
    Args:
    input_tuple: a tuple to be manipulated
    
    Returns:
    The final manipulated tuple.
    """
    input_list = list(input_tuple)
    input_list.sort()
    return tuple(input_list)
