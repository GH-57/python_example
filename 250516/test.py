import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(1, 4), 5)
        self.assertEqual(add(1, 2), 2)


if __name__ == '__main__':
    unittest.main()