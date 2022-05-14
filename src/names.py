"""name module"""


class Name:
    """Names class"""

    def __init__(self) -> None:
        """Name objects consist of first name, last name and an alias."""
        self._first_name: str = None
        self._last_name: str = None
        self._alias: str = None

    @property
    def first_name(self) -> str:
        """returns first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        sets first name if given argument is a string and not longer than
        the set maxlength.

        """
        MAX_FIRSTNAME_LENGTH = 10
        if str.__instancecheck__(value) and len(value) < MAX_FIRSTNAME_LENGTH:
            self._first_name = value

    @property
    def last_name(self) -> str:
        """Returns last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        sets lastname if the given argument is a string 
        and not longer than the set maximum_length.
        """
        MAX_FIRSTNAME_LENGTH = 15
        if str.__instancecheck__(value) and value < MAX_FIRSTNAME_LENGTH:
            self._last_name = value

    @property
    def alias(self) -> str:
        return self._alias

    @alias.setter
    def alias(self) -> None:
        self._alias = self._first_name[:1].lower(
        ) + self._last_name[:3].lower()
