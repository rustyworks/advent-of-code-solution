from typing import List


class CleaningPairs:

    def __init__(self, pairs: str):
        self.pairs = pairs.split(",")
        self.first_pair = self.pairs[0]
        self.second_pair = self.pairs[1]

    def is_sub(self) -> bool:
        return (
            self.first_pair_responsibility.issubset(
                self.second_pair_responsibility
            ) or self.first_pair_responsibility.issuperset(
                self.second_pair_responsibility
            )
        )

    def is_overlapped(self) -> bool:
        return bool(
            self.first_pair_responsibility.intersection(
                self.second_pair_responsibility
            )
        )

    @property
    def first_pair_responsibility(self) -> set:
        min_room, max_room = [int(room) for room in self.first_pair.split("-")]
        return set(range(min_room, max_room + 1))

    @property
    def second_pair_responsibility(self) -> set:
        min_room, max_room = [int(room) for room in self.second_pair.split("-")]
        return set(range(min_room, max_room + 1))


class Solution:

    @staticmethod
    def parse(filename: str) -> List[str]:
        with open(filename, "r") as f:
            pairs_list = f.read().strip().split('\n')
        return pairs_list

    @staticmethod
    def solve1(pairs_list: List[str]) -> int:
        cleaning_pairs_list = []
        for pairs in pairs_list:
            cleaning_pairs = CleaningPairs(pairs)
            cleaning_pairs_list.append(cleaning_pairs)
        return sum(
            map(
                lambda x: x.is_sub(),
                cleaning_pairs_list
            )
        )

    @staticmethod
    def solve2(pairs_list: List[str]) -> int:
        cleaning_pairs_list = []
        for pairs in pairs_list:
            cleaning_pairs = CleaningPairs(pairs)
            cleaning_pairs_list.append(cleaning_pairs)
        return sum(
            map(
                lambda x: x.is_overlapped(),
                cleaning_pairs_list
            )
        )


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
    print(Solution.solve2(Solution.parse("input.txt")))
