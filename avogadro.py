import math
import stdio

if __name__ == '__main__':
    n = 0
    s = 0.00
    while not stdio.isEmpty():
        convert_to_m = stdio.readFloat() * (0.175 * (10 ** -6))  # Convert input parameters to meters
        s += convert_to_m ** 2
        n += 1  # count beads
        
    var = s / (2 * n)

    viscosity = 9.135 * 10 ** -4

    r_bead = 0.5 * 10 ** -6  # Radius of willow

    T = 297.0  # Absolute temperature

    R = 8.31446  # Global gas constant

    k = 6 * math.pi * var * viscosity * r_bead / T  # Boltzman
    Avogadro = R / k
    print('Boltzman = {0:.4e}'.format(k))
    print('Avogadro = {0:.4e}'.format(Avogadro))
