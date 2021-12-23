import unittest
import doctest
from src.player import Player


class Player_test_doctest(Player):
    def player_test(self):
        """
        >>> p = Player_test_doctest("Rick", "blue")
        >>> p.name
        Rick
        >>> p.change_name("Morty")
        Morty
        >>> p.return_player()
        {"Rick": "blue"}
        """


if __name__ == "__main__":
    doctest.testmod(extraglobs={"p": Player_test_doctest})
    unittest.main()
