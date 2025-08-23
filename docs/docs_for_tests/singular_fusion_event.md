17/08/25
The goal in this test is to "Simulate a singular fusion event". At definition, nuclear fusion is a reaction in which two or more nuclei collide with sufficient energy to fuse, releasing more energy in the process. This means we need to simulate:
- Two or more nuclei (we will be using two for D-T fusion) with energy (assigned in a list)
- A reaction occuring (a check whether they are the correct kinds of particles with sufficient energy)
- Products being formed (assigned to a list and energy as a variable)

The following could be written as below in plain english pseudocode

SET_VARIABLE boltzmann_constant
CREATE_DICTIONARY plasma WITH particle_type AND particle_energy

FOR i IN RANGE 2
    IF random_number = 1 THEN:
        APPEND "deuterium", energy*0.75-1.25x #NOTE: Adding variability in temperature
    ELSE:
        APPEND "tritium", energy*0.75-1.25x

IF POSITION 1 OF plasma = "deuterium" AND POSITION 2 OF plasma = "tritium" THEN: #NOTE: Or vice versa added too
    print("APPROPRIATE PARTICLES")
    IF POSITION 1 OF plasma particle_energy + POSITION 2 OF plasma particle_energy > boltzmann_constant THEN:
        print("FUSION SUCCESSFUL")
        CLEAR_DICTIONARY plasma
        APPEND "helium", energy 3.5MeV
        APPEND "neutron", energy 14.1MeV
    ELSE:
        print("FUSION FAILED")
ELSE:
    print("INAPPROPRIATE PARTICLES")

----------------------------------------------------------------------------------------------------------------------------------

23/08/25
I revisited this code and finished it up, below is the code copied from singular_fusion_event.py along with explanations of my own code:

----------------------------------------------------------------------------------------------------------------------------------

import random

boltzmann_constant = 1.380649e-23 # J/K

energy = boltzmann_constant / 2

plasma = []

### The Boltzmann constant has been defined, energy has been set to half to allow fusion failures with later variability, Plasma list created ###

for i in range(2):
    rnd = random.randint(0, 1)
    particle_type = "deuterium" if rnd == 1 else "tritium"
    variability = random.uniform(0.75, 1.25)
    particle_energy = energy * variability
    plasma.append({"particle_type": particle_type, "particle_energy": particle_energy})

### Two random particles generated from integer 0 or 1 twice. Energy is added with variability defined above for easy fusion failure/success parameter modification ###

print("Selected particles:")
print(" -", plasma[0]["particle_type"], f"{plasma[0]['particle_energy']:.3e}")
print(" -", plasma[1]["particle_type"], f"{plasma[1]['particle_energy']:.3e}")

### Little log dump here ###

types = {plasma[0]["particle_type"], plasma[1]["particle_type"]}
if types == {"deuterium", "tritium"}:
    print("APPROPRIATE PARTICLES")
    total_energy = plasma[0]["particle_energy"] + plasma[1]["particle_energy"]

### First checks for a D-T (or vice versa) pair

    if total_energy > boltzmann_constant:
        print("FUSION SUCCESSFUL")
        plasma = []
        plasma.append({"particle_type": "helium", "particle_energy": 3.5})
        plasma.append({"particle_type": "neutron", "particle_energy": 14.1})

        print("Products:")
        print(" -", plasma[0]["particle_type"], f"{plasma[0]['particle_energy']:.3e}")
        print(" -", plasma[1]["particle_type"], f"{plasma[1]['particle_energy']:.3e}")

### Checks if enough energy, removes used particles and adds waste particles into plasma ###
### NOTE - SUCH A MECHANIC WILL BE KEY IN THE MAIN PLASMA SIMULATION LATER ###

    else:
        print("FUSION FAILED")
else:
    print("INAPPROPRIATE PARTICLES")

### Else dependencies ###