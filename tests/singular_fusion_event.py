import random

boltzmann_constant = 1.380649e-23 # J/K

energy = boltzmann_constant / 2

plasma = []

for i in range(2):
    rnd = random.randint(0, 1)
    particle_type = "deuterium" if rnd == 1 else "tritium"
    variability = random.uniform(0.75, 1.25)
    particle_energy = energy * variability
    plasma.append({"particle_type": particle_type, "particle_energy": particle_energy})

print("Selected particles:")
print(" -", plasma[0]["particle_type"], f"{plasma[0]['particle_energy']:.3e}")
print(" -", plasma[1]["particle_type"], f"{plasma[1]['particle_energy']:.3e}")

types = {plasma[0]["particle_type"], plasma[1]["particle_type"]}
if types == {"deuterium", "tritium"}:
    print("APPROPRIATE PARTICLES")
    total_energy = plasma[0]["particle_energy"] + plasma[1]["particle_energy"]

    if total_energy > boltzmann_constant:
        print("FUSION SUCCESSFUL")
        plasma = []
        plasma.append({"particle_type": "helium", "particle_energy": 3.5})
        plasma.append({"particle_type": "neutron", "particle_energy": 14.1})

        print("Products:")
        print(" -", plasma[0]["particle_type"], f"{plasma[0]['particle_energy']:.3e}")
        print(" -", plasma[1]["particle_type"], f"{plasma[1]['particle_energy']:.3e}")
    else:
        print("FUSION FAILED")
else:
    print("INAPPROPRIATE PARTICLES")