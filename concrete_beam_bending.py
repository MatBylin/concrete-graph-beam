import math


class ConcreteBeamBending:
    def __init__(self, fcd, fyd, fctm):
        self.fcd = fcd
        self.fyd = fyd
        self.fctm = fctm

    def calculate_bend(self, my, b, d, a, n):
        ks = 0.000001 * b * d * d * self.fcd
        ni = my / ks
        x = 1 - 2 * ni
        if x <= 0:
            x = 0
        y = math.sqrt(x)
        range_of_compression = 1 - y
        range_of_compression_lim = 0.493

        if range_of_compression < range_of_compression_lim:
            ramie_sil = (1 - 0.5 * range_of_compression) * d
            as1 = 10000 * my / (ramie_sil * self.fyd)
            as2 = 0

        else:
            mrd = 0.3715 * b * d * d * self.fcd * n * 0.000001
            as2 = (my - mrd) / ((d - a) * self.fyd) * 10000
            as1 = (mrd / (0.7535 * d * self.fyd)) * 10000 + as2

        as1 = round(as1, 2)
        as2 = round(as2, 2)

        if ni > 0.50:
            as1 = 0
            as2 = 0
            # warning = "error calculation"

        asmin = max(0.01 * 0.0013 * b * d, 0.10 * 0.26 * self.fctm / (self.fyd * 1.4))

        return as1, as2, asmin
