import argparse
import pygame
from game import make_grid, start_game


def arg_parse():
    """
    Parse command-line arguments for the Graph Algorithm Visualizer.

    This function sets up command-line argument parsing and defines the
    expected arguments.

    Arguments:
    - '-rows' (int): Number of rows in the grid (default: 50).
    - '-width' (int): Width of each cell in the grid in pixels (default: 800).
    - '-algo' or '--algorithm' (str): Algorithm to use for pathfinding.
    Choices are 'dijkstra', 'a_star', 'bfs', 'dfs' (default: 'dijkstra').

    Returns:
    - argparse.Namespace: An object containing the parsed command-line
    arguments.
    """
    parser = argparse.ArgumentParser(description="Graph Algorithm Visualizer")
    parser.add_argument(
        "-rows",
        type=int,
        default=50,
        help="Number of rows in the grid",
    )
    parser.add_argument(
        "-width",
        type=int,
        default=800,
        help="Width of each cell in the grid",
    )
    parser.add_argument(
        "-algo",
        "--algorithm",
        choices=["dijkstra", "a_star", "bfs", "dfs"],
        type=str,
        default="dijkstra",
        help="Algorithm to use for pathfinding",
    )

    return parser.parse_args()


if __name__ == "__main__":
    """
    Main execution block to initialize and run the Graph Algorithm Visualizer.

    Initializes the Pygame window and starts the game with the provided
    command-line arguments.
    - Initializes Pygame.
    - Parses command-line arguments for grid configuration and pathfinding
    algorithm.
    - Sets up the Pygame window and font.
    - Creates the grid.
    - Starts the game loop with the specified pathfinding algorithm.
    """
    pygame.init()
    args = arg_parse()
    font = pygame.font.SysFont("Arial", 20)

    win = pygame.display.set_mode((args.width, args.width))
    pygame.display.set_caption("Graph Algorithm Visualizer")

    grid = make_grid(args.rows, args.width)

    start_game(grid, args.rows, args.width, win, args.algorithm)
