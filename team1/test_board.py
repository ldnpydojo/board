import unittest
from board import Board

class TestBoard(unittest.TestCase):
    """
    Tests for the board class.
    """

    def test_empty_position(self):
        b = Board(64, 64)
        self.assertEqual(b.contents_of(20, 20), None)

    def test_piece_placement(self):
        b = Board(64, 64)
        b.place(20, 20, {})
        self.assertEquals(len(b.contents()), 1)

    def test_piece_placed(self):
        b = Board(2,3)
        b.place(2,1,"Foo")
        self.assertEquals(b.get(2,1), "Foo")

    def test_piece_check_neighbour(self):
        b = Board(10, 10)
        b.place(2,1,"Foo")
        b.place(2,2,"Bar")
        self.assertEquals(b.get_neighbours(2,1, ["Bar"]))

