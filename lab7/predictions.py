from math import exp

E1_V0 = 4.0
E1_R = 100
E1_C1 = 330 * (10 ** -6)
E1_C2 = 100 * (10 ** -6)


# DC RC Circuit
def expt1_capacitor_C330(time: float):
    def charging(time: float):
        return E1_V0 * (1 - exp(- time / (E1_R * E1_C1)))

    def discharging(time: float):
        return E1_V0 * exp(- time / (E1_R * E1_C1))

    is_charging = (time % 1) >= 0.5
    base = time - time % 0.5
    t = time - base
    return charging(t) if is_charging else discharging(t)


# DC RC Circuit
def expt1_resistor_C330(time: float):
    def charging(time: float):
        return E1_V0 * exp(- time / (E1_R * E1_C1))

    def discharging(time: float):
        return - E1_V0 * exp(- time / (E1_R * E1_C1))

    is_charging = (time % 1) >= 0.5
    base = time - time % 0.5
    t = time - base
    return charging(t) if is_charging else discharging(t)


# DC RC Circuit
def expt1_capacitor_C100(time: float):
    def charging(time: float):
        return E1_V0 * (1 - exp(- time / (E1_R * E1_C2)))

    def discharging(time: float):
        return E1_V0 * exp(- time / (E1_R * E1_C2))

    is_charging = (time % 1) >= 0.5
    base = time - time % 0.5
    t = time - base
    return charging(t) if is_charging else discharging(t)


# DC RC Circuit
def expt1_resistor_C100(time: float):
    def charging(time: float):
        return E1_V0 * exp(- time / (E1_R * E1_C2))

    def discharging(time: float):
        return - E1_V0 * exp(- time / (E1_R * E1_C2))

    is_charging = (time % 1) >= 0.5
    base = time - time % 0.5
    t = time - base
    return charging(t) if is_charging else discharging(t)


# DC RL Circuit
def expt2_inductor_L178(time: float):
    def charging(time: float):
        return E1_V0 * exp(- time / (E1_R * E1_C1))

    def discharging(time: float):
        return - E1_V0 * exp(- time / (E1_R * E1_C1))

    is_charging = (time % 1) >= 0.5
    base = time - time % 0.5
    t = time - base
    return charging(t) if is_charging else discharging(t)