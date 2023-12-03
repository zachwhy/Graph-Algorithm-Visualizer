import pytest
import pygame

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


class MockSpot:
    """
    Initialize a MockSpot object representing a cell in a testing grid.

    Parameters:
    - row (int): The row index of the spot.
    - col (int): The column index of the spot.

    Attributes:
    - neighbors (list[MockSpot]): List of neighboring spots.
    """
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.neighbors = []

    def __repr__(self):
        """
        Representation of the MockSpot object.

        Returns:
        - str: A string representation of the spot's position.
        """
        return f"({self.row}, {self.col})"

    def __eq__(self, other: "MockSpot"):
        """
        Check equality between two MockSpot objects.

        Parameters:
        - other (MockSpot): Another MockSpot object to compare with.

        Returns:
        - bool: True if the spots have the same row and column, False
        otherwise.
        """
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """
        Generate a hash value for the MockSpot object.

        Returns:
        - int: The hash value of the spot.
        """
        return hash((self.row, self.col))

    def get_pos(self) -> tuple[int, int]:
        """
        Get the position of the spot.

        Returns:
        - tuple[int, int]: The (row, col) coordinates of the spot.
        """
        return self.row, self.col

    def add_neighbor(self, neighbor: "MockSpot"):
        """
        Add a neighbor to the spot.

        Parameters:
        - neighbor (MockSpot): A neighbor spot to add.
        """
        self.neighbors.append(neighbor)

    def are_neighbors(node1, node2):
        """
        Check if two spots are neighbors.

        Parameters:
        - node1: The first MockSpot.
        - node2: The second MockSpot.

        Returns:
        - bool: True if node2 is a neighbor of node1, False otherwise.
        """
        return node2 in node1.neighbors

    def update_neighbors(self, val):
        """
        Update the neighbors of the spot.

        Parameters:
        - val: The new list of neighbors.
        """
        self.neighbors = val

    def __lt__(self, other):
        """
        Less than comparison for MockSpot objects.

        Parameters:
        - other (MockSpot): Another MockSpot object to compare against.

        Returns:
        - bool: True if the current spot is less than the other, based on
        position.
        """
        return (self.row, self.col) < (other.row, other.col)

    # similar to Spot class
    def make_open(self):
        self.color = colors["green"]

    def make_closed(self):
        self.color = colors["red"]

    def make_path(self):
        self.color = colors["purple"]

    def make_end(self):
        self.color = colors["turquoise"]


@pytest.fixture(
    scope="session",
    autouse=True,
)
def initialise_pygame():
    """
    Pytest fixture to initialize Pygame.

    This fixture is automatically used in every test session.

    Returns:
    - None: Pygame is initialized for the testing session.
    """
    pygame.init()


@pytest.fixture(scope="class")
def grid():
    """
    Pytest fixture to create a 3x3 grid of MockSpot objects. This fixture sets
    up a grid with neighboring relationships between MockSpots.

    Returns:
    - tuple: A tuple containing the grid (list of lists of MockSpot), start
    MockSpot, and end MockSpot.
    """
    grid = [[MockSpot(i, j) for j in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            if j < 2:  # right neighbour
                grid[i][j].add_neighbor(grid[i][j + 1])
            if i < 2:  # bottom neighbor
                grid[i][j].add_neighbor(grid[i + 1][j])

    start: MockSpot = grid[0][0]
    end: MockSpot = grid[2][2]

    return grid, start, end
