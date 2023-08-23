import pygame
from pygame import Vector2

from body import Body
from camera import Camera


class Ship(Body):
    def __init__(self):
        super().__init__()
        self.power = 100
        self.font = None
        self.direction = Vector2()
        self.stabilize = False
        self.lock_space = False

    def on_setup(self):
        super().on_setup()

    def on_start(self):
        super().on_start()
        self.font = pygame.font.SysFont('Comic Sans Ms', 22)

    def on_process(self, delta_time):
        super().on_process(delta_time)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if not self.lock_space:
                self.stabilize = not self.stabilize
                if self.stabilize:
                    self.power = 500
                self.lock_space = True
        elif self.lock_space:
            self.lock_space = False

        inputs = Vector2()
        inputs.x += 1 if keys[pygame.K_RIGHT] else 0
        inputs.x -= 1 if keys[pygame.K_LEFT] else 0
        inputs.y += 1 if keys[pygame.K_DOWN] else 0
        inputs.y -= 1 if keys[pygame.K_UP] else 0

        self.power += 5 if keys[pygame.K_a] else 0
        self.power -= 5 if keys[pygame.K_q] else 0
        self.power = max(10, min(self.power, 100))

        mouse_inputs = pygame.mouse.get_pressed()
        Camera.scale *= 0.99 if mouse_inputs[2] else 1
        Camera.scale *= 1.01 if mouse_inputs[0] else 1

        if inputs.magnitude_squared() > 0:
            if self.stabilize:
                self.stabilize = False
            self.direction = inputs.normalize()
        else:
            self.direction = -self.velocity.normalize() if self.stabilize else inputs

        self.velocity += self.direction * self.power * delta_time

    def on_render(self, screen, delta_time):
        super().on_render(screen, delta_time)

        Camera.active.x = self.position.x
        Camera.active.y = self.position.y

        pygame.draw.circle(screen, (230, 230, 230), (640, 340), max(1, 3 * Camera.scale))

        screen.blit(
            self.font.render(f"Position: {int(self.position.x)} ; {int(self.position.y)}", False, (240, 240, 240)),
            (20, 10))
        screen.blit(self.font.render(f"Speed: {int(self.velocity.magnitude())}", False, (240, 240, 240)), (20, 30))
        screen.blit(
            self.font.render(f"Direction: {self.direction.x:.2n} ; {self.direction.y:.2n}", False, (240, 240, 240)),
            (20, 50))
        screen.blit(self.font.render(f"Power: {int(self.power)}", False, (240, 240, 240)), (20, 70))
        screen.blit(
            self.font.render(f"Stabilize: {'on' if self.stabilize else 'off'}", False, (240, 240, 240)),
            (20, 90))
        screen.blit(self.font.render(f"Scale: {Camera.scale:.2f}", False, (240, 240, 240)), (20, 110))
