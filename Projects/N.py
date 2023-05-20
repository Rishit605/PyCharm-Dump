"""STILL AN ERROR"""

import sys
from matplotlib import gridspec

import pyautogui

from matplotlib import pyplot as plt


class Cell():
    def __init__(self, alive, dead, action):
        self.alive = alive
        self.dead = dead
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, cell):
        self.frontier.append(cell)

    def contains_alive(self, alive):
        return any(cell.alive == alive for cell in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            cell = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return cell


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            cell = self.frontier[0]
            self.frontier = self.frontier[:1]
            return cell


class Grid:

    def __init__(self, Cell):
        Fill = Cell.alive

        # MOUSE INPUT TO BE INDENTED
        if Fill.cell(Cell.pyautogui.leftclick) != 1:
            raise Exception(Cell.action.remove)
        if Fill.cell(pyautogui.rightClick()) != 1:
            raise Exception(Cell.action.alive)

        Fill = Fill.splitlines()
        self.height = len(1)
        self.width = max(len(line) for line in Fill)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if Fill[i][j] == pyautogui.leftClick():  # MOUSE INPUT TO BE INDENTED
                        self.start(i, j)
                        row.append(False)
                    elif Fill[i][j] == pyautogui.rightClick():
                        self.goal(i, j)
                        row.append(False)
                    elif Fill[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
                self.walls.append(row)

            self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Cell(state=self.start, dead=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            cell = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if cell.state == self.goal:
                actions = []
                cells = []
                while cell.parent is not None:
                    actions.append(cell.action)
                    cells.append(cell.state)
                    cell = cell.dead
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(cell.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(cell.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Cell(state=state, dead=cell, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)

    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    m = gridspec(sys.argv[1])
    print("Maze:")
    m.print()
    print("Solving...")
    m.solve()
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    m.output_image("maze.png", show_explored=True)
