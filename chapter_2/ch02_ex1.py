from typing import Tuple

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11

class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10


from enum import Enum

class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"

Suit.Club