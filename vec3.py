import math
class Vec3(tuple):
    # create a new Vec3 object
    # store (x,y,z) inside it as a tuple
    def __new__(cls, x=0.0, y=0.0, z=0.0):
        return super().__new__(cls, (float(x), float(y), float(z)))

    @property
    def x(self):
        return self[0]
    @property
    def y(self):
        return self[1]
    @property
    def z(self):
        return self[2]

    def __add__(self, t):
        return Vec3(self.x + t.x, self.y + t.y, self.z + t.z)

    def __sub__(self,t):
        return Vec3(self.x - t.x, self.y  - t.y, self.z - t.z)

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x, self.y * t.y, self.z * t.z)
        return Vec3(self.x * t, self.y * t, self.z * t)

    __rmul__ = __mul__

    def __truediv__(self, t):
        return self * (1.0 / t)

    def dot(self,t):
        return self.x*t.x+self.y*t.y+self.z*t.z

    def length(self):
        return math.sqrt(self.dot(self))

    def unit(self):
        return Vec3(self.x/self.length(),self.y/self.length(),self.z/self.length())

    def to_color_tuple(self):
        # clamp and convert floats in [0,1] to 0..255 ints
        def to8(v): return int(255.999 * max(0.0, min(1.0, v)))

        return (to8(self.x), to8(self.y), to8(self.z))