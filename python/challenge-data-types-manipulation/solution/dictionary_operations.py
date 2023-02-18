def dictionary_operations(input_dict: dict) -> dict:
    """
    Args:
    input_dict: a dictionary to be manipulated
    
    Returns:
    The final manipulated dictionary.
    """
    input_dict["new_key"] = "new_value"
    input_dict.pop("remove_key", None)
    return input_dict
