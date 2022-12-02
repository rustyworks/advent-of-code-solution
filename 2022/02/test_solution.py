from solution import Solution


def test_solution_1():
    encrypted_strategies = [
        "A Y",
        "B X",
        "C Z",
    ]
    expected = 15
    actual = Solution.solve1(encrypted_strategies)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"


def test_solution_2():
    encrypted_strategies = [
        "A Y",
        "B X",
        "C Z",
    ]
    expected = 12
    actual = Solution.solve2(encrypted_strategies)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"
