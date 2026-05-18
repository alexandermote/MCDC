import mcdc.trace as trace

####

import mcdc.transport.physics.electron.native as native

# ======================================================================================
# Particle attributes
# ======================================================================================


@trace.njit()
def particle_speed(particle_container, simulation, data):
    return native.particle_speed(particle_container)


# ======================================================================================
# Material properties
# ======================================================================================


@trace.njit()
def macro_xs(reaction_type, particle_container, simulation, data):
    return native.macro_xs(reaction_type, particle_container, simulation, data)


# ======================================================================================
# Collision
# ======================================================================================


@trace.njit()
def collision(particle_container, collision_data_container, program, data):
    native.collision(particle_container, collision_data_container, program, data)
