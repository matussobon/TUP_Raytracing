import math

def hit_sphere(center, radius, ray):
    oc = center - ray.origin

    a = ray.direction.dot(ray.direction)
    b = -2*(ray.direction.dot(oc))
    c = oc.dot(oc) - radius**2
    h = ray.direction.dot(oc)

    discriminant = h**2-a*c

    if discriminant < 0:
        return -1.0
    else: return (h - math.sqrt(discriminant))/a