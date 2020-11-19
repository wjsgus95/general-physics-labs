
import sys

from parser import parse
from plotter import Plotter2D
from predictions import expt1_capacitor_C1, expt1_resistor_C1
from predictions import expt1_capacitor_C2, expt1_resistor_C2

from common import FIGURE_DIR

if __name__ == "__main__":
    data_model = parse(sys.argv[1])

    plt = Plotter2D(expt1_capacitor_C1, data_model['330uF+100ohm']['Voltage-A'])
    plt.set_xlabel('Time (s)')
    plt.set_ylabel('Voltage (V)')
    plt.plot(FIGURE_DIR + 'E1_C330_Capacitor.png')

    plt = Plotter2D(expt1_resistor_C1, data_model['330uF+100ohm']['Voltage-B'])
    plt.set_xlabel('Time (s)')
    plt.set_ylabel('Voltage (V)')
    plt.plot(FIGURE_DIR + 'E1_C330_Resistor.png')

    plt = Plotter2D(expt1_capacitor_C2, data_model['100uF+100ohm']['Voltage-A'])
    plt.set_xlabel('Time (s)')
    plt.set_ylabel('Voltage (V)')
    plt.plot(FIGURE_DIR + 'E1_C100_Capacitor.png')

    plt = Plotter2D(expt1_resistor_C2, data_model['100uF+100ohm']['Voltage-B'])
    plt.set_xlabel('Time (s)')
    plt.set_ylabel('Voltage (V)')
    plt.plot(FIGURE_DIR + 'E1_C100_Resistor.png')
