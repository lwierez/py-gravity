import pygame

from ncorps.objects.body import Body
from engine.camera import Camera


class Planet(Body):
    def __init__(self):
        super().__init__()
        self.radius = 30
        self.color = (255, 255, 255)

    def on_process(self, delta_time):
        super().on_process(delta_time)

    def on_render(self, screen, delta_time):
        super().on_render(screen, delta_time)
        pygame.draw.circle(screen, self.color,
                           (self.position - Camera.active) * Camera.scale + Camera.SCREEN_HALF_SIZE,
                           max(self.radius * Camera.scale, 1))
