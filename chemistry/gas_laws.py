R = 0.082057 #L·atm·mol⁻¹·K⁻¹

def calculate_pressure(n, T, V):
    return (n * R * T) / V
def calculate_volume(n, T, P):
    return (n * R * T) / P
def calculate_temperature(n, P, V):
    return (P * V) / (n * R)
