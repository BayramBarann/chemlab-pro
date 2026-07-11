from chemistry.constants import R_ATM
from chemistry.gas_database import VAN_DER_WAALS_CONSTANTS


def calculate_pressure(n, volume, temperature, a, b):
    if volume <= n * b:
        raise ValueError("Volume must be greater than n * b for the van der Waals equation.")
    return (n * R_ATM * temperature) / (volume - n * b) - (a * n * n) / (volume * volume)


def calculate_temperature(pressure, volume, n, a, b):
    if volume <= n * b:
        raise ValueError("Volume must be greater than n * b for the van der Waals equation.")
    return ((pressure + (a * n * n) / (volume * volume)) * (volume - n * b)) / (n * R_ATM)


def _vdw_pressure_residual(volume, pressure, n, temperature, a, b):
    return calculate_pressure(n, volume, temperature, a, b) - pressure


def calculate_volume(pressure, n, temperature, a, b, max_iterations=100, tolerance=1e-7):
    if pressure <= 0:
        raise ValueError("Pressure must be greater than zero.")
    if temperature <= 0:
        raise ValueError("Temperature must be greater than zero.")
    lower = n * b * 1.000001
    ideal_volume = (n * R_ATM * temperature) / pressure
    upper = max(ideal_volume * 10, lower + 1.0)
    lower_residual = _vdw_pressure_residual(lower, pressure, n, temperature, a, b)
    upper_residual = _vdw_pressure_residual(upper, pressure, n, temperature, a, b)

    for _ in range(max_iterations):
        if lower_residual == 0:
            return lower
        if upper_residual == 0:
            return upper
        if lower_residual * upper_residual < 0:
            break
        upper *= 2
        upper_residual = _vdw_pressure_residual(upper, pressure, n, temperature, a, b)
    else:
        raise ValueError("Unable to bracket a valid volume solution.")

    for _ in range(max_iterations):
        midpoint = (lower + upper) / 2
        mid_residual = _vdw_pressure_residual(midpoint, pressure, n, temperature, a, b)
        if abs(mid_residual) < tolerance:
            return midpoint
        if lower_residual * mid_residual < 0:
            upper = midpoint
            upper_residual = mid_residual
        else:
            lower = midpoint
            lower_residual = mid_residual
    raise ValueError("Volume solution did not converge.")


def _vdw_moles_residual(moles, pressure, volume, temperature, a, b):
    if volume <= moles * b:
        return float('inf')
    return calculate_pressure(moles, volume, temperature, a, b) - pressure


def calculate_moles(pressure, volume, temperature, a, b, max_iterations=100, tolerance=1e-7):
    if pressure <= 0:
        raise ValueError("Pressure must be greater than zero.")
    if volume <= 0:
        raise ValueError("Volume must be greater than zero.")
    if temperature <= 0:
        raise ValueError("Temperature must be greater than zero.")

    lower = 1e-9
    upper = min(volume / b * 0.999999, max((pressure * volume) / (R_ATM * temperature) * 10, 1.0))
    lower_residual = _vdw_moles_residual(lower, pressure, volume, temperature, a, b)
    upper_residual = _vdw_moles_residual(upper, pressure, volume, temperature, a, b)

    if upper_residual == float('inf'):
        upper = volume / b * 0.999
        upper_residual = _vdw_moles_residual(upper, pressure, volume, temperature, a, b)

    for _ in range(max_iterations):
        if lower_residual == 0:
            return lower
        if upper_residual == 0:
            return upper
        if lower_residual * upper_residual < 0:
            break
        upper = min(upper * 2, volume / b * 0.999999)
        upper_residual = _vdw_moles_residual(upper, pressure, volume, temperature, a, b)
        if upper_residual == float('inf'):
            break
    else:
        raise ValueError("Unable to bracket a valid moles solution.")

    for _ in range(max_iterations):
        midpoint = (lower + upper) / 2
        mid_residual = _vdw_moles_residual(midpoint, pressure, volume, temperature, a, b)
        if abs(mid_residual) < tolerance:
            return midpoint
        if lower_residual * mid_residual < 0:
            upper = midpoint
            upper_residual = mid_residual
        else:
            lower = midpoint
            lower_residual = mid_residual
    raise ValueError("Moles solution did not converge.")


def get_vdw_constants(gas_symbol):
    return VAN_DER_WAALS_CONSTANTS[gas_symbol]


def get_available_gases():
    return list(VAN_DER_WAALS_CONSTANTS.items())
