import mcdc.transport.physics.neutron.multigroup as multigroup
import mcdc.transport.physics.neutron.native as native
import mcdc.transport.util as util
import mcdc.trace as trace

# ======================================================================================
# Particle attributes
# ======================================================================================


@trace.njit()
def particle_speed(particle_container, simulation, data):
    if simulation["settings"]["neutron_multigroup_mode"]:
        return multigroup.particle_speed(particle_container, simulation, data)
    else:
        return native.particle_speed(particle_container)


# ======================================================================================
# Material properties
# ======================================================================================


@trace.njit()
def macro_xs(reaction_type, particle_container, simulation, data):
    if simulation["settings"]["neutron_multigroup_mode"]:
        return multigroup.macro_xs(reaction_type, particle_container, simulation, data)
    else:
        return native.macro_xs(reaction_type, particle_container, simulation, data)


@trace.njit()
def neutron_production_xs(reaction_type, particle_container, simulation, data):
    if simulation["settings"]["neutron_multigroup_mode"]:
        return multigroup.neutron_production_xs(
            reaction_type, particle_container, simulation, data
        )
    else:
        return native.neutron_production_xs(
            reaction_type, particle_container, simulation, data
        )


# ======================================================================================
# Collision
# ======================================================================================


@trace.njit()
def collision(particle_container, collision_data_container, program, data):
    simulation = util.access_simulation(program)

    if simulation["settings"]["neutron_multigroup_mode"]:
        multigroup.collision(
            particle_container, collision_data_container, program, data
        )
    else:
        native.collision(particle_container, collision_data_container, program, data)
