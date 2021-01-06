# NickSookhoo
# plot_multigraphs.py

import matplotlib.pyplot as plt

import plot_parabola_NEW
import plot_polynomial_edits
import plot_rings_edits
import plot_rose_curves_edits


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2)

    ax = fig.add_subplot(gs[0, 0])
    plot_parabola_NEW.plot(ax)

    ax = fig.add_subplot(gs[0, 1])
    plot_polynomial_edits.plot(ax)

    ax = fig.add_subplot(gs[1, 0])
    plot_rings_edits.plot(ax)

    ax = fig.add_subplot(gs[1, 1], projection='polar')
    plot_rose_curves_edits.plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
