class MessageParser:

    def __init__(self, encrypted_message):
        self.encrypted_message = encrypted_message

    def marker_signal(self, number_check: int) -> int:
        iteration = 0
        encrypted_message = self.encrypted_message
        while encrypted_message:
            signal = encrypted_message[:number_check]
            if len(set(signal)) == number_check:
                return number_check + iteration
            iteration += 1
            encrypted_message = encrypted_message[1:]
        return iteration + number_check


class Solution:

    @staticmethod
    def parse(filename: str) -> str:
        encrypted_message = ""
        with open(filename, "r") as f:
            encrypted_message = f.read().strip()
        return encrypted_message

    @staticmethod
    def solve1(encrypted_message: str) -> int:
        parser = MessageParser(encrypted_message)
        return parser.marker_signal(4)

    @staticmethod
    def solve2(encrypted_message: str) -> int:
        parser = MessageParser(encrypted_message)
        return parser.marker_signal(14)


if __name__ == "__main__":
    print(Solution.solve1(Solution.parse("input.txt")))
    print(Solution.solve2(Solution.parse("input.txt")))
