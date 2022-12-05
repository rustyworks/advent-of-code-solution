from typing import List


class CrateStack:

    def __init__(self, crates: List[str]):
        self.number_of_crates = self.get_number_of_crates(crates.pop())
        self.stacks = self.processing_stacks(crates)

    def move(self, movement: str) -> None:
        movement = movement.replace("move ", "")
        movement = movement.replace("from ", "")
        movement = movement.replace("to ", "")
        number_stack, begin, end = list(map(int, movement.split(" ")))
        working_stack = self.stacks[begin - 1]
        crates = []
        for i in range(number_stack):
            try:
                crates.append(working_stack.pop())
            except IndexError:
                pass
        for crate in crates:
            self.stacks[end - 1].append(crate)

    def bulk_move(self, movement: str) -> None:
        movement = movement.replace("move ", "")
        movement = movement.replace("from ", "")
        movement = movement.replace("to ", "")
        number_stack, begin, end = list(map(int, movement.split(" ")))
        crates = self.stacks[begin - 1][-number_stack:]
        del self.stacks[begin - 1][-number_stack:]
        self.stacks[end - 1].extend(crates)

    def get_top_most_stack(self) -> str:
        words = ""
        for crate in self.stacks:
            try:
                words += crate[-1]
            except IndexError:
                pass
        return words

    def get_number_of_crates(self, numbers) -> int:
        return int(numbers.strip().split(" ")[-1])

    def processing_stacks(self, crates: List[str]) -> List[str]:
        stacks = []
        while crates:
            crate = crates.pop()
            for i, cr in enumerate(crate):
                real_index = i // 4
                if i % 4 == 1:
                    try:
                        if cr != " ":
                            stacks[real_index].append(cr)
                    except IndexError:
                        if cr != " ":
                            stacks.append([])
                            stacks[real_index].append(cr)
        return stacks


class Util:

    @staticmethod
    def get_crates(crates_and_movements: List[str]) -> List[str]:
        crates = []
        for data in crates_and_movements:
            if data != "":
                crates.append(data)
            else:
                break
        return crates

    @staticmethod
    def get_movements(crates_and_movements: List[str]) -> List[str]:
        start_appending = False
        movements = []

        for data in crates_and_movements:
            if start_appending:
                movements.append(data)
            if data == "":
                start_appending = True
        return movements


class Solution:

    @staticmethod
    def parse(filename: str) -> List[str]:
        crates_and_movements = None
        with open(filename, "r") as f:
            crates_and_movements = f.read().strip().split("\n")
        return crates_and_movements

    @staticmethod
    def solve1(crates_and_movements: List[str]) -> str:
        crates = Util.get_crates(crates_and_movements)
        crate_stack = CrateStack(crates)
        movements = Util.get_movements(crates_and_movements)
        for movement in movements:
            crate_stack.move(movement)
        return crate_stack.get_top_most_stack()

    @staticmethod
    def solve2(crates_and_movements: List[str]) -> str:
        crates = Util.get_crates(crates_and_movements)
        crate_stack = CrateStack(crates)
        movements = Util.get_movements(crates_and_movements)
        for movement in movements:
            crate_stack.bulk_move(movement)
        return crate_stack.get_top_most_stack()


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
    print(Solution.solve2(Solution.parse("input.txt")))
