# Scientific Computing using Python (2023)

This repository contains the code and documentation for simulating the Lorenz Attractor solutions to the Lorenz system. The assignment is a part of the course Scientific Computing using Python at Aalborg University. The code is implemented in Python 3.11.3 using anaconda 1.11.2. All code considerations and results can be found at the [assignment]().

## Installation

All code was developed in a docker container and vscode. To create all the figures and files for running the code, simply run the following command:

> This will firstly build the docker image and create the conda environment. This build process can take a long time. Secondly, the code will be run in the docker container.

```bash
docker build -f docker/Dockerfile -t scp_in_python ./docker
docker run -it --rm -v ${PWD}:/workspaces/Scientific_Computing_Lorenz -w /workspaces/Scientific_Computing_Lorenz scp_in_python /bin/bash -c "pytest && python3 main.py"
```

Alternatively, the code can be run locally with [anaconda](https://www.anaconda.com/). Firstly, to recreate the environment, run the following command:

```bash
conda env create -f docker/environment.yml
```

Then activate the environment with:

```bash
conda activate scip1
```

Finally, run the following command to create all the figures and files for running the code:

```bash
pytest && python3 main.py
```



## Assignment
The Lorenz attractor is a set of chaotic solutions to the Lorenz system, which is a system of ordinary differential equations first studied by Edward Lorenz in 1963. It's notable for its distinctive butterfly-like shape when visualized in three dimensions.

The Lorenz system is typically described by three differential equations. Letting X, Y, and Z be three dimensions, and letting sigma, beta, and rho be parameters, the Lorenz system can be represented as:

$$ \frac{dx}{dt} = \sigma(y-x) $$
$$ \frac{dy}{dt} = x(\rho-z)-y $$
$$ \frac{dz}{dt} = xy-\beta z $$

The Lorenz attractor itself is the set of the trajectories that, after a long enough time, are pulled into a type of equilibrium known as a "strange attractor". It forms a fractal structure in phase space, and is visualized in three dimensions typically as two lobes around which the trajectories circulate and endlessly switch back and forth.

Lorenz's discovery of this chaotic behavior was one of the first and is one of the most famous examples of deterministic chaos, chaos that arises not from randomness or noise, but from deterministic systems behaving in a non-periodic manner. As such, the Lorenz attractor has become an iconic figure in the study of chaotic systems.

![Lorenz Attractor](lorenz_attractor_2.gif)


