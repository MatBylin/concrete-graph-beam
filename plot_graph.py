import matplotlib.pyplot as plt


def plot_graph(asd, asg, amin, d, fcd, fyd, m, b, a):
    plt.plot(d, asd, label="zbrojenie rozciągane")
    plt.plot(d, asg, label="zbrojenie ściskane")
    plt.plot(d, amin, label="zbrojenie minimalne")
    plt.xlabel("przekrój {} x d [mm]".format(b))
    plt.ylabel('ilość zbrojenia belki [cm2]')
    plt.title(
        "Iteracja ilości zbrojenia belki zginanej momentem My= {} kNm"
        " \nBeton fcd= {} MPa, stal fyd= {} MPa, otulina a= {} mm"
        .format(m, fcd, fyd, a))
    plt.legend()
    plt.show()
