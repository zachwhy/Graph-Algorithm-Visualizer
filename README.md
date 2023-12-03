# Graph Algorithm Visualizer

This project is a Graph Algorithm Visualizer built with Python.

## Installation

To install and run this project, you will need to have Conda and Poetry installed on your system.

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a new Conda environment using Python 3.11:

   ```bash
   conda create --name graph_algo_viz python=3.11
   ```

4. Activate the new environment:

   ```bash
   conda activate graph_algo_viz
   ```

5. Install Poetry:

   ```bash
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

6. Install the project dependencies using Poetry:

   ```bash
   poetry install
   ```

# Usage

To use this project, you can run the `main.py` file with the following command-line arguments:

```bash
main.py [-h] [-rows ROWS] [-width WIDTH] [-algo {dijkstra,a_star, bfs, dfs}]
```

The following arguments are available:

- `-rows`: Number of rows in the grid (default: 800).
- `-width`: Width of each cell in the grid (default: 800).
- `-algo`: Algorithm to use for pathfinding. Valid options are `dijkstra` (default) and `a_star`.

To run the project with custom arguments, you can use the following command:

```bash
python main.py -rows 1000 -width 600 -algo a_star
```

## Controls

The controls for the pygame are as follows:

- **Start/Restart the Algorithm**: Press the `Spacebar` key to begin the graph traversal. Once the traversal is completed, you can press the `Spacebar` key again to restart the path finding.
- **Clear the Board**: Press the `C` key to clear the board.

Please ensure that the pygame window is active (clicked on or selected) when using these controls.


# Description of Algorithms

We implemented a variety of algorithms to compare their efficiency:

- `Breadth-first search`, implemented using deque
- `Depth-first search`, implemented using stack
- `Dijkstra`, implemented using priority queue
- `A-star`, implemented using priority queue

In carrying out these algorithms, we found that the Dijkstra and A-star algorithms were quite similar, with the only difference being A-star calculated distance to target heuristically whereas Dijkstra only considered absolute distance to the target. Dijkstra and A-star are also optimised versions of BFS. Unsurprisingly, they generally perform better than BFS.

# Unit Tests

To ensure the robustness and accuracy of our pathfinding algorithms, we have developed a series of unit tests. Each test is designed to validate different aspects of the pathfinding process under various scenarios.

## Test Cases

### No Path Scenario

This test verifies that when all nodes are isolated (no neighbours), the algorithms correctly determine that there is no available path.

### Specific Path Scenario

We will test a predetermined grid layout with two possible paths to see if the algorithm can find a path from the start to end node.

### Empty Grid Scenario

This test gives an empty grid scenario is used to test the algorithms' ability to handle cases with no nodes. The expected behavior is for the algorithm to return False, indicating no path is found.

### Start and End as Neighbours

This test checks the algorithms' behavior when the start and end nodes are direct neighbors. The expected outcome is a True result, as the path is immediately available.

### Start and End are Not Neighbours

This test ensures that if the start and end nodes are not neighbors and no other nodes are present, the algorithms correctly return False, indicating no path exists.

## Running the Tests

To execute the tests, navigate to the project's root directory and run:

```bash
pytest tests/test_algorithms.py
```
