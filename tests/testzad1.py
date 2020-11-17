import unittest
from src.sample.zad1 import *


class HammingParametrizedFile(unittest.TestCase):
    def test_from_file(self):
        fileTest = open("data/zad1_data_test")
        for line in fileTest:
            if line.startswith('#') or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(',')
                inp1, inp2, result = str(data[0]), str(data[1]), int(data[2].strip("\n"))
                self.assertEqual(self.hamming.distance(inp1,inp2), result)
        fileTest.close()

    def setUp(self):
        self.hamming = Hamming()


if __name__ == '__main__':
    unittest.main()
