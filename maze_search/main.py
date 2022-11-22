import random
from enum import Enum
from typing import NamedTuple, List


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(
        self,
        rows: int = 10,
        columns: int = 10,
        sparseness: float = 0.2,
        start: MazeLocation = MazeLocation(0, 0),
        goal: MazeLocation = MazeLocation(9, 9),
    ):
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for _ in range(columns)] for _ in range(rows)
        ]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for col in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def __str__(self) -> str:
        output: str = f"{'+-'*10}+\n"
        for row in self._grid:
            output += "|"
            output += "|".join([c.value for c in row])
            output += f"|\n{'+-'*10}+\n"
        return output


if __name__ == "__main__":
    maze = Maze(sparseness=0.3)
    print(maze)
