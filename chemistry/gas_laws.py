def calculate_pressure(volume, moles, temperature):
    from chemistry.constants import R_ATM
    pressure = (moles * R_ATM * temperature) / volume
    return pressure
def calculate_volume(pressure, moles, temperature):
    from chemistry.constants import R_ATM
    volume = (moles * R_ATM * temperature) / pressure
    return volume
def calculate_moles(pressure, volume, temperature):
    from chemistry.constants import R_ATM
    moles = (pressure * volume) / (R_ATM * temperature)
    return moles