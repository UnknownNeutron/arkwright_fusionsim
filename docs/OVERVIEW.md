11/08/25:
In this project, I aim to create an educational nuclear fusion simulator aimed at A-Level/Undergraduate students. It will be programmed in Python for ease of coding and reading, it could be programmed in C++ for efficiency during running but that is impractical for a prototype project like this. It will differentiate from other fusion simulators by being easier to use and having the ability to extrapolate calculations on weaker hardware.
The project will be structured in different parts, as written below:

- Revise nuclear fusion at an A-Level/Undergraduate level
- Simulate a singular fusion event
- Simulate multiple isolated fusion events (generate particles with varying temperature values from a baseline e.g. 0.5x-1.5x)
- Gain cumulative statistics from isolated fusion events (e.g. total energy released in MeV, total fusion events)
- Simulate other isolated fusion products (helium nuclei, neutrons, etc)
- Simulate cumulative fusion events (produced energy affects other particles)
- Simulate sustaining fusion [MILESTONE]
- Simulate cumulative fusion with other fusion products affecting (e.g. helium buildup, neutron effects)

At this point, I will have coded a program that simulates a self-sustaining plasma that produces and interacts with it's products (e.g. possibly incorporating the triple-alpha process). We will move onto this being a reactor simulator.

- Research tokamak reactors - their construction, controllability, physics and conditions
- Simulate the environment of a reactor (particle presence, reactor wall temperature)
- Simulate the effect of a magnetic field on the heating of the reactor wall (via probability)
- Simulate the effect of the magnetic field on the plasma in the reactor (e.g. do magnetif fields affect neutron flux and effect of neutron flux on structural integrity) [MILESTONE]
- Program a GUI to display the data in a way that can be compared against current fusion simulators and reactors (e.g. matplotlib)
- Program a GUI to interact with the reactor and tweak settings in a way that is easy for the user to understand

The end result should be a nuclear fusion simulator based inside a tokamak reactor that can be easily tweaked and compared to real results.