import random
from enum import Enum
from typing import NamedTuple, List, Optional
from search import Node, dfs, node_to_path


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

    def move_options(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        # check up
        if (
            ml.row + 1 < self._rows
            and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED
        ):
            locations.append(MazeLocation(ml.row + 1, ml.column))
        # check down
        if ml.row >= 1 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        # check right
        if (
            ml.column + 1 < self._columns
            and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED
        ):
            locations.append(MazeLocation(ml.row, ml.column + 1))
        # check left
        if ml.column >= 1 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]) -> None:
        for ml in path:
            self._grid[ml.row][ml.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]) -> None:
        for ml in path:
            self._grid[ml.row][ml.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = f"{'+-'*10}+\n"
        for row in reversed(self._grid):
            output += "|"
            output += "|".join([c.value for c in row])
            output += f"|\n{'+-'*10}+\n"
        return output


if __name__ == "__main__":
    maze = Maze()
    solution1: Optional[Node[MazeLocation]] = dfs(
        maze.start, maze.goal_test, maze.move_options
    )
    if solution1 is None:
        print("No solution found using depth first search")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)
