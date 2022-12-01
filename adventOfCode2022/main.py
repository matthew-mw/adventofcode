import requests


class Solutions:

    def __init__(self, session: str):
        self.session = requests.session()
        self.session.cookies.set("session", session, domain="adventofcode.com")

    def getPuzzle(self, day: int):
        request = self.session.get(f"https://adventofcode.com/2022/day/{day}/input")
        puzzle = request.text
        return puzzle

    def day1P1(self):
        puzzle = self.getPuzzle(1)
        return max([sum([int(calorie) for calorie in elve.splitlines()]) for elve in puzzle.split("\n\n")])

    def day1P2(self):
        puzzle = self.getPuzzle(1)
        return sum(sorted([sum([int(calorie) for calorie in elve.splitlines()]) for elve in puzzle.split("\n\n")])[-3:])
