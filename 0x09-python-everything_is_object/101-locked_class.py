#!/usr/bin/python3

"""
LockedClass: A class that enforces strict attribute control.

(... rest of the file-level docstring ...)
"""


class LockedClass:
    """
    Provides a restricted attribute model with only "first_name" allowed.
    """

    __slots__ = ("first_name",)  # Tuple defining permitted attributes

    def __setattr__(self, name, value):
        """
        Controls attribute setting behavior.

        Args:
            name (str): Name of the attribute to set.
            value: Value to assign to the attribute.

        Raises:
            AttributeError: If the attribute name is not "first_name".
        """

        if name == "first_name":
            super().__setattr__(name, value)  # Allow setting "first_name"
        else:
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'"
            )
