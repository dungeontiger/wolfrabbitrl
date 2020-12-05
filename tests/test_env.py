import unittest
import random
from wolfrabbit.env import Environment
from wolfrabbit.move_action import MoveAction
from wolfrabbit.objects import Objects
from wolfrabbit.game_status import GameStatus


class TestEnv(unittest.TestCase):

    def test_find_rabbit(self):
        random.seed(1)
        game = Environment(5)
        x, y = game.find_object(Objects.RABBIT)
        self.assertEqual(x, 1)
        self.assertEqual(y, 4)

    def test_find_wolf(self):
        random.seed(2)
        game = Environment(5)
        x, y = game.find_object(Objects.WOLF)
        self.assertEqual(x, 0)
        self.assertEqual(y, 2)

    def test_find_hole(self):
        random.seed(3)
        game = Environment(5)
        x, y = game.find_object(Objects.HOLE)
        self.assertEqual(x, 2)
        self.assertEqual(y, 4)


if __name__ == '__main__':
    unittest.main()