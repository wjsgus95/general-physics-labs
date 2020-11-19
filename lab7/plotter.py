
import matplotlib.pyplot as plt

from typing import Callable
from schemas import DataSubSet


# Plot 2D data.
class Plotter2D:
    def __init__(self, predict: Callable, data: DataSubSet):
        self.xlabel = str()
        self.yalbel = str()

        self.measured = data.rows
        expected = []
        for x, y in data.rows:
            expected.append((x, predict(x)))
        self.expected = expected

    def set_xlabel(self, label: str):
        self.xlabel = label

    def set_ylabel(self, label: str):
        self.ylabel = label

    def plot(self, outpath: str):
        plt.clf()
        figure = plt.figure(figsize=(9, 4))

        ax = plt.subplot(1, 2, 1)
        plt.title("Expected")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(*zip(*self.expected))

        plt.subplot(1, 2, 2, sharex=ax, sharey=ax)
        plt.title("Measured")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(*zip(*self.measured))

        figure.tight_layout()
        plt.savefig(outpath)

