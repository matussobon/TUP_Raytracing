from camera import *
from renderer import *

import pygame

# ---------- Main: render to pygame window ----------
def main():

    pygame.init()
    pygame.display.set_caption("Simple Sphere - single-sample render (press ESC to quit)")

    aspect_ratio = 16.0/9.0
    image_width = 800
    image_height = int(image_width / aspect_ratio)
    screen = pygame.display.set_mode((image_width, image_height))

    cam = Camera(aspect_ratio)

    clock = pygame.time.Clock()

    sphere_center = Vec3(0,0,-1)
    sphere_radius = 0.5

    # Render once (no antialiasing). If you want AA, sample randomly per pixel.
    for j in range(image_height):
        for i in range(image_width):
            u = i / (image_width - 1)
            v = (image_height - 1 - j) / (image_height - 1)  # flip Y so image is right-side-up

            r = cam.get_ray(u, v)
            col = ray_color(r,sphere_center,sphere_radius)
            screen.set_at((i, j), col.to_color_tuple())
        # optional: update row-by-row so you see progress
        pygame.display.flip()
        # handle events so window stays responsive while rendering
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                pygame.quit()
                return

    pygame.display.flip()
    # simple event loop so image remains until window closed
    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


