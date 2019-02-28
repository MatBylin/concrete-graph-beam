from concrete_beam_bending import *


def prepare_data(fcd, fyd, fctm, m, b, a, start, stop, step):
    beam = ConcreteBeamBending(fcd, fyd, fctm)
    asd = []
    asg = []
    amin = []
    d = []

    for i in range(start, stop, step):
        as1, as2, asmin = beam.calculate_bend(m, b, i, a, 1)
        asd.append(as1)
        asg.append(as2)
        amin.append(asmin)
        d.append(i)

    print("RAW DATA : ")
    print("Asd = {}".format(asd))
    print("Asg = {}".format(asg))
    print("d = {}".format(d))
    return asd, asg, amin, d



