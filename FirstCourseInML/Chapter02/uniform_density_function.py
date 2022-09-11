import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Calculates the variance from some randomly generated points from the PDF.
    The plot shows the variance converging on 1/3, which aligns with an
    analytical viewpoint.
    """
    # Uniform PDF parameters
    a, b = 0, 1
    r = (b - a) ** -1

    to_plot = np.zeros(shape=(100, 2))
    for i, samples in enumerate(np.logspace(0, 5, 100)):
        samples = int(samples)
        random = np.random.uniform(a, b, samples)
        random *= random

        to_plot[i, 0] = samples
        to_plot[i, 1] = np.sum(random) / samples

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(to_plot[:, 0], to_plot[:, 1])
    ax.set_xscale("log")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Variance")


    plt.show()

if __name__ == "__main__":
    main()