from typing import List, Iterable


class Elf:

    def __init__(self, calories: List[int]) -> None:
        self.calories = calories

    @property
    def total_calories(self) -> int:
        return sum(self.calories)


class Solution:

    @staticmethod
    def parse(filename: str) -> Iterable[str]:
        calories = None
        with open(filename, 'r') as f:
            calories = map(lambda x: x.strip(), f.readlines())
        return calories

    @classmethod
    def solve1(cls, calories: List[str]) -> int:
        elf_list = cls.get_total_elf_calories(calories)

        result = max(map(lambda x: x.total_calories, elf_list))
        return result

    @classmethod
    def solve2(cls, calories: List[str]) -> int:
        elf_list = cls.get_total_elf_calories(calories)

        result = (
            list(
                sorted(
                    map(lambda x: x.total_calories, elf_list),
                    reverse=True)
            )
        )
        return sum(result[:3])

    @classmethod
    def get_total_elf_calories(cls, calories: List[str]):
        elf_list = []
        calory_list = []
        for calory in calories:
            if calory:
                calory_list.append(int(calory))
            else:
                if calory_list:
                    elf_list.append(Elf(calory_list))
                    calory_list = []
        else:
            if calory_list:
                elf_list.append(Elf(calory_list))
                calory_list = []
        return elf_list


if __name__ == "__main__":
    user_input = list(Solution.parse('input.txt'))
    print(f"Solution 1: {Solution.solve1(user_input)}")
    print(f"Solution 2: {Solution.solve2(user_input)}")
