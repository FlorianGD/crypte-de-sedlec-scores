from enum import Enum, auto
from typing import Self

from attr import define


# those are not the "canon" names, but they make for different initials
class Figure(Enum):
    PEASANT = auto()
    ROYAL = auto()
    LOVER = auto()
    BISHOP = auto()
    CRIMINAL = auto()


@define
class Skull:
    column: int
    level: int
    figure: Figure

    def _neighboring(self, other: Self) -> bool:
        return (
            self != other
            and (self.level == other.level and abs(self.column - other.column) <= 2)
            or (
                abs(self.level - other.level) == 1
                and abs(self.column - other.column) == 1
            )
        )

    def _score_peasant(self, _grid: list[Self]) -> int:
        return 1

    def _score_royal(self, grid: list[Self]) -> int:
        return sum(
            1
            for s in grid
            if s.level < self.level and s.figure in [Figure.PEASANT, Figure.ROYAL]
        )

    def _score_bishop(self, grid: list[Self]) -> int:
        same_line_bishops = sorted(
            (s for s in grid if s.figure is Figure.BISHOP and s.level == self.level),
            key=lambda x: x.column,
        )
        # we give points only for the leftmost card
        return 2 if same_line_bishops[0] == self else 0

    def _score_criminal(self, grid: list[Self]) -> int:
        neighboring_bishops = [
            x for x in grid if x.figure is Figure.BISHOP and x._neighboring(self)
        ]
        return 2 if neighboring_bishops else 0

    def _score_lover(self, grid: list[Self]) -> int:
        neighboring_lovers = [
            x for x in grid if x.figure is Figure.LOVER and x._neighboring(self)
        ]
        return 3 if neighboring_lovers else 0

    def score(self, grid: list[Self]):
        match self.figure:
            case Figure.PEASANT:
                return self._score_peasant(grid)
            case Figure.ROYAL:
                return self._score_royal(grid)
            case Figure.BISHOP:
                return self._score_bishop(grid)
            case Figure.CRIMINAL:
                return self._score_criminal(grid)
            case Figure.LOVER:
                return self._score_lover(grid)


def score_by_figure(grid: list[Skull], figure: Figure) -> int:
    return sum(s.score(grid) for s in grid if s.figure is figure)
