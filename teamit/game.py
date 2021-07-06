from typing import List

from teamit.player import Player


class Game:
    def __init__(self, players: List[Player], num_teams: int):
        self._players = players.sort(key=lambda player: player.rating)
        self._num_teams = num_teams
        self._teams = None

    def create_teams(self):
        if not self._teams:

        return self._teams

    def match_ended(self):
        pass