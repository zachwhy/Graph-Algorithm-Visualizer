from src.graph_algo_viz.algorithms import a_star, bfs, dfs, dijkstra
from .conftest import MockSpot


def mock_draw():
    pass


def test_no_path_found(grid):
    """
    Sets 'neighbors' list to an empty list, effectively removing all
    connections between nodes (i.e. only barriers [])
    """
    grid, start, end = grid

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].update_neighbors([])

    for algorithm in (bfs, dfs, dijkstra, a_star):
        result = algorithm(mock_draw, grid, start, end)
        assert not result, f"{algorithm.__name__} found a path."


def test_specific_path(grid):
    """
    Sets up a specific configuration for the grid to test if the pathfinding
    algorithms can find a path from the start to end node

    Grid layout:
    (0,0) - (0,1) - (0,2)
    |       |
    (1,0)   (1,1) - (1,2)
            |       |
    (2,0)   (2,1) - (2,2)

    2 possible paths:
    (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2)
    (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)
    """
    grid, start, end = grid

    start.update_neighbors([grid[0][1]])
    grid[0][1].update_neighbors([grid[1][1]])
    grid[1][1].update_neighbors([grid[2][1], grid[1][2]])
    grid[2][1].update_neighbors([end])
    grid[1][2].update_neighbors([end])

    for algorithm in (bfs, dfs, dijkstra, a_star):
        result = algorithm(mock_draw, grid, start, end)
        assert result, f"{algorithm.__name__} failed to find the path."


def test_empty_grid(grid):
    """
    Tests that the pathfinding algorithms return False for an empty grid
    """
    _, start, end = grid

    empty_grid = []
    for algorithm in (bfs, dfs, dijkstra, a_star):
        result = algorithm(mock_draw, empty_grid, start, end)
        error_message = f"{algorithm.__name__} found a path in an empty grid."
        assert not result, error_message


def ensure_start_and_end_are_neighbors(start, end):
    """
    Helper function to ensure start and end are neighbors
    (Not a test case itself)
    """
    start.add_neighbor(end)
    assert end in start.neighbors


def test_start_end_neighbour(grid):
    """
    Tests that the pathfinding algorithms return True when
    only start and end points are present and are neighbors
    """
    _, start, end = grid

    start = MockSpot(start.row, start.col)
    end = MockSpot(end.row, end.col)
    ensure_start_and_end_are_neighbors(start, end)
    start_end_grid = [[start], [end]]

    for algorithm in (bfs, dfs, dijkstra, a_star):
        result = algorithm(mock_draw, start_end_grid, start, end)
        error_message = (
            f"{algorithm.__name__} failed to find the path "
            "when only start and end are neighbors."
        )
        assert result, error_message


def ensure_start_and_end_are_not_neighbors(start, end):
    """
    Helper function to ensure start and end are not neighbors
    (Not a test case itself)
    """
    start.neighbors = [
        neighbor for neighbor in start.neighbors if neighbor != end
    ]
    assert end not in start.neighbors


def test_start_end_not_neighbours(grid):
    """
    Tests that the pathfinding algorithms return False when
    only start and end points are present and are not neighbors
    """
    _, start, end = grid
    start = MockSpot(start.row, start.col)
    end = MockSpot(end.row, end.col)
    ensure_start_and_end_are_not_neighbors(start, end)
    start_end_grid = [[start], [end]]

    for algorithm in (bfs, dfs, dijkstra, a_star):
        result = algorithm(mock_draw, start_end_grid, start, end)
        error_message = (
            f"{algorithm.__name__} incorrectly found a path "
            "when start and end are not neighbors."
        )
        assert not result, error_message
