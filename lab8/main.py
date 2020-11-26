import matplotlib.pyplot as plt

from typing import List


def get_wavelength(d, m):
    def micro(x):
        return x * (10 ** -6)

    d = micro(d)
    return 2 * d / m


def set_legends(scatter_points: List):
    plt.legend(
        tuple(scatter_points),
        ("Trial 1", "Trial 2", "Trial 3", "Average", "Expected"),
        loc='lower right',
    )


m = 50  # number of fringes
d_red = [16.15, 16.4, 16.3]
d_green = [13.8, 13.7, 13.55]

red_wavelength = 650
green_wavelength = 532

if __name__ == "__main__":
    # Set title and axis labels.
    plt.title("Red Light")
    plt.xlabel('distance (µm)')
    plt.ylabel('wavelength (nm)')

    # Plot baseline.
    xlim = (16.1, 16.5)
    ylim = tuple((x * 40 for x in xlim))
    plt.plot(xlim, ylim)
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Scatter each measured point.
    points = []
    for i, d in enumerate(d_red):
        wavelength = get_wavelength(d, m)

        # Scale to plotting units.
        wavelength *= 10 ** 9

        print(d, wavelength)
        stub = plt.scatter(d, wavelength, label=f'Trial #{i+1}')
        points.append(stub)

    # Repeat for average d measured.
    avg_d = sum(d_red) / len(d_red)
    wavelength = get_wavelength(avg_d, m)
    wavelength *= 10 ** 9
    stub = plt.scatter(avg_d, wavelength, label='Average')
    points.append(stub)

    # Set theoretical point.
    real_d = red_wavelength / 40
    stub = plt.scatter(real_d, red_wavelength, label='Theoretical')
    points.append(stub)

    # Set legends and save figure.
    set_legends(points)
    plt.savefig('red_light.png')

    # Clear states.
    plt.clf()

    # Set plot title and axis labels.
    plt.title("Green Light")
    plt.xlabel('distance (µm)')
    plt.ylabel('wavelength (nm)')

    # Plot baseline.
    xlim = (13.2, 13.9)
    ylim = tuple((x * 40 for x in xlim))
    plt.plot(xlim, ylim)
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Scatter each measured point.
    points = []
    for i, d in enumerate(d_green):
        wavelength = get_wavelength(d, m)

        # Scale to plotting units.
        wavelength *= 10 ** 9

        print(d, wavelength)
        stub = plt.scatter(d, wavelength, label=f'Trial #{i+1}')
        points.append(stub)

    # Repeat for average d measured.
    avg_d = sum(d_green) / len(d_green)
    wavelength = get_wavelength(avg_d, m)
    wavelength *= 10 ** 9
    stub = plt.scatter(avg_d, wavelength, label='Average')
    points.append(stub)

    # Set theoretical point.
    real_d = green_wavelength / 40
    stub = plt.scatter(real_d, green_wavelength, label='Theoretical')
    points.append(stub)

    # Set legends and save figure.
    set_legends(points)
    plt.savefig('green_light.png')
