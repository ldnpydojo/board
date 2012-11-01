class Board(object):
    def __init__(self, dimensions, wrap=False, infinite=False):
        self.dimensions = dimensions
        self.num_dimensions = len(dimensions)
        self.wrap = wrap
        self.infinite = infinite

        if wrap and infinite:
            raise ValueError("A board cannot wrap and be infinite.")

        self._data = {}

    def clear(self):
        self._data = {}

    def __getitem__(self, loc):
        loc = self._bounds_check(loc)

        try:
            return self._data[loc]
        except KeyError:
            return None

    def __setitem__(self, loc, val):
        loc = self._bounds_check(loc)

        self._data[loc] = val

    def __delitem__(self, loc):
        loc = self._bounds_check(loc)

        try:
            del self._data[loc]
        except KeyError:
            pass

    def _bounds_check(self, loc):
        if len(loc) != self.num_dimensions:
            raise ValueError("Wrong number of dimensions for given key")

        if self.wrap and not self.infinite:
            loc = [x % self.dimensions[i] for i, x in enumerate(loc)]

        if not self.infinite:
            for i, dim in enumerate(loc):
                if not (0 <= dim < self.dimensions[i]):
                    raise ValueError("Location out of bounds")

        return loc

    def occupied(self):
        pass

    def get_viewport(self):
        slice

    def neighbours(self, loc):
        for dim in loc:
            coords.add(dim-1

        return {coord: val}


if __name__ == '__main__':
    x = Board([5,5,5], wrap=True)

    x[100,1,1] = 1
    print x[100, 1, 1]