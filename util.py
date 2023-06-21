"""
Util function(s) live here.
"""


def format_repr(class_name, **kwargs):
    """
    Generate formatted class repr

    Args:
        class_name: Name of the class utilizing this repr.
        **kwargs: keyword arguments to represent.
    """

    processed_args = "".join(
        [f"'{kwarg[0]}': {kwarg[1]}, " for kwarg in kwargs.items()]
    ).strip()

    return f"{{'class': {class_name}, {processed_args}}}"
