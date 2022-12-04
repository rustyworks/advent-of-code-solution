from solution import Solution


def test_solution_1():
    items = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    expected = 2
    actual = Solution.solve1(items)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"


def test_solution_2():
    items = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    expected = 4
    actual = Solution.solve2(items)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"
