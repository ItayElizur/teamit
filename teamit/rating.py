import numpy as np

from typing import Optional


class Rating:
    def __init__(self, rating: Optional[int] = None):
        self.rating = rating if rating else 5

    def update(self, result_diff: int):
        pass
        # TODO: TAKE Victor's update tool
        # self.rating = 0.9 * self.rating + 0.1 * result_diff, 0, 10
