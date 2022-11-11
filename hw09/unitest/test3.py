import unittest
from code3 import *


class TestFunction(unittest.TestCase):
    """class"""

    def setUp(self):
        size = 10
        m = 1
        n = 10
        self.res = create_list(size, m, n)

    def testequal(self):
        """test1"""
        self.MultiLineEqual(self.res())

    # def testraises(self):
        # """test2"""
        # self.assertRaises(self.resRaise.calc_asphalt_mass(), "can't multiply sequence by non-int of type 'float'")


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
