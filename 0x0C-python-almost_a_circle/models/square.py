from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
