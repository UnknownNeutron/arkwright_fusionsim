import random

boltzmann_constant = 1.380649e-23
energy = boltzmann_constant / 2

total_d_particles = 0
total_t_particles = 0
live_d_particles = 0
live_t_particles = 0

total_cycles = 0
total_fusion_events = 0
total_fusion_pairs = 0

reactor_wall_neutron_energy = 0

plasma = []


def INITIALISE_PLASMA():
    global total_d_particles, total_t_particles, live_d_particles, live_t_particles

for i in range(10000):
        if random.randint(0, 1) == 1:
            variability = random.uniform(0.75, 1.25)
            particle_energy = energy * variability
            plasma.append({"particle_type": "deuterium", "particle_energy": particle_energy})
            total_d_particles += 1
            live_d_particles = total_d_particles
        else:
            variability = random.uniform(0.75, 1.25)
            particle_energy = energy * variability
            plasma.append({"particle_type": "tritium", "particle_energy": particle_energy})
            total_t_particles += 1
            live_t_particles = total_t_particles


def RUN_PLASMA():
    global total_cycles, total_fusion_events, total_fusion_pairs
    global live_d_particles, live_t_particles

    total_cycles += 1

    if len(plasma) < 2:
        print("INAPPROPRIATE PARTICLES")
        return

    p1 = random.choice(plasma)
    p2 = random.choice(plasma)

    if (p1["particle_type"] == "deuterium" and p2["particle_type"] == "tritium") or \
       (p1["particle_type"] == "tritium" and p2["particle_type"] == "deuterium"):

        print("APPROPRIATE PARTICLES")
        total_fusion_pairs += 1

        if p1["particle_energy"] + p2["particle_energy"] > boltzmann_constant:
            print("FUSION SUCCESSFUL")
            total_fusion_events += 1

            plasma.remove(p1)
            plasma.remove(p2)

            if p1["particle_type"] == "deuterium":
                live_d_particles -= 1
                live_t_particles -= 1
            else:
                live_t_particles -= 1
                live_d_particles -= 1

            plasma.append({"particle_type": "helium", "particle_energy": 3.5})
            SIMULATE_NEUTRON()
        else:
            print("FUSION FAILED")
    else:
        print("INAPPROPRIATE PARTICLES")


def SIMULATE_NEUTRON():
    global reactor_wall_neutron_energy

    neutron_total_energy = 14.1
    plasma_fraction = 0.8
    wall_fraction = 0.2

    plasma_energy = neutron_total_energy * plasma_fraction
    wall_energy = neutron_total_energy * wall_fraction

    particles_recieving_neutronenergy = 5
    energy_per_particle = plasma_energy / particles_recieving_neutronenergy

    for i in range(particles_recieving_neutronenergy):
        if plasma:
            random_particle = random.choice(plasma)
            random_particle["particle_energy"] += energy_per_particle

    reactor_wall_neutron_energy += wall_energy


def FUSION_VIABILITY():
    if live_d_particles == 0 or live_t_particles == 0:
        return False

    for particle_d in plasma:
        if particle_d["particle_type"] == "deuterium":
            for particle_t in plasma:
                if particle_t["particle_type"] == "tritium":
                    if particle_d["particle_energy"] + particle_t["particle_energy"] > boltzmann_constant:
                        return True
    return False


def main():
    INITIALISE_PLASMA()

    while FUSION_VIABILITY():
        RUN_PLASMA()

    print("Total Deuterium:", total_d_particles)
    print("Total Tritium:", total_t_particles)
    print("Total Cycles:", total_cycles)
    print("Total Fusion Events:", total_fusion_events)
    print("Total Fusion Pairs:", total_fusion_pairs)
    print("Reactor Wall Neutron Energy:", reactor_wall_neutron_energy)


if __name__ == "__main__":
    main()