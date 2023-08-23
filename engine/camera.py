from pygame import Vector2


class Camera:
    SCREEN_HALF_SIZE = Vector2(640, 360)
    cameras = []
    active = None
    scale = 1
