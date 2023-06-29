import os
from lorenz.lorenz import Lorenz
from lorenz.plot_lorenz import plot_lorenz2D, plot_lorenz3D, animate_lorenz
import h5py
import datetime

initial_conditions = [1, 1, 1]

cases = {
    1: {
        "initial_conditions": initial_conditions,
        "sigma": 10,
        "beta": 8 / 3,
        "rho": 6,
        "method": ["euler"],
    },
    2: {
        "initial_conditions": initial_conditions,
        "sigma": 10,
        "beta": 8 / 3,
        "rho": 16,
        "method": ["euler"],
    },
    3: {
        "initial_conditions": initial_conditions,
        "sigma": 10,
        "beta": 8 / 3,
        "rho": 28,
        "method": ["euler"],
    },
    4: {
        "initial_conditions": initial_conditions,
        "sigma": 14,
        "beta": 8 / 3,
        "rho": 28,
        "method": ["euler"],
    },
    5: {
        "initial_conditions": initial_conditions,
        "sigma": 14,
        "beta": 13 / 3,
        "rho": 28,
        "method": ["euler"],
    },
}


def main(case: dict):
    """
    Call the lorenz attractor with different initial conditions and save the
    resulting plots and data to a new folder.
    """

    if not os.path.exists("results"):
        os.mkdir("results")

    for key, value in case.items():
        # Create a new folder for each case

        if not os.path.exists(f"results/case_{key}"):
            os.mkdir(f"results/case_{key}")

        # Create a new Lorenz object
        lorenz = Lorenz(
            initial_state=value["initial_conditions"],
            sigma=value["sigma"],
            beta=value["beta"],
            rho=value["rho"],
        )

        for method in value["method"]:
            # Run the simulation
            lorenz.solve(method=method)

            # Plot the results
            plot_lorenz3D(lorenz, filename=f"results/case_{key}/lorenz3D_{method}.png")
            plot_lorenz2D(lorenz, filename=f"results/case_{key}/lorenz2D_{method}.png")
            # animate_lorenz(lorenz, filename=f"results/case_{key}/lorenz_{method}.gif")

            # Save the data
            with h5py.File(f"results/case_{key}/lorenz.h5", "w") as f:
                f.create_dataset(f"data_{method}", data=lorenz.history)

        # Create a readme file
        with open(f"results/case_{key}/README.md", "w") as f:
            f.write(f"# Case {key}\n")
            f.write(f"Run on {datetime.datetime.now()}\n\n")

            f.write("## Parameters\n")
            f.write(f"Initial conditions: {value['initial_conditions']}\n")
            f.write(f"Sigma: {value['sigma']}\n")
            f.write(f"Beta: {value['beta']}\n")
            f.write(f"Rho: {value['rho']}\n")

            for method in value["method"]:
                f.write(f"## Results\n")
                f.write(f"Method: {value['method']}\n")

                f.write("\n\n")

                f.write(f"![Lorenz 3D](lorenz3D_{method}.png)\n")
                # f.write(f"![Lorenz animation](lorenz_{method}.gif)\n")
                f.write(f"![Lorenz 2D](lorenz2D_{method}.png)\n")


if __name__ == "__main__":
    main(cases)
