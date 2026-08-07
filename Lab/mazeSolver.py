"""
==========================================================
        MAZE SOLVER USING BFS (BEGINNER FRIENDLY)
==========================================================

This program allows the user to enter a maze (up to 10x10)
and finds the shortest path from Start (S) to Goal (G)
using Breadth-First Search (BFS).

Maze Symbols:
S = Start
G = Goal
. = Empty path
| = Wall
* = Shortest path (output)

==========================================================
PART 1 - Maze Input & Validation        (Person 1)
PART 2 - BFS Search Algorithm           (Person 2)
PART 3 - Output & Statistics            (Person 3)
==========================================================
"""

from collections import deque

# ==========================================================
# PART 1 - MAZE INPUT & VALIDATION
# ==========================================================

def get_maze_from_user():
    """Gets the maze from the user."""
    rows = int(input("Enter number of rows (1-10): "))
    cols = int(input("Enter number of columns (1-10): "))
    if rows < 1 or rows > 10 or cols < 1 or cols > 10:
        print("Maze size must be between 1 and 10.")
        exit()
    print("\nEnter the maze row by row.")
    print("S = Start")
    print("G = Goal")
    print(". = Empty Path")
    print("| = Wall\n")

    maze = []
    for i in range(rows):
        row = input(f"Row {i+1}: ")
        if len(row) != cols:
            print(f"Row {i+1} must contain exactly {cols} characters.")
            exit()
        maze.append(row)
    validate_maze(maze)
    start, goal = find_start_and_goal(maze)
    return maze, start, goal


def validate_maze(maze):
    """Checks if the maze is valid."""

    valid_symbols = {"S", "G", ".", "|"}

    start_count = 0
    goal_count = 0

    for row in maze:
        for cell in row:
            if cell not in valid_symbols:
                print("Invalid character found:", cell)
                exit()
            if cell == "S":
                start_count += 1
            elif cell == "G":
                goal_count += 1
    if start_count != 1:
        print("Maze must contain exactly one Start (S).")
        exit()
    if goal_count != 1:
        print("Maze must contain exactly one Goal (G).")
        exit()


def find_start_and_goal(maze):
    """Finds the Start and Goal positions."""
    start = None
    goal = None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "S":
                start = (row, col)
            elif maze[row][col] == "G":
                goal = (row, col)
    return start, goal


# ==========================================================
# PART 2 - BFS SEARCH
# ==========================================================

def get_walkable_neighbors(maze, cell):
    """Returns all valid neighboring cells."""
    rows = len(maze)
    cols = len(maze[0])
    row, col = cell
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    neighbors = []
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if maze[new_row][new_col] != "|":
                neighbors.append((new_row, new_col))
    return neighbors


def find_shortest_path_bfs(maze, start, goal):
    """Uses BFS to find the shortest path."""
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    came_from = {}
    explored_cells = 0
    while queue:
        current = queue.popleft()
        explored_cells += 1
        if current == goal:
            path = build_path(came_from, start, goal)
            return path, explored_cells
        neighbors = get_walkable_neighbors(maze, current)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
    return None, explored_cells


# ==========================================================
# PART 3 - OUTPUT
# ==========================================================

def build_path(came_from, start, goal):
    """Builds the shortest path."""
    path = [goal]
    while path[-1] != start:
        previous = came_from[path[-1]]
        path.append(previous)
    path.reverse()
    return path

def print_maze_with_path(maze, path):
    """Prints the maze with the shortest path."""
    grid = []
    for row in maze:
        grid.append(list(row))
    for row, col in path:
        if grid[row][col] not in ("S", "G"):
            grid[row][col] = "*"
    for row in grid:
        print(" ".join(row))

def main():
    maze, start, goal = get_maze_from_user()
    print("\nOriginal Maze:\n")
    print_maze_with_path(maze, [])
    path, explored = find_shortest_path_bfs(maze, start, goal)
    if path is None:
        print("\nNo path available.")
    else:
        print("\nShortest Path Found:\n")
        print_maze_with_path(maze, path)

main()