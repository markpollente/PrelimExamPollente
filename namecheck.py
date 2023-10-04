import unittest

def namecheck():
    return "MIGUEL"


class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(namecheck(), "MIGUEL")

if __name__ == '__main__':

    unittest.main()