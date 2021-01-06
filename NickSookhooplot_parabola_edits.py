# plot_parabola_new.py


import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    x = np.linspace(-4, 5, 100)
    y = np.power(x, 2) + 1

    # Step 1 - Plot graph
    ax.plot(x, y)

    # Step 2 - Graph has title
    ax.set_title("$y = x^2+1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Step 3 - Center the graph
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 30)

    # Step 4 - Add decor
    ax.grid()
    ax.plot(0, 1, color='red', marker='o')
    ax.axhline(1, color='gray', linestyle='--')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
