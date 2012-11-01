from collections import defaultdict

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.table = defaultdict(lambda: None)

    def size(self):
        return (self.width, self.height)
    
    def put(self, x, y, o):
        if x not in range(self.width) or y not in range(self.height):
            raise IndexError('Out of bounds')
        self.table[(x,y)]=o

    def get(self,x ,y):
        if x not in range(self.width) or y not in range(self.height):
            raise IndexError('Out of bounds')
        return self.table[(x, y)]

    def remove(self, x, y):
        del self.table[(x, y)]

    def neighbours(self, x, y):
        neighbours = set()
        for i in -1, 0, 1:
            for j in -1, 0, 1:
                try:
                    neighbour = self.get(x+i, y+j)
                    if neighbour is not None:
                        neighbours.add(neighbour)
                except IndexError:
                    pass
        return neighbours

    def empty(self):
        return not any(self.table.values())

    def clear(self):
        self.table = defaultdict(lambda: None)

    def __str__(self):
        s = ''
        for k,v in self.table.iteritems():
            s = s + str(k) + '->' + str(v) + '\n'
        return s

class NoughtsAndCrossesBoard(Board):
    def __init__(self):
        Board.__init__(self, 3, 3)

    def __str__(self):
        s = []
        for i in range(3):
            for j in range(3):
                if self.get(i, j) is None:
                    s.append(' ')
                else:
                    s.append(self.get(i, j))
            s.append('\n')
        return ''.join(s)

