import unittest
from code2 import Road


class TestSplitFunction(unittest.TestCase):
    """class"""

    def setUp(self):
        self.res = Road(5000, 20, 25, 0.05)
        # self.resRaise = Road('5000', 20, 25, 0.05)

    def testequal(self):
        """test1"""
        self.assertEqual(self.res.calc_asphalt_mass(), '5000м*20м*25кг*0.05м = 125000 кг = 125 т')

    # def testraises(self):
        # """test2"""
        # self.assertRaises(self.resRaise.calc_asphalt_mass(), "can't multiply sequence by non-int of type 'float'")


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
