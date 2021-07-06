from typing import Dict

from teamit.rank import Rank
from teamit.sport_type import SportType


class Player:
    def __init__(self, name: str, initial_score: Dict[SportType, Rank]):
        self.name = name
        self.initial_score = initial_score
