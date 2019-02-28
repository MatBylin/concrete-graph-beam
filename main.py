from prepare_data import *
from plot_graph import *

# # # D A T A # # # # #
# # # # # # # # # # # #
f_cd = 17.86  # [MPa]
f_yd = 435    # [MPa]
f_ctm = 2.6   # [MPa]
m = 200      # [kNm]
b = 240      # [mm]
a = 25       # [mm]
start = 325  # [mm]
stop = 1500  # [mm]
step = 25    # [mm]
# # # # # # # # # # # #


def main():

    asd, asg, amin, d = prepare_data(f_cd, f_yd, f_ctm, m, b, a, start, stop, step)
    plot_graph(asd, asg, amin, d, f_cd, f_yd, m, b, a)


if __name__ == "__main__":
    main()
