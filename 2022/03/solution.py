from string import ascii_letters
from typing import List, Set, Iterable


class Rucksack:

    def __init__(self, items: str) -> None:
        self.items = list(items)
        self.total_items = len(items)
        self.divider = self.total_items // 2

    @property
    def left_compartment_items(self) -> List[str]:
        return self.items[:self.divider]

    @property
    def right_compartment_items(self) -> List[str]:
        return self.items[self.divider:]

    @staticmethod
    def check_duplicate_items(items_list: List[str]) -> Set[str]:
        items_set = [set(items) for items in items_list]
        return items_set[0].intersection(*items_set[1:])

    def get_priority(self, items: Iterable[str]) -> int:
        total_priority_index = 0
        for item in items:
            total_priority_index += ascii_letters.index(item) + 1
        return total_priority_index


class Solution:

    @staticmethod
    def parse(filename: str) -> List[str]:
        user_input = []
        with open(filename, "r") as f:
            user_input = f.read().strip().split('\n')
        return user_input

    @staticmethod
    def solve1(items_list: List[str]) -> int:
        rucksack_list = []
        for items in items_list:
            rucksack = Rucksack(items)
            rucksack_list.append(rucksack)
        return sum(
            map(
                lambda x: x.get_priority(
                    Rucksack.check_duplicate_items(
                        [
                            x.left_compartment_items,
                            x.right_compartment_items,
                        ]
                    )
                ), rucksack_list
            )
        )

    @staticmethod
    def solve2(items_list: List[str]) -> int:
        rucksack_list = []
        total_badge_points = 0
        counter = 1
        for items in items_list:
            rucksack = Rucksack(items)
            rucksack_list.append(rucksack)
            if counter % 3 == 0:
                badges = Rucksack.check_duplicate_items(
                    list(map(lambda x: x.items, rucksack_list))
                )
                total_badge_points += rucksack.get_priority(badges)
                rucksack_list = []
            counter += 1
        return total_badge_points


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
    print(Solution.solve2(Solution.parse("input.txt")))
