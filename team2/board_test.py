import board
import unittest

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = board.Board(15, 10)

    def test_dimensions(self):
        "2-dimensional finite board"
        self.assertEqual(self.board.size(), (15, 10))

    def test_setter_and_getters(self):
        self.board.put(1, 1, "A gem")
        self.assertEqual(self.board.get(1, 1), "A gem")

    def test_remove(self):
        self.board.put(1, 1, "A gem")
        self.board.remove(1,1)
        self.assertTrue((1,1) not in self.board.table.keys())
        self.assertEqual(self.board.get(1,1), None)
        

    def test_outofbounds(self):
        self.assertRaises(IndexError, self.board.put, 15, 1, 'Bad thing')

    def test_neighbours(self):
        gem = 'a gem'
        diamond = 'a diamond'
        self.board.put(1, 1, gem)
        self.board.put(1, 2, diamond)
        self.assertEqual(self.board.neighbours(2, 1), set([diamond, gem]))

    def test_clear(self):
        self.assertTrue(self.board.empty())
        self.board.put(1, 1, "X")
        self.assertFalse(self.board.empty())
        self.board.clear()
        self.assertTrue(self.board.empty())

    def test_textual_display(self):
        gem = 'a gem'
        diamond = 'a diamond'
        self.board.put(1, 1, gem)
        self.board.put(2, 2, diamond)

        display = str(self.board)
        self.assertTrue(gem in display)
        self.assertTrue(diamond in display)
        self.assertTrue(display.index(gem) < display.index(diamond))

class NoughtsAndCrossesBoardTest(unittest.TestCase):
    def test_textual_display(self):
        b = board.NoughtsAndCrossesBoard()
        b.put(0, 0, 'X')
        b.put(1, 1, 'O')
        self.assertEqual('X  \n O \n   \n', str(b))



if __name__ == "__main__":
    unittest.main()
