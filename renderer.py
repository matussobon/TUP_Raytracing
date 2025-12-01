from vec3 import *
from objects import *


def ray_color(ray, sphere_center, sphere_radius):

    t_hit = hit_sphere(sphere_center, sphere_radius, ray)

    if t_hit > 0:
        sphere_normal = (ray.at(t_hit) - sphere_center).unit()
        return Vec3(0.5*(sphere_normal.x + 1.0), 0.5*(sphere_normal.y + 1.0), 0.5*(sphere_normal.z + 1.0))
    # if t_hit is not None:
    #     return Vec3(1,0,0)

    # background gradient
    unit_dir = ray.direction.unit()
    t = 0.5 * (unit_dir.y + 1.0)
    return Vec3(1.0, 1.0, 1.0)*(1.0 - t) + Vec3(0.5, 0.7, 1.0)*t