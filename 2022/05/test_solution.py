from solution import Solution


def test_solution_1():
    items = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    expected = "CMZ"
    actual = Solution.solve1(items)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"


def test_solution_2():
    items = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    expected = "MCD"
    actual = Solution.solve2(items)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"
