import unittest
from main import *


class TestCuboid(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(mayus("test"), "TEST")


if __name__ == '__main__':
    unittest.main()