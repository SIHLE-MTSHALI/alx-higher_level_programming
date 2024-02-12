from .rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    
    Attributes:
        size (int): The size of the square's sides.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The square's identifier.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square.
        
        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The square's identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        
        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
