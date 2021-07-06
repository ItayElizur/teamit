from enum import Enum, auto


class SportType(Enum):
    SOCCER = auto()
    BASKETBALL = auto()
    VOLLEYBALL = auto()

    @staticmethod
    def all_types():
        return [SportType.SOCCER, SportType.BASKETBALL, SportType.VOLLEYBALL]
