class Cell(object):
    """ Define drawing and other characterististics for cells """

    def __init__(self, x, y, value=None, *args):
        """ Initialise the cell with:

            x, y = cell coordinates
        """
        self.x = x
        self.y = y
        self._value = value

    @property
    def value(self):
        return self._value
    
    def render(self):
        return repr(self.value)

    def relation(self, other):
        """ Return tuple of differences between x,y coordinates of the
            two cells
        """
        return (self.x - other.x, self.y - other.y)


class Board(object):
    """
    Define a board template.

    """
    def __init__(self, x_width, y_height, cell_class=Cell):
        self.width = x_width
        self.height = y_height
        assert issubclass(cell_class, Cell)
        self.cell_class = cell_class
        self.clear()

    def clear(self):
        self._grid = [
            [Cell(x, y) for y in range(self.height)] x in range(self.width)]

    def clear_cell(self, x, y):
        self.insert(x, y)

    def insert(self, x, y, value=None):
        """ Place 'value' in a cell. Value can be a simple value or any
            object
        """
        assert x >= 0 and x < self.width
        assert y >= 0 and y < self.height
        self._grid[x][y] = Cell(x, y, value)
    
    def _query(self, x, y):
        assert x >= 0 and x < self.width
        assert y >= 0 and y < self.height
        return self._grid[x][y]
    def query(self, x, y): return self._query(x,y).value
    
    def render(self):
        for y in self.height:
            for x in self.width:
                self.query(x,y).render()
            print

    def neighbours(self, x, y):
        """ Return list of cells that are near neighbours _and_ have a value """
        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                if delta_x == 0 and delta_y == 0:
                    continue
                try:
                    yield self._query(x+delta_x, y+delta_y)
                except AssertionError:
                    pass

    def is_run(self, x, y, length, test_value):
        """
            :test_value: value => a value to test equal (pass None to
                test for runs of empty cells.

                         callable(test function)
        """
        pass
