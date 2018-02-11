from vpython import *
import numpy as np

"""
units:
    distance: meters
    time: seconds
    mass: kg
"""
scene.caption = 'apollo 8'

scene.center = vector(3.84402e8, 0, 0) / 2

earth = sphere(pos=vector(0, 0, 0), radius=6.3781e6, color = color.cyan)
earth.mass = 5.972e24

moon = sphere(pos=vector(3.84402e8, 0, 0), radius=1.7371e6)
moon.mass = 7.34767309e22
moon.velocity = vector(0, 1.022e3, 0)

ship = sphere(pos=vector(0, -(346733.4696+ earth.radius), 0), radius=1e6)
ship.mass = 1.3521567e5
ship.velocity = vector(7.793e3,0,0) # 1.0821e4 tli

grav_const = 6.674e-11

# 378

#364340



# F = G (m1 * m2/ r^2)
# update forces on ship and moon
def update_forces():
    # moon
    d = earth.pos - moon.pos # direction
    r2 = mag2(d) # radius square

    # force is a vector
    moon.force = norm(d) * grav_const * (moon.mass * earth.mass)/ r2

    # ship

    # with earth
    d = earth.pos - ship.pos # direction
    r2 = mag2(d) # radius square

    # force is a vector
    ship.force = norm(d) * grav_const * (ship.mass * earth.mass)/ r2

    # with moon
    d = moon.pos - ship.pos
    r2 = mag2(d)

    # add moon forces
    ship.force += norm(d) * grav_const * (ship.mass * moon.mass)/ r2

# F = Ma
def update_velocities():
    moon.velocity += moon.force / moon.mass
    ship.velocity += ship.force / ship.mass

def update_positions():
    moon.pos += moon.velocity
    ship.pos += ship.velocity

# number of elapsed seconds per frame
seconds_per_frame = 1

while 1:
    # frames per second
    rate(100)

    for _ in range(seconds_per_frame):
        update_forces()
        update_velocities()
        update_positions()

    scene.center = ship.pos
