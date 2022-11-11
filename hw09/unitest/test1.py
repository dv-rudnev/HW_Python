import unittest
from code1 import Clothes


class TestSplitFunction(unittest.TestCase):
    """class"""

    def setUp(self):
        self.res = Clothes(48, 188)

    def testcoat(self):
        """test1"""
        self.assertEqual(round(self.res.coat, 2), 7.88)

    def testcostume(self):
        """test2"""
        self.assertEqual(round(self.res.costume, 2), 376.30)


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
