from string import ascii_letters
from typing import List, Set


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

    @property
    def duplicate_items(self) -> Set[str]:
        return set(self.left_compartment_items).intersection(set(self.right_compartment_items))

    def get_priority(self, items: str) -> int:
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
                lambda x: x.get_priority(x.duplicate_items), rucksack_list
            )
        )


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
