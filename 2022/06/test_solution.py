from solution import Solution


def test_solution_1():
    item_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    item_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    item_3 = "nppdvjthqldpwncqszvftbrmjlhg"
    item_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    item_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    expected_1 = 7
    expected_2 = 5
    expected_3 = 6
    expected_4 = 10
    expected_5 = 11
    actual_1 = Solution.solve1(item_1)
    actual_2 = Solution.solve1(item_2)
    actual_3 = Solution.solve1(item_3)
    actual_4 = Solution.solve1(item_4)
    actual_5 = Solution.solve1(item_5)
    assert expected_1 == actual_1, f"Expected: {expected_1}, Actual: {actual_1}"
    assert expected_2 == actual_2, f"Expected: {expected_2}, Actual: {actual_2}"
    assert expected_3 == actual_3, f"Expected: {expected_3}, Actual: {actual_3}"
    assert expected_4 == actual_4, f"Expected: {expected_4}, Actual: {actual_4}"
    assert expected_5 == actual_5, f"Expected: {expected_5}, Actual: {actual_5}"


def test_solution_2():
    item_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    item_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    item_3 = "nppdvjthqldpwncqszvftbrmjlhg"
    item_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    item_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    expected_1 = 19
    expected_2 = 23
    expected_3 = 23
    expected_4 = 29
    expected_5 = 26
    actual_1 = Solution.solve2(item_1)
    actual_2 = Solution.solve2(item_2)
    actual_3 = Solution.solve2(item_3)
    actual_4 = Solution.solve2(item_4)
    actual_5 = Solution.solve2(item_5)
    assert expected_1 == actual_1, f"Expected: {expected_1}, Actual: {actual_1}"
    assert expected_2 == actual_2, f"Expected: {expected_2}, Actual: {actual_2}"
    assert expected_3 == actual_3, f"Expected: {expected_3}, Actual: {actual_3}"
    assert expected_4 == actual_4, f"Expected: {expected_4}, Actual: {actual_4}"
    assert expected_5 == actual_5, f"Expected: {expected_5}, Actual: {actual_5}"
