from vec3 import Vec3
from ray import Ray

class Camera:
    def __init__(self, aspect, viewport_height=2.0, focal_length=1):
        self.origin = Vec3(0,0,0)
        self.viewport_height = viewport_height
        self.viewport_width = aspect * viewport_height
        self.horizontal = Vec3(self.viewport_width, 0, 0)
        self.vertical = Vec3(0, self.viewport_height, 0)
        self.lower_left = self.origin - self.horizontal/2 - self.vertical/2 - Vec3(0,0,focal_length)

    def get_ray(self, u, v):
        return Ray(self.origin, (self.lower_left + self.horizontal*u + self.vertical*v - self.origin).unit())