from typing import List, Tuple


class RPSStrategy:

    def __init__(self, choices: str):
        self.choices = choices
        self.strategy_to_point_mapper = {
            'Rock': 1,
            'Paper': 2,
            'Scissor': 3,
        }
        self.condition_to_point_mapper = {
            'Win': 6,
            'Draw': 3,
            'Lose': 0,
        }
        self.enemy_choice_to_strategy_mapper = {
            'A': "Rock",
            'B': "Paper",
            'C': "Scissor",
        }
        self.our_choice_to_strategy_mapper = {
            'X': "Rock",
            'Y': "Paper",
            'Z': "Scissor",
        }
        self.elf_choice_to_condition_mapper = {
            'X': "Lose",
            'Y': "Draw",
            'Z': "Win",
        }
        self.condition = None

    def to_choice(self, encrypted_message: str) -> Tuple[str, str]:
        enemy_choice, general_choice = encrypted_message.split(' ')
        return enemy_choice, general_choice

    def check_condition(self, enemy_strategy: str, our_strategy: str) -> str:
        condition = ""
        if our_strategy == enemy_strategy:
            condition = "Draw"

        else:
            if our_strategy == "Rock":
                if enemy_strategy == "Scissor":
                    condition = "Win"
                else:
                    condition = "Lose"

            elif our_strategy == "Paper":
                if enemy_strategy == "Rock":
                    condition = "Win"
                else:
                    condition = "Lose"

            elif our_strategy == "Scissor":
                if enemy_strategy == "Paper":
                    condition = "Win"
                else:
                    condition = "Lose"

        return condition

    def pick_strategy(self, enemy_strategy: str, condition: str) -> str:
        strategy = ""
        if condition == "Draw":
            strategy = enemy_strategy

        elif condition == "Win":
            if enemy_strategy == "Rock":
                strategy = "Paper"
            elif enemy_strategy == "Paper":
                strategy = "Scissor"
            elif enemy_strategy == "Scissor":
                strategy = "Rock"

        elif condition == "Lose":
            if enemy_strategy == "Rock":
                strategy = "Scissor"
            elif enemy_strategy == "Paper":
                strategy = "Rock"
            elif enemy_strategy == "Scissor":
                strategy = "Paper"

        return strategy

    def total_point(self, instruction: bool = False) -> int:
        point = 0

        enemy_choice, general_encrypted_message = self.to_choice(self.choices)
        enemy_strategy = self.enemy_choice_to_strategy_mapper[enemy_choice]

        our_strategy = None
        condition = None

        if instruction:
            elf_condition = self.elf_choice_to_condition_mapper[general_encrypted_message]
            our_strategy = self.pick_strategy(enemy_strategy, elf_condition)
            condition = self.check_condition(enemy_strategy, our_strategy)
        else:
            our_strategy = self.our_choice_to_strategy_mapper[general_encrypted_message]
            condition = self.check_condition(enemy_strategy, our_strategy)

        point += self.strategy_to_point_mapper[our_strategy]
        point += self.condition_to_point_mapper[condition]

        return point


class Solution:

    @staticmethod
    def parse(filename):
        encrypted_messages = None
        with open(filename, "r") as f:
            encrypted_messages = f.read().strip().split('\n')
        return encrypted_messages

    @staticmethod
    def solve1(encrypted_messages: List[str]) -> int:
        rps_list = []
        for choices in encrypted_messages:
            rps_strategy = RPSStrategy(choices)
            rps_list.append(rps_strategy)
        return sum(
            map(
                lambda x: x.total_point(), rps_list
            )
        )

    @staticmethod
    def solve2(encrypted_messages: List[str]) -> int:
        rps_list = []
        for choices in encrypted_messages:
            rps_strategy = RPSStrategy(choices)
            rps_list.append(rps_strategy)
        return sum(
            map(
                lambda x: x.total_point(instruction=True), rps_list
            )
        )


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
    print(Solution.solve2(Solution.parse("input.txt")))
