class Plate:
    def __init__(self, value, index, is_visited=False):
        self.is_visited = is_visited
        self.index = index
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return "[" + ', '.join([self.value, str(self.index), str(self.is_visited)]) + "]"
