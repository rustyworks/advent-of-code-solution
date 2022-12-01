from solution import Solution


def test_solution_1():
    calories = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    expected = 24000
    actual = Solution.solve1(calories)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"


def test_solution_2():
    calories = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    expected = 45000
    actual = Solution.solve2(calories)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"
