26/08/25
Back in England but my laptop short circuited while repairing a fan, continuing via remote repo on GitHub.

As quoted in 22-08-25.md:
### Project Convergence will manage to simulate sustaining fusion in one fell swoop by generating a plasma that interacts with itself and the surroundings and keeps itself up for a certain amount of cycles. 
This means that the code will have to:
- Generate a LARGE list of D & T particles with varying energy values
- Perform a fusion event on a pair, and remove the particles from the system
- Add a helium particle, and: 
- Simulate a neutron exerting the energy it has on other particles in the plasma and how much it would exert on the reactor wall before it exits and is deleted and recorded
- Loop the program until plasma failure and record statistics
The code should look like this in pseudocode:

SET_VARIABLE boltzmann_constant

SET_VARIABLE total_d_particles #NOTE: Self explanatory
SET_VARIABLE total_t_particles #NOTE: Self explanatory
SET_VARIABLE live_d_particles #NOTE: Particle count that decreases for fusion viability tracking
SET_VARIABLE live_t_particles #NOTE: Particle count that decreases for fusion viability tracking
SET_VARIABLE total_h_particles

SET_VARIABLE total_cycles = 0 #NOTE: How many times the simulation runs, regardless of fusion or not
SET_VARIABLE total_fusion_events = 0 #NOTE: How many times a FUSION SUCCESSFUL message would occur
SET_VARIABLE total_fusion_pairs = 0 #NOTE: How many times an APPROPRIATE PARTICLES message would occur

SET_VARIABLE reactor_wall_neutron_energy = 0

CREATE_DICTIONARY plasma WITH particle_type AND particle_energy

DEF INITIALISE_PLASMA:
    FOR i IN RANGE [SUPER_LARGE_NUMBER]
        IF random_number = 1 THEN:
            APPEND "deuterium", energy*0.75-1.25x
            total_d_particles = total_d_particles + 1
            live_d_particles = total_d_particles
        ELSE:
            APPEND "tritium", energy*0.75-1.25x
            total_t_particles = total_t_particles + 1
            live_t_particles = total_t_particles

DEF RUN_PLASMA
    total_cycles = total_cycles + 1
    IF POSITION RANDOM OF plasma = "deuterium" AND POSITION RANDOM OF plasma = "tritium" THEN: [Or vice versa added too]
        print("APPROPRIATE PARTICLES")
        total_fusion_pairs = total_fusion_pairs + 1
        IF POSITION 1 OF plasma particle_energy + POSITION 2 OF plasma particle_energy > boltzmann_constant THEN:
            print("FUSION SUCCESSFUL")
            total_fusion_events = total_fusion_events + 1
            REMOVE POSITION [whatever_was_used_for_deuterium] OF plasma
            REMOVE POSITION [whatever_was_used_for_tritium] OF plasma
            live_d_particles = live_d_particles - 1
            live_t_particles = live_t_particles - 1
            APPEND "helium", energy 3.5MeV
            total_h_particles = total_h_particles + 1
            FUNCTION SIMULATE_NEUTRON
        ELSE:
            print("FUSION FAILED")
    ELSE:
        print("INAPPROPRIATE PARTICLES")

DEF SIMULATE_NEUTRON
    neutron_total_energy = 14.1
    plasma_fraction = 0.8
    wall_fraction = 0.2

    plasma_energy = neutron_total_energy * plasma_fraction
    wall_energy = neutron_total_energy * wall_fraction

    particles_recieving_neutronenergy = 5
    energy_per_particle = plasma_energy / particles_recieving_neutronenergy

    FOR i IN RANGE [particles_recieving_neutronenergy]
        RANDOM_PARTICLE = RANDOM CHOICE FROM plasma
        RANDOM_PARTICLE energy = RANDOM_PARTICLE energy + energy_per_particle

    reactor_wall_neutron_energy = reactor_wall_neutron_energy + wall_energy

DEF FUSION_VIABILITY
    IF live_d_particles = 0 OR live_t_particles = 0 THEN:
        RETURN False #NOTE: No pairs found
    fusion_pair_found = False

    FOR each particle_d IN plasma WHERE particle_type = "deuterium":
        FOR each particle_t IN plasma WHERE particle_type = "tritium":
            IF particle_d.energy + particle_t.energy > boltzmann_constant THEN:
                fusion_pair_found = True
                BREAK
        IF fusion_pair_found = True THEN:
            BREAK

    IF fusion_pair_found = True THEN:
        RETURN True
    ELSE:
        RETURN False

def main():
    RUN INITIALISE_PLASMA
    WHILE FUSION_VIABILITY = True:
        RUN RUN_PLASMA
    

    print total_d_particles
    print total_t_particles
    print total_cycles
    print total_fusion_events
    print total_fusion_pairs
    print reactor_wall_neutron_energy
    print total_h_particles

if __name__ == "__main__":
    main()