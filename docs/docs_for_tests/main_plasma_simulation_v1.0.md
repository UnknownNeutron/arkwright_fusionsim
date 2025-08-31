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

----------------------------------------------------------------------------------------------------------------------------------

28/08/25
Finished the pseudocode and writing the main code. I'm noticing pseudocode to normal code is a very efficient workflow since I know what to look up and learn. Lists have definitely been the hardest, and the little python tidbits like __name__ == "__main__"

----------------------------------------------------------------------------------------------------------------------------------

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

### Initialisation of variables

def INITIALISE_PLASMA():
    global total_d_particles, total_t_particles, live_d_particles, live_t_particles

### Sets everything needed as a global variable

for i in range(10000):

### Creates as many particles as in loop

        if random.randint(0, 1) == 1:
            variability = random.uniform(0.75, 1.25)
            particle_energy = energy * variability
            plasma.append({"particle_type": "deuterium", "particle_energy": particle_energy})

### Previous particle generation code reused since it's functional

            total_d_particles += 1
            live_d_particles = total_d_particles

### Tracking how many particles created for logs and fusion viability (running out)

        else:
            variability = random.uniform(0.75, 1.25)
            particle_energy = energy * variability
            plasma.append({"particle_type": "tritium", "particle_energy": particle_energy})
            total_t_particles += 1
            live_t_particles = total_t_particles

### Same as before


def RUN_PLASMA():
    global total_cycles, total_fusion_events, total_fusion_pairs
    global live_d_particles, live_t_particles

### Defines globally variables needed for fusion

    total_cycles += 1

### Counts as total cycle

    if len(plasma) < 2:
        print("INAPPROPRIATE PARTICLES")
        return

### Stops fusion if length of list is <2 - if fusion is impossible

    p1 = random.choice(plasma)
    p2 = random.choice(plasma)

### 2 particles chosen in local variables for convenience

    if (p1["particle_type"] == "deuterium" and p2["particle_type"] == "tritium") or \
       (p1["particle_type"] == "tritium" and p2["particle_type"] == "deuterium"):

### Vice versa code reused

        print("APPROPRIATE PARTICLES")
        total_fusion_pairs += 1

### Logging for total pairs

        if p1["particle_energy"] + p2["particle_energy"] > boltzmann_constant:
            print("FUSION SUCCESSFUL")
            total_fusion_events += 1

### Main fusion magic happens here w/ logging

            plasma.remove(p1)
            plasma.remove(p2)

            if p1["particle_type"] == "deuterium":
                live_d_particles -= 1
                live_t_particles -= 1

### More logging

            else:
                live_t_particles -= 1
                live_d_particles -= 1

            plasma.append({"particle_type": "helium", "particle_energy": 3.5})
            SIMULATE_NEUTRON()

### Code to handle neutron included (since neutrons are neutral and no sense keeping them in plasma)

        else:
            print("FUSION FAILED")
    else:
        print("INAPPROPRIATE PARTICLES")


def SIMULATE_NEUTRON():
    global reactor_wall_neutron_energy

### Defines global variable - how much energy the wall recieves

    neutron_total_energy = 14.1
    plasma_fraction = 0.8
    wall_fraction = 0.2

### Energies in MeV with fractions for ability to tweak later (educational aspect!!!)

    plasma_energy = neutron_total_energy * plasma_fraction
    wall_energy = neutron_total_energy * wall_fraction

### This is like the variability code but for energy

    particles_recieving_neutronenergy = 5
    energy_per_particle = plasma_energy / particles_recieving_neutronenergy

### More tweakability!!!

    for i in range(particles_recieving_neutronenergy):
        if plasma:
            random_particle = random.choice(plasma)
            random_particle["particle_energy"] += energy_per_particle

    reactor_wall_neutron_energy += wall_energy

### Handles the rest


def FUSION_VIABILITY():
    if live_d_particles == 0 or live_t_particles == 0:
        return False

### If fusable paricles have run out, fusion is not viable

    for particle_d in plasma:
        if particle_d["particle_type"] == "deuterium":
            for particle_t in plasma:
                if particle_t["particle_type"] == "tritium":
                    if particle_d["particle_energy"] + particle_t["particle_energy"] > boltzmann_constant:
                        return True
    return False

### If pairs left are correct and have enough energy fusion is viable!!! 


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

### Logdump of all data (Next release will use Matplotlib for better visibility)


if __name__ == "__main__":
    main()