import unittest

def area(x, y):
    return x * y

def perim(x):
    return x+x+x+x


class squareAreaPerim(unittest.TestCase):

    def test(self):
        self.assertTrue(area(4,4))
        self.assertTrue(perim(4))

if __name__ == '__main__':

    unittest.main()