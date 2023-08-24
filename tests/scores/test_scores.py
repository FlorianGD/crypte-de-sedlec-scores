import pytest

from sedlec.scores.scores import Figure, Skull, score_by_figure


@pytest.fixture
def mini_grid() -> list[Skull]:
    # A mini grid like so
    #
    #     P     <- level 4
    #     R     <- level 3
    #   B   R   <- level 2
    #   P   L   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores:
    # Royals: 1 + 2 = 3 points
    # Peasants: 1 + 1 = 2 points
    return [
        Skull(column=1, level=1, figure=Figure.PEASANT),
        Skull(column=1, level=2, figure=Figure.BISHOP),
        Skull(column=3, level=1, figure=Figure.LOVER),
        Skull(column=3, level=2, figure=Figure.ROYAL),
        Skull(column=2, level=3, figure=Figure.ROYAL),
        Skull(column=2, level=4, figure=Figure.PEASANT),
    ]


def test_peasant_scores(mini_grid: list[Skull]) -> None:
    """1 point per card in the grid"""
    assert score_by_figure(mini_grid, Figure.PEASANT) == 2


def test_royal_scores(mini_grid: list[Skull]) -> None:
    assert score_by_figure(mini_grid, Figure.ROYAL) == 3


def test_bishop_mini_grid(mini_grid: list[Skull]) -> None:
    assert score_by_figure(mini_grid, Figure.BISHOP) == 2


@pytest.fixture
def bishop_grid() -> list[Skull]:
    # A mini grid like so
    #
    #     B     <- level 4
    #     P     <- level 3
    #   B   B   <- level 2
    #   P   B   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores:
    # Bishops: 2 + 2 + 2 = 6 points
    return [
        Skull(column=1, level=1, figure=Figure.PEASANT),
        Skull(column=1, level=2, figure=Figure.BISHOP),
        Skull(column=3, level=1, figure=Figure.BISHOP),
        Skull(column=3, level=2, figure=Figure.BISHOP),
        Skull(column=2, level=3, figure=Figure.PEASANT),
        Skull(column=2, level=4, figure=Figure.BISHOP),
    ]


def test_bishop_grid(bishop_grid: list[Skull]) -> None:
    assert score_by_figure(bishop_grid, Figure.BISHOP) == 6


@pytest.fixture
def criminals_grid_1() -> list[Skull]:
    # A mini grid like so
    #
    #   C   B   C   <- level 2
    #   C   R   P   <- level 1
    #   ^ ^ ^ ^ ^
    #   \ \ \ \ \
    #   1 2 3 4 5

    # With this grid we have those scores (top left to bottom right):
    # Criminals: 2 + 2 + 0 = 4 points
    return [
        Skull(column=1, level=1, figure=Figure.CRIMINAL),
        Skull(column=1, level=2, figure=Figure.CRIMINAL),
        Skull(column=3, level=1, figure=Figure.ROYAL),
        Skull(column=3, level=2, figure=Figure.BISHOP),
        Skull(column=5, level=1, figure=Figure.PEASANT),
        Skull(column=5, level=2, figure=Figure.CRIMINAL),
    ]


def test_criminals_same_line(criminals_grid_1: list[Skull]) -> None:
    assert score_by_figure(criminals_grid_1, Figure.CRIMINAL) == 4


@pytest.fixture
def criminals_grid_2() -> list[Skull]:
    # A mini grid like so
    #
    #     C     <- level 4
    #     C     <- level 3
    #   R   B   <- level 2
    #   C   R   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores (top left to bottom right):
    # Criminals: 0 + 2 + 0 = 2 points
    return [
        Skull(column=1, level=1, figure=Figure.CRIMINAL),
        Skull(column=1, level=2, figure=Figure.ROYAL),
        Skull(column=3, level=1, figure=Figure.ROYAL),
        Skull(column=3, level=2, figure=Figure.BISHOP),
        Skull(column=2, level=3, figure=Figure.CRIMINAL),
        Skull(column=2, level=4, figure=Figure.CRIMINAL),
    ]


def test_criminals_diagonal_top_left(criminals_grid_2: list[Skull]) -> None:
    assert score_by_figure(criminals_grid_2, Figure.CRIMINAL) == 2


@pytest.fixture
def criminals_grid_3() -> list[Skull]:
    # A mini grid like so
    #
    #     R     <- level 4
    #     B     <- level 3
    #   C   C   <- level 2
    #   C   R   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores (top left to bottom right):
    # Criminals: 2 + 2 + 0 = 4 points
    return [
        Skull(column=1, level=1, figure=Figure.CRIMINAL),
        Skull(column=1, level=2, figure=Figure.CRIMINAL),
        Skull(column=3, level=1, figure=Figure.ROYAL),
        Skull(column=3, level=2, figure=Figure.CRIMINAL),
        Skull(column=2, level=3, figure=Figure.BISHOP),
        Skull(column=2, level=4, figure=Figure.ROYAL),
    ]


def test_criminals_diagonal_bottom(criminals_grid_3: list[Skull]) -> None:
    assert score_by_figure(criminals_grid_3, Figure.CRIMINAL) == 4


@pytest.fixture
def lovers_grid_1() -> list[Skull]:
    # A mini grid like so
    #
    #     R     <- level 4
    #     L     <- level 3
    #   L   C   <- level 2
    #   C   L   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores (top left to bottom right):
    # Criminals: 3 + 3 + 0 = 6 points
    return [
        Skull(column=1, level=1, figure=Figure.CRIMINAL),
        Skull(column=1, level=2, figure=Figure.LOVER),
        Skull(column=3, level=1, figure=Figure.LOVER),
        Skull(column=3, level=2, figure=Figure.CRIMINAL),
        Skull(column=2, level=3, figure=Figure.LOVER),
        Skull(column=2, level=4, figure=Figure.ROYAL),
    ]


def test_lovers_diagonal(lovers_grid_1: list[Skull]) -> None:
    assert score_by_figure(lovers_grid_1, Figure.LOVER) == 6


@pytest.fixture
def lovers_grid_2() -> list[Skull]:
    # A mini grid like so
    #
    #     L     <- level 4
    #     B     <- level 3
    #   L   L   <- level 2
    #   C   C   <- level 1
    #   ^ ^ ^
    #   \ \ \
    #   1 2 3

    # With this grid we have those scores (top left to bottom right):
    # Criminals: 0 + 3 + 3 = 6 points
    return [
        Skull(column=1, level=1, figure=Figure.CRIMINAL),
        Skull(column=1, level=2, figure=Figure.LOVER),
        Skull(column=3, level=1, figure=Figure.CRIMINAL),
        Skull(column=3, level=2, figure=Figure.LOVER),
        Skull(column=2, level=3, figure=Figure.BISHOP),
        Skull(column=2, level=4, figure=Figure.LOVER),
    ]


def test_lovers_same_line(lovers_grid_2: list[Skull]) -> None:
    assert score_by_figure(lovers_grid_2, Figure.LOVER) == 6
