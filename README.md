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


### The algorithm
The Lorenz set of ordinary differential equations (ODE) does not have an analytical solution and therefore a way to simulate it is by using numerical methods. In this assignment, the Euler method is used to simulate the Lorenz system. The Euler method is a first-order numerical procedure for solving ordinary differential equations with a given initial value.

The Euler method is based on the following equation:

$$ \frac{dy}{dt} \approx \frac{y(t+\delta t)-y(t)}{\delta t} $$

where $$ \delta t $$ is the time step. 

Applying the Euler method to the Lorenz system, the following equations are obtained:

$$ x_{n+1} = x_n + \sigma \delta t (y_n - x_n) $$
$$ y_{n+1} = y_n + \delta t (x_n (\rho - z_n) - y_n) $$
$$ z_{n+1} = z_n + \delta t (x_n y_n - \beta z_n) $$

where $$ x_n $$, $$ y_n $$, and $$ z_n $$ are the values of $$ x $$, $$ y $$, and $$ z $$ at time $$ t_n $$, respectively.

A pseudo code of the algorithm is shown below:

```python
# Initialize
x = 1
y = 1
z = 1
sigma = 10
beta = 8/3
rho = 6
dt = 0.01
N = 5000

# Loop
for i in range(N):
    x = x + sigma * dt * (y - x)
    y = y + dt * (x * (rho - z) - y)
    z = z + dt * (x * y - beta * z)
```


### Code Considerations
In this assignement, I tried to follow the best practices for object-oriented programming. In the `lorenz` module, there is a `Lorenz` class (in `lorenz.py`) that contains all the methods and attributes for simulating the Lorenz system. The `Lorenz` class has the following methods:

- `__init__`: The constructor of the class. It initializes the attributes of the class, such as the initial conditions, the parameters, and the time step.
- `step_euler`: This method takes a step in forward in time, specified by `dt` using the Euler method.
- `solve`: This method solves the Lorenz system for a given number of steps, specified by `N`. As an argument it takes a method that specifies the numerical method to be used. The default method is the Euler method. When calling `solve`, the object keeps a `history` attribute, which is a list of all the states of the system. The `history` attribute can later be used to plot the results.

Another file in the `lorenz` module is `plot_lorenz.py`, which contains three functions for plotting the results. The `plot_lorenz3D` function plots the 3D trajectory of the system. The `plot_lorenz2D` function plots the 2D projection of the trajectory on the XY, XZ, and YZ plane. Lastly, there is a `animate_lorenz` function that creates an animation of the trajectory. All functions take the `Lorenz` object as input.

All functions and object methods have been tested in the `tests/test_lorenz.py` file. The tests are run using `pytest` and can be run with the following command:

```bash
pytest
```

Furthermore, functions, methods, and class are documented with a `docstring` and are type hinted. This makes the code more readable and easier to use. All variables are defined to avoid global variables interfering with the code.