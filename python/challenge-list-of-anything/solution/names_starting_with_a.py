def names_starting_with_a(names: list) -> list:
    """Given a list of names, this function returns a new list containing only the names that start with the letter "A".
    
    Args:
        names(list): A list of strings, e.g. ["Alice", "Bob", "Charlie", "David", "Eva"]

    Returns: 
        result(list): A list of names that start with the letter "A", e.g. ["Alice"]
    """
    result = [name for name in names if name.startswith("A")]
    
    return result
