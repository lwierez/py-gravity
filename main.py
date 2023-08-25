#!/bin/python3

from pygame import Vector2

from ncorps.objects.planet import Planet
from engine.engine import Engine
from ncorps.objects.ship import Ship


def main():
    heart = Planet()
    heart.position = Vector2(0, 0)
    heart.velocity = Vector2(0, 0)
    heart.mass = 6e24
    heart.radius = 6370
    heart.color = (65, 105, 225)

    iss = Planet()
    iss.position = Vector2(6370 + 420, 0)
    iss.velocity = Vector2(0, -7.66)
    iss.mass = 450000
    iss.radius = 3
    iss.color = (255, 255, 255)

    moon = Planet()
    moon.position = Vector2(384400, 0)
    moon.velocity = Vector2(0, -1)
    moon.mass = 7e22
    moon.radius = 1736
    moon.color = (246, 241, 213)

    player = Ship()
    player.position = Vector2(384400 + 100, 0)
    moon.velocity = Vector2(0, -0)
    player.mass = 30000

    bodies = [heart, iss, moon, player]

    engine = Engine()
    engine.setup(bodies)
    engine.loop()


if __name__ == '__main__':
    main()
