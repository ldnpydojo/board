import itertools

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

        return tuple(loc)

    def occupied(self):
        pass

    def get_viewport(self):
        slice

    def neighbours(self, loc):
        loc = self._bounds_check(loc)

        mins = [x - 1 for x in loc]
        maxs = [x + 1 for x in loc]

        coords = set(itertools.product(*zip(mins, loc, maxs)))
        coords.remove(loc)

        ret = {}
        for c in coords:
            val = self[c]
            if val:
                ret[c] = val

        return ret

if __name__ == '__main__':
    x = Board([5,5], wrap=True)

    x[1,1] = 1
    x[1,2] = 2
    x[1,3] = 3

    print x.neighbours([1,2])