import pygame
from spot import Spot, colors
from algorithms import a_star, bfs, dfs, dijkstra
import time
from typing import List


def make_grid(
    rows: int,
    width: int,
) -> List[List[Spot]]:
    """
    Create a grid of 'Spot' objects.

    Parameters:
    - rows (int): The number of rows in the grid.
    - width (int): The width of the grid in pixels.

    Returns:
    - List[List[Spot]]: A 2D list representing the grid with 'Spot' objects.
    """
    grid: List[List[Spot]] = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(
    win: pygame.Surface,
    rows: int,
    width: int,
) -> None:
    """
    Draw grid lines on the window.

    Parameters:
    - win (pygame.Surface): The pygame window surface to draw on.
    - rows (int): The number of rows in the grid.
    - width (int): The width of the grid in pixels.

    Returns:
    - None: This function does not return a value but draws lines on the
    window.
    """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, colors["grey"], (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, colors["grey"], (j * gap, 0), (j * gap,
                                                                 width))


def draw(
    win: pygame.Surface,
    grid: list,
    rows: int,
    width: int,
) -> None:
    """
    Draw the entire grid and its spots on the window.

    Parameters:
    - win (pygame.Surface): The pygame window surface to draw on.
    - grid (list): A 2D list of 'Spot' objects representing the grid.
    - rows (int): The number of rows in the grid.
    - width (int): The width of the grid in pixels.

    Returns:
    - None: This function does not return a value but updates the window
    display.
    """
    win.fill(colors["white"])

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(
    pos: tuple,
    rows: int,
    width: int,
) -> tuple:
    """
    Get the row and column in the grid corresponding to a mouse click position.

    Parameters:
    - pos (tuple): The x and y pixel coordinates of the mouse click.
    - rows (int): The number of rows in the grid.
    - width (int): The width of the grid in pixels.

    Returns:
    - tuple: The row and column in the grid corresponding to the mouse click.
    """
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def draw_stats(
    win: pygame.Surface,
    nodes_traversed: int,
    time_taken: float
) -> None:
    """
    Draw statistics like nodes traversed and time taken on the window.

    Parameters:
    - win (pygame.Surface): The pygame window surface to draw on.
    - nodes_traversed (int): The number of nodes traversed during pathfinding.
    - time_taken (float): The time taken for the pathfinding in seconds.

    Returns:
    - None: This function does not return a value but updates the window
    display.
    """
    font = pygame.font.SysFont("Arial", 20)
    # Create text surfaces for the statistics
    nodes_text = font.render(
        f"Nodes traversed: {nodes_traversed}", True, colors["black"]
    )
    time_text = font.render(
        f"Time taken: {time_taken:.2f} seconds", True, colors["black"]
    )

    # Display the text surfaces on the screen
    win.blit(nodes_text, (10, 10))
    win.blit(time_text, (10, 30))


def count_nodes_traversed(
    grid: List[List[Spot]]
) -> int:
    """
    Count the number of nodes that were traversed during pathfinding.

    Parameters:
    - grid (List[List[Spot]]): A 2D list of 'Spot' objects representing the
    grid.

    Returns:
    - int: The number of nodes that were traversed.
    """
    count = 0
    for row in grid:
        for spot in row:
            if spot.is_closed() or spot.is_open():
                count += 1
    return count


def display_results(
    start_time: float,
    grid,
    win
) -> None:
    """
    Display the results of the pathfinding algorithm, including time taken and
    nodes traversed.

    Parameters:
    - start_time (float): The starting time of the pathfinding algorithm.
    - grid: A 2D list of 'Spot' objects representing the grid.
    - win (pygame.Surface): The pygame window surface to display the results
    on.

    Returns:
    - None: This function does not return a value but displays results on the
    window.
    """
    global run, exit
    end_time: float = time.time()
    time_taken: float = end_time - start_time
    node_traversed = count_nodes_traversed(grid)
    draw_stats(win, node_traversed, time_taken)
    pygame.display.update()
    exit = False
    while not exit:
        for event2 in pygame.event.get():
            if event2.type == pygame.KEYDOWN:
                exit = True
            if event2.type == pygame.QUIT:
                pygame.quit()

def display_no_path_message(
    win,
    message: str
) -> None:
    """
    Display a message on the window and wait for a key press to continue.

    This function creates a white rectangular block that matches the size of the
    message text, and overlays the text over this block. The display lasts until
    the user provides a keyboard input.

    Parameters:
    - win (pygame.Surface): The pygame window surface to display the message on.
    - message (str): The message to be displayed.

    Returns:
    - None: This function does not return a value but displays a message on the
    window.
    """
    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render(message, True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(win.get_width()/2, win.get_height()/2))  # Get the rectangle for positioning

    # Create a new surface with the same size as the text
    background = pygame.Surface(text.get_size())
    # Fill the new surface with white color
    background.fill((255, 255, 255))

    # Draw the white background on the window
    win.blit(background, text_rect)
    # Draw the text on the window
    win.blit(text, text_rect)

    pygame.display.flip()  

    # Wait for a key press
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

            if event.type == pygame.QUIT:
                pygame.quit()

def start_game(
    grid: list,
    rows: int,
    width: int,
    win: pygame.Surface,
    algorithm: str,
) -> None:
    """
    Start the pathfinding game loop, allowing the user to set up the grid and
    run different algorithms.

    Parameters:
    - grid (list): A 2D list of 'Spot' objects representing the grid.
    - rows (int): The number of rows in the grid.
    - width (int): The width of the grid in pixels.
    - win (pygame.Surface): The pygame window surface for the game.
    - algorithm (str): The name of the pathfinding algorithm to use ('a_star',
    'dfs', 'bfs', 'dijkstra').

    Returns:
    - None: This function does not return a value but initiates and manages
    the game loop, handling user interactions and visualizations.

    Note:
    - The function includes interactions for setting start and end points,
    creating barriers, and triggering the selected pathfinding algorithm.
    - The game loop continues until the user quits the application.
    """
    start = None
    end = None

    run = True
    # started = False
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if started:
            #     continue

            if pygame.mouse.get_pressed()[0]:  # left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    start_time: float = time.time()
                    if algorithm == "a_star":
                        if a_star(
                            lambda: draw(win, grid, rows, width),
                            grid,
                            start,
                            end,
                        ):
                            display_results(start_time, grid, win)
                        else:
                            display_no_path_message(win, "No path found!")
                    elif algorithm == "dfs":
                        if dfs(
                            lambda: draw(win, grid, rows, width),
                            grid,
                            start,
                            end,
                        ):
                            display_results(start_time, grid, win)
                        else:
                            display_no_path_message(win, "No path found!")
                    elif algorithm == "bfs":
                        if bfs(
                            lambda: draw(win, grid, rows, width),
                            grid,
                            start,
                            end,
                        ):
                            display_results(start_time, grid, win)
                        else:
                            display_no_path_message(win, "No path found!")
                    elif algorithm == "dijkstra":
                        if dijkstra(
                            lambda: draw(win, grid, rows, width),
                            grid,
                            start,
                            end,
                        ):
                            display_results(start_time, grid, win)
                        else:
                            display_no_path_message(win, "No path found!")
                       
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)

    pygame.quit()
