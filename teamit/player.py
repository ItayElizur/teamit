from typing import Dict

from teamit.rating import Rating
from teamit.sport_type import SportType


class Player:
    def __init__(self, name: str, initial_score: Dict[SportType, Rating]):
        self.name = name
        self.rating = initial_score
        self._relative_goals = []

    def add_match(self, relative_goal: int):
        self._relative_goals.append(relative_goal)
