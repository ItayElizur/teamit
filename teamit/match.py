from typing import List

from teamit.player import Player
from teamit.sport_type import SportType


class Match:
    def __init__(self, sport_type: SportType, team_a: List[Player], team_b: List[Player]):
        self.sport_type = sport_type
        self.team_a = team_a
        self.team_b = team_b

    def set_score(self, score_a: int, score_b: int):
        for player in self.team_a:
            player.add_match(score_a - score_b)
        for player in self.team_b:
            player.add_match(score_b - score_a)
