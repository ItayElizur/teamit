import numpy as np

from typing import Optional


class Rank:
    def __init__(self, rank: Optional[int] = None):
        self.rank = rank if rank else 5

    def update(self, result_diff: int):
        # set something smarter
        self.rank = np.clip(0.9 * self.rank + 0.1 * result_diff, 0, 10)
