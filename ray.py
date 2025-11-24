class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction  # should be normalized for nicer numeric behavior
    def at(self, t): return self.origin + self.direction * t