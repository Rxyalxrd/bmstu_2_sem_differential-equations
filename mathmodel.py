import numpy as np
import matplotlib.pyplot as plt


class UraniumDecaySolver:
    def __init__(
            self, initial_uranium_mass, lead_mass,
            uranium_to_lead_ratio, half_life, time_step=1e6
    ):
        self.initial_uranium_mass = initial_uranium_mass
        self.lead_mass = lead_mass
        self.uranium_to_lead_ratio = uranium_to_lead_ratio
        self.half_life = half_life
        self.time_step = time_step
        self.decay_constant = -np.log(2) / half_life
        self.initial_uranium_mass_total = initial_uranium_mass + lead_mass * uranium_to_lead_ratio
        self.times = []
        self.uranium_masses = []

    def solve(self):
        time = 0
        uranium_mass = self.initial_uranium_mass_total
        self.times = [time]
        self.uranium_masses = [uranium_mass]

        while uranium_mass > self.initial_uranium_mass:
            uranium_mass += self.decay_constant * uranium_mass * self.time_step
            time += self.time_step
            self.times.append(time)
            self.uranium_masses.append(uranium_mass)

        return time

    def plot(self):
        plt.plot(self.times, self.uranium_masses, label="Uranium Mass")
        plt.axhline(
            y=self.initial_uranium_mass, color='r',
            linestyle='--', label="Current Uranium Mass"
        )
        plt.xlabel('Time (years)')
        plt.ylabel('Uranium Mass (mg)')
        plt.legend()
        plt.title('Uranium Decay Over Time')
        plt.show()


initial_uranium_mass = 100  # мг
lead_mass = 14  # мг
uranium_to_lead_ratio = 238 / 206
half_life = 4.5e9  # лет
time_step = 1e6  # шаг времени (1 миллион лет)

solver = UraniumDecaySolver(
    initial_uranium_mass, lead_mass,
    uranium_to_lead_ratio, half_life, time_step
)
age_of_rock = solver.solve()

print(f"Возраст горной породы: {age_of_rock:.2e} лет")
solver.plot()
