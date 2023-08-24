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

    moon = Planet()
    moon.position = Vector2(384400, 0)
    moon.velocity = Vector2(0, -1)
    moon.mass = 7e22
    moon.radius = 1736
    moon.color = (246, 241, 213)

    player = Ship()
    player.position = Vector2(0, 0)
    player.mass = 30000

    bodies = [heart, moon, player]

    engine = Engine()
    engine.setup(bodies)
    engine.loop()


if __name__ == '__main__':
    main()
