import re

def to_snake_case(value: str):
    """ Converts a given value to snake case.
    
    Arguments:
    value: Value to be converted.
    """
    return re.sub(r"\s+", '_', value.lower())