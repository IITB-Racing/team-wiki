"""
Lumache - Python library for cooks and food lovers.

This is a Python docstring, we can use Markdown syntax here because
our API documentation library understands it (mkdocstrings).

    # Import lumache
    import lumache

    # Call its only function
    get_random_ingredients(kind=["cheeses"])

"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass