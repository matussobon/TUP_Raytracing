from vec3 import *
from objects import *


def ray_color(ray):
    # Sphere parameters
    center = Vec3(0, 0, -2)
    radius = 0.5
    t_hit = hit_sphere(center, radius, ray)
    if t_hit is not None:
        return Vec3(1,0,0)


    # background gradient
    unit_dir = ray.direction.unit()
    t = 0.5 * (unit_dir.y + 1.0)
    return Vec3(1.0, 1.0, 1.0)*(1.0 - t) + Vec3(0.5, 0.7, 1.0)*t