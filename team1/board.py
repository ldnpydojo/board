
class Board(object):

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.state = []

    def place(self, x, y, obj):
        self.state.append(obj)

    def contents(self):
        return self.state

    def contents_of(self, x, y):
        return  None

    def get(self, x, y):
        return "Foo"

    def neighbours(self, x, y):
        return ['Bar']

    def __str__(self):
        return '          \n          \n          \n          \n          \n          \n          \n          \n          \n          '
