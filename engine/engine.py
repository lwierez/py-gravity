import pygame
from pygame import Vector2
from scipy import constants

from engine.camera import Camera


class Engine:
    GRAVITATIONAL_CONSTANT = constants.gravitational_constant * 10e-9

    def __init__(self):
        self.is_setup = False
        self.is_running = False
        self.screen = None
        self.clock = None
        self.bodies = []

    def setup(self, bodies):
        if self.is_setup:
            print("Engine has already been set up")
            return

        self.bodies = bodies

        for body in bodies:
            body.on_setup()

        Camera.cameras.append(Vector2(640, 360))
        Camera.active = Camera.cameras[0]

        self.is_setup = True

    def handle_events(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def process(self, delta_time):
        for body in self.bodies:
            self.apply_gravity(body, delta_time)

        for ii, body in enumerate(self.bodies):
            for other in self.bodies[ii + 1:]:
                if body.position.distance_to(other.position) < body.radius + other.radius:
                    # Direction from body to other
                    direction = other.velocity - body.velocity
                    if direction.magnitude_squared() > 0:
                        direction = direction.normalize()
                        energy_from_body = 0.5 * body.mass * (body.velocity - other.velocity).magnitude_squared()
                        energy_from_other = 0.5 * other.mass * (other.velocity - body.velocity).magnitude_squared()
                        body.velocity += energy_from_other / body.mass * direction
                        other.velocity += energy_from_body / other.mass * -direction

        for body in self.bodies:
            body.on_process(delta_time)

    def apply_gravity(self, body, delta_time):
        f = Vector2(0, 0)

        for b in self.bodies:
            if b == body:
                continue

            # Distance between the 2 bodies (squared)
            r = (b.position - body.position).magnitude_squared()
            if r == 0:
                continue
            # Unit vector from body to b
            unit = (b.position - body.position).normalize()
            # Applying gravity formula
            f += self.GRAVITATIONAL_CONSTANT * body.mass * b.mass / r * unit

        body.velocity += f / body.mass * delta_time

    def render(self, delta_time):
        self.screen.fill((25, 25, 112))

        for body in self.bodies:
            body.on_render(self.screen, delta_time)

        pygame.display.flip()

    def loop(self):
        if not self.is_setup or self.is_running:
            print("Engine is already running or has not been set up")
            return

        self.is_running = True

        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        delta_time = 0

        for body in self.bodies:
            body.on_start()

        while self.is_running:
            self.handle_events(delta_time)
            self.process(delta_time)
            self.render(delta_time)
            delta_time = self.clock.tick(60) / 1000
