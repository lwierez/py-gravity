from pygame import Vector2


class Body:
    def __init__(self):
        self.mass = 30
        self.radius = 10
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    # Called at set up. At this point, bodies are created but pygame is not initialized
    def on_setup(self):
        return

    # Called right before the engine loop starts
    def on_start(self):
        return

    # Called at each physics step
    def on_process(self, delta_time):
        self.position += self.velocity * delta_time

    # Called at each rendering step
    def on_render(self, screen, delta_time):
        return
