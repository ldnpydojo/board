import unittest
import random
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
        self.assertEquals(b.neighbours(2,1), ["Bar"])

    def test_show_board(self):
        b = Board(10, 10)
        self.assertEqual('{}'.format(b), (((' ' * 10) + '\n') * 10) [:-1])

    def test_pieces_are_placed_and_restored(self):
        width = 4000
        height = 4000
        board = Board(width, height)
        pieces = [(random.randint(0, width), random.randint(0, height), { "i" : random.randint(0, 5000)}) for x in range(0, random.randint(0, 57000))]

        for piece in pieces:
            board.place(piece[0], piece[1],  piece[2])
            self.assertEquals(board.get(piece[0], piece[1])["i"], piece[2])

        self.assertEquals(len(board.contents()), len(pieces))
