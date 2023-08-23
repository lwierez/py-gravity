from pygame import Vector2

from planet import Planet
from engine import Engine
from ship import Ship


def main():
    sun = Planet()
    sun.position = Vector2()
    sun.mass = 100000000
    sun.radius = 600
    sun.color = (240, 210, 20)

    heart = Planet()
    heart.position = Vector2(5000, 0)
    heart.velocity = Vector2(0, 400)
    heart.mass = 500000
    heart.radius = 30
    heart.color = (65, 105, 225)

    moon = Planet()
    moon.position = Vector2(5000 + 200, 0)
    moon.velocity = Vector2(-50, 230)
    moon.mass = 500
    moon.radius = 5
    moon.color = (246, 241, 213)

    player = Ship()
    player.position = Vector2(5000, 1000)
    player.mass = 0.01

    bodies = [sun, heart, moon, player]

    engine = Engine()
    engine.setup(bodies)
    engine.loop()


if __name__ == '__main__':
    main()
