import pygame
from typing import List


colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 255, 255),
    "yellow": (255, 255, 0),
    "purple": (255, 0, 255),
    "orange": (255, 165, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "grey": (128, 128, 128),
    "turquoise": (64, 224, 208),
}


class Spot:
    """
    Initialize a Spot object representing a cell in the grid.

    Parameters:
    - row (int): The row index of the spot in the grid.
    - col (int): The column index of the spot in the grid.
    - width (int): The width of each cell in the grid.
    - total_rows (int): The total number of rows in the grid.

    Attributes:
    - x (int): The x-coordinate of the spot in the window.
    - y (int): The y-coordinate of the spot in the window.
    - color (pygame.Color): The color of the spot, indicating its state.
    - neighbors (List[Spot]): A list of neighboring spots.
    """
    def __init__(
        self,
        row: int,
        col: int,
        width: int,
        total_rows: int,
    ) -> None:
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = colors["white"]  # default color is white
        self.neighbors: List[Spot] = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """
        Get the position of the spot in the grid.

        Returns:
        - tuple: The (row, col) coordinates of the spot.
        """
        return self.row, self.col

    def is_closed(self):
        """
        Check if the spot is in a closed state.

        Returns:
        - bool: True if the spot is closed, False otherwise.
        """
        return self.color == colors["red"]

    def is_open(self):
        """
        Check if the spot is in an open state.

        Returns:
        - bool: True if the spot is open, False otherwise.
        """
        return self.color == colors["green"]

    def is_barrier(self):
        """
        Check if the spot is a barrier.

        Returns:
        - bool: True if the spot is a barrier, False otherwise.
        """
        return self.color == colors["black"]

    def is_start(self):
        """
        Check if the spot is the start spot.

        Returns:
        - bool: True if the spot is the start spot, False otherwise.
        """
        return self.color == colors["orange"]

    def is_end(self):
        """
        Check if the spot is the end spot.

        Returns:
        - bool: True if the spot is the end spot, False otherwise.
        """
        return self.color == colors["turquoise"]

    def reset(self):
        """
        Reset the spot to its default state.
        """
        self.color = colors["white"]

    def make_closed(self):
        """
        Mark the spot as closed.
        """
        self.color = colors["red"]

    def make_open(self):
        """
        Mark the spot as open.
        """
        self.color = colors["green"]

    def make_barrier(self):
        """
        Mark the spot as a barrier.
        """
        self.color = colors["black"]

    def make_start(self):
        """
        Mark the spot as the start spot.
        """
        self.color = colors["orange"]

    def make_end(self):
        """
        Mark the spot as the end spot.
        """
        self.color = colors["turquoise"]

    def make_path(self):
        """
        Mark the spot as part of the path.
        """
        self.color = colors["purple"]

    def draw(
        self,
        win: pygame.Surface,
    ):
        """
        Draw the spot on the window.

        Parameters:
        - win (pygame.Surface): The pygame window surface to draw on.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width,
                                           self.width))

    def update_neighbors(self, grid):
        """
        Update the neighbors of the spot based on the current grid state.

        Parameters:
        - grid: The grid containing all spots.
        """
        self.neighbors = []

        # DOWN
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].is_barrier()
        ):
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if (
            self.row > 0
            and not grid[self.row - 1][self.col].is_barrier()
        ):
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if (
            self.col < self.total_rows - 1
            and not grid[self.row][self.col + 1].is_barrier()
        ):
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if (
            self.col > 0
            and not grid[self.row][self.col - 1].is_barrier()
        ):
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        """
        Less than comparison for priority queue usage. Always returns False.

        Parameters:
        - other: Another object to compare against.

        Returns:
        - bool: False, as the comparison is not relevant for this
        implementation.
        """
        return False
