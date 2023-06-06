import re

from code.utils.utils import to_snake_case


def test_to_snake_case():
    """ Test if string is being coverted to snake case """
    res = to_snake_case("String To Snake Case")
    snake_pattern = r"^[a-z][a-z0-9_&]*$"
    assert re.match(snake_pattern, res)