from queue import PriorityQueue
from game import Spot
import pygame
from collections import deque


def h(
    p1: tuple,
    p2: tuple,
) -> int:
    """
    Calculate the Manhattan distance between two points.

    Parameters:
    - p1 (tuple): A tuple representing the coordinates (x, y) of the first
    point.
    - p2 (tuple): A tuple representing the coordinates (x, y) of the second
    point.

    Returns:
    - int: The Manhattan distance between the two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(
    came_from: dict,
    current: Spot,
    draw: callable,
):
    """
    Reconstruct the path from the start node to the end node.

    Parameters:
    - came_from (dict): A dictionary mapping each node to the node it came
    from.
    - current (Spot): The current spot (end node) to start reconstructing from.
    - draw (callable): A function that updates the visual representation of
    the path.

    Returns:
    - None: This function does not return a value but updates the path
    visually.
    """
    ...
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(
    draw: callable,
    grid: list,
    start: Spot,
    end: Spot,
) -> bool:
    """
    Perform the A* search algorithm to find the shortest path between two
    points.

    Parameters:
    - draw (callable): Function to draw or update the grid state.
    - grid (list): A 2D list representing the grid or graph.
    - start (Spot): The starting node in the grid.
    - end (Spot): The end or target node in the grid.

    Returns:
    - bool: True if a path is found, False otherwise.
    """
    if not grid:  # handle empty grid
        return False
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(
                    neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()
    
    return False


def bfs(
    draw: callable,
    grid: list,
    start: Spot,
    end: Spot,
) -> bool:
    """
    Perform the Breadth-First Search (BFS) algorithm to find the shortest path.

    Parameters:
    - draw (callable): Function to draw or update the grid state.
    - grid (list): A 2D list representing the grid or graph.
    - start (Spot): The starting node in the grid.
    - end (Spot): The end or target node in the grid.

    Returns:
    - bool: True if a path is found, False otherwise.
    """
    if not grid:  # handle empty grid
        return False
    queue = deque([start])
    came_from = {}
    visited = {spot: False for row in grid for spot in row}
    visited[start] = True

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if not visited[neighbor]:
                came_from[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dfs(
    draw: callable,
    grid: list,
    start: Spot,
    end: Spot,
) -> bool:
    """
    Perform the Depth-First Search (DFS) algorithm to find a path.

    Parameters:
    - draw (callable): Function to draw or update the grid state.
    - grid (list): A 2D list representing the grid or graph.
    - start (Spot): The starting node in the grid.
    - end (Spot): The end or target node in the grid.

    Returns:
    - bool: True if a path is found, False otherwise.
    """
    if not grid:  # handle empty grid
        return False
    stack = [start]
    came_from = {}
    visited = {spot: False for row in grid for spot in row}
    visited[start] = True

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if not visited[neighbor]:
                came_from[neighbor] = current
                visited[neighbor] = True
                stack.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dijkstra(
        draw: callable,
        grid: list,
        start: Spot,
        end: Spot
) -> bool:
    """
    Perform Dijkstra's algorithm to find the shortest path in a grid.

    Parameters:
    - draw (callable): Function to draw or update the grid state.
    - grid (list): A 2D list representing the grid or graph.
    - start (Spot): The starting node in the grid.
    - end (Spot): The end or target node in the grid.

    Returns:
    - bool: True if the shortest path is found, False otherwise.
    """
    if not grid:  # handle empty grid
        return False
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    distance = {spot: float("inf") for row in grid for spot in row}
    distance[start] = 0
    # unexplored = set(spot for row in grid for spot in row)

    open_set_hash = {start}

    # current = start

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[1]
        open_set_hash.remove(current)
        # open_set = PriorityQueue()
        # open_set.put((distance[current], current))
        # open_set_hash = {current}

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_distance = distance[current] + 1

            if temp_distance < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = temp_distance
                if neighbor not in open_set_hash:
                    open_set.put((distance[neighbor], neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
