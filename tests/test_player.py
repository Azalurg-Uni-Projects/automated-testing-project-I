import unittest
from hamcrest import *
from src.player import Player


class Player_test(unittest.TestCase):
    def setUp(self):
        self.player = Player("Bob", "%green%")

    def test_instance(self):
        assert_that(self.player, instance_of(Player))

    def test_correct_name(self):
        assert_that(self.player.name, equal_to("Bob"))

    def test_color_ends_with(self):
        assert_that(self.player.color, ends_with("%"))

    def test_player_change_name(self):
        assert_that(self.player.change_name("Piter"), all_of(contains_string("iter"), starts_with("P")))

    def test_return_player_positive(self):
        assert_that(self.player.return_player(), all_of(has_key("Bob"), has_value("%green%")))

    def test_return_player_negative(self):
        self.player.change_name(None)
        assert_that(calling(self.player.return_player), raises(ValueError))

    def tearDown(self):
        self.player = None
