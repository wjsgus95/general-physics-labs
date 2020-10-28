import sys

from math import pi, pow, sqrt
from typing import DefaultDict, List, Callable, Tuple
from collections import defaultdict

import matplotlib.pyplot as plt

# Type list of tuples (pos, magnetic_field)
Pairs = List[Tuple[float, float]]
# Type defaultdict of pos -> magnetic_field
Pos2Magnet = DefaultDict[float, float]

## Constants.
FIGURE_DIR = 'figures/'
# Current
I1 = 5.0
I2 = 5.0
I3 = 0.101
# Radii
radius_a = 0.03
radius_b = 0.04
# Solenoid
L = 0.13
a = 0.0195
N = 2900
n = N / L
# Others
pos_bias = 8.5 * (10 ** -3)
permeability = 4 * pi * (10 ** -7)


# Parse input given filename.
def parse_data(filename: str) -> Pos2Magnet:
    pairs = defaultdict(list)

    # Convert input string to float and map position and magnet read.
    with open(filename, 'r') as f:
        row = 0
        for line in f.readlines()[1:]:
            row += 1
            nums = line.split()
            for i in range(0, len(nums), 2):
                # Seems CAPSTONE has some issues with exporting data.
                try:
                    pos, mag = float(nums[i]), float(nums[i+1])
                    pairs[pos + pos_bias].append(mag)
                except IndexError:
                    pass

    # Reduce to average for multiple key-value pairs.
    for pos in pairs:
        pairs[pos] = sum(pairs[pos]) / len(pairs[pos])
    
    return pairs


# Expr 1
def get_B_linear(pos: float) -> float:
    top = permeability * I1
    bottom = 2 * pi * pos
    return top / bottom


# Expr 2 - A
def get_B_circular_a(pos: float) -> float:
    pos -= 0.06
    top = permeability * I2 * (radius_a ** 2)
    bottom = 2 * pow((pos ** 2) + (radius_a ** 2), 1.5)
    return top / bottom


# Expr 2 - B
def get_B_circular_b(pos: float) -> float:
    pos -= 0.06
    top = permeability * I2 * (radius_b ** 2)
    bottom = 2 * pow((pos ** 2) + (radius_b ** 2), 1.5)
    return top / bottom


# Expr 3
def get_B_solenoid(pos: float) -> float:
    pos += 0.065
    part1 = 0.5 * permeability * n * I3
    part2 = pos / sqrt((pos**2) + (a**2))
    part3 = (L - pos) / sqrt(((L - pos) ** 2) + (a ** 2))
    return part1 * (part2 + part3)


# Return one expected and one measured plot.
def get_plots(pairs: Pos2Magnet, predict: Callable) -> [Pairs, Pairs]:
    expected = []
    measured = []

    for pos in pairs:
        expected.append((pos, predict(pos)))
        measured.append((pos, pairs[pos]))
    
    expected.sort()
    measured.sort()

    return expected, measured
    

# Plot a session and save the figures.
def plot(expected: Pairs, measured: Pairs, session: str, plot_lim: List[Tuple]):
    plt.clf()
    figure = plt.figure(figsize=(9, 4))

    plt.subplot(1, 2, 1)
    plt.title('Expected')
    plt.xlabel('Distance (m)')
    plt.ylabel('Magnetic Field (T)')
    plt.xlim(*plot_lim[0])
    plt.ylim(*plot_lim[1])

    plt.plot(*zip(*expected))

    plt.subplot(1, 2, 2)
    plt.title('Measured')
    plt.xlabel('Distance (m)')
    plt.ylabel('Magnetic Field (T)')
    plt.xlim(*plot_lim[0])
    plt.ylim(*plot_lim[1])
    plt.plot(*zip(*measured))

    figure.tight_layout()
    plt.savefig(FIGURE_DIR + session + '.png')


# Session parameters
sessions = ['expt1', 'expt2_a', 'expt2_b', 'expt3']
plot_lims = [
    [(0, 0.15), (0, 0.00013)],
    [(0, 0.15), (0, 0.0002)],
    [(0, 0.15), (0, 0.00015)],
    [(0, 0.15), (0, 0.003)],
]
get_Bs = [get_B_linear, get_B_circular_a, get_B_circular_b, get_B_solenoid]

# Drives analysis.
for session, get_B, plot_lim in zip(sessions, get_Bs, plot_lims):
    pairs = parse_data(session + '.txt')

    expected, measured = get_plots(pairs, get_B)

    plot(expected, measured, session, plot_lim)



    

