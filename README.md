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

All tests follow the GIVEN, WHEN, THEN structure. An example of a GIVEN WHEN THEN example is shown below:

```python
def test_example():
    # GIVEN some condition
    # WHEN something is done
    # THEN this is expected

    ...
```



Furthermore, functions, methods, and class are documented with a `docstring` and are type hinted. This makes the code more readable and easier to use. All variables are defined to avoid global variables interfering with the code.


The `main.py` script contains the code to simulate all the parameter cases and plot the results. The script is run with the following command:

```bash
python3 main.py
```

The script creates a `results` folder, where all the results are saved. The results are saved in a `lorenz.h5` file and the figures are saved in a `png` file. Lastly, the script creates a `README.md` file, which specifies the initial state, the parameters used, the methods used, and the resulting 2D and 3D plots for running the code.


### Benchmarking
The code was benchmarked with `line_profiler`, which can be installed with the following command:

```bash
conda install line_profiler
```

To run the benchmark run the following command:

```bash
kernprof -l -v results/benchmark/benchmark.py
```

The results of the benchmark are shown below:

```bash
Total time: 0.096951 s
File: /workspaces/scientific_computing_in_python/Scientific_Computing_Lorenz/lorenz/lorenz.py
Function: solve at line 87

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    87                                               @profile
    88                                               def solve(self, method: str = "euler") -> List[Tuple[float, float, float]]:
    89                                                   """
    90                                                   Solves the Lorenz system for N time steps.
    91                                           
    92                                                   Parameters
    93                                                   ----------
    94                                                   method : str, optional
    95                                                       The integration method to use (either "euler" or "rk4").
    96                                                       Default is "euler".
    97                                           
    98                                                   Returns
    99                                                   -------
   100                                                   list of tuple of float
   101                                                       The state of the system (x, y, z) at each time step.
   102                                           
   103                                                   Examples
   104                                                   --------
   105                                                   >>> lorenz = Lorenz((0.0, 1.0, 1.05)).solve()
   106                                           
   107                                                   """
   108         3          1.3      0.4      0.0          if method not in ("euler", "rk4"):
   109                                                       raise ValueError('Method must be either "euler" or "rk4"')
   110                                           
   111         3          1.6      0.5      0.0          self.history = []  # Reset the history at the beginning of each simulation
   112         3          2.1      0.7      0.0          self.history.append(self.state)  # Record the initial state
   113                                           
   114     15000       2818.7      0.2      2.9          for _ in range(self.N):
   115     15000       2595.6      0.2      2.7              if method == "euler":
   116     15000      86313.2      5.8     89.0                  self.step_euler()
   117                                                       else:
   118                                                           self.step_rk4()
   119     15000       5217.9      0.3      5.4              self.history.append(self.state)  # Record the state after each step
   120                                           
   121         3          0.5      0.2      0.0          return self.history

Total time: 0.0286185 s
File: /workspaces/scientific_computing_in_python/Scientific_Computing_Lorenz/lorenz/lorenz.py
Function: step_euler at line 123

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   123                                               @profile
   124                                               def step_euler(self) -> Tuple[float, float, float]:
   125                                                   """
   126                                                   Advances the state of the system one time step using the Euler method.
   127                                           
   128                                                   Returns
   129                                                   -------
   130                                                   tuple of float
   131                                                       The new state of the system (x, y, z).
   132                                           
   133                                                   Examples
   134                                                   --------
   135                                                   lorenz = Lorenz((0.0, 1.0, 1.05)).step_euler()
   136                                                   """
   137     15001       5492.0      0.4     19.2          x, y, z = self.state
   138     15001       3799.5      0.3     13.3          dx = self.sigma * (y - x)
   139     15001       4087.1      0.3     14.3          dy = x * (self.rho - z) - y
   140     15001       4091.2      0.3     14.3          dz = x * y - self.beta * z
   141     15001       8140.6      0.5     28.4          self.state = x + dx * self.dt, y + dy * self.dt, z + dz * self.dt
   142     15001       3008.3      0.2     10.5          return self.state
```

The `step_euler` and `solve` methods takes about 0.1 seconds to simulate the Lorenz system, with a `dt=0.01` and `N=5000`. The most time consuming step is calculating euler, which in itself has a uniform distribution of compute time.


The plotting functions take more time to compute:

```bash
Total time: 10.5636 s
File: /workspaces/scientific_computing_in_python/Scientific_Computing_Lorenz/lorenz/plot_lorenz.py
Function: plot_lorenz3D at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           def plot_lorenz3D(lorenz: Lorenz, filename: str = None):
    26                                               """Plotting of the Lorenz system in 3D.
    27                                           
    28                                               This function takes a Lorenz object and plots the trajectory of the system
    29                                           
    30                                               Args:
    31                                                   lorenz (Lorenz): A Lorenz object
    32                                                   filename (str, optional): The filename to save the plot to. Defaults to None.
    33                                           
    34                                               Returns:
    35                                                   A plot of the trajectory of the Lorenz system in 3D
    36                                           
    37                                               """
    38                                           
    39                                               # Ensure the system has been solved before plotting
    40         1          0.9      0.9      0.0      if not lorenz.history:
    41         1      38097.0  38097.0      0.4          lorenz.solve()
    42                                           
    43                                               # Unpack the history into separate x, y, and z lists
    44         1        799.6    799.6      0.0      x, y, z = zip(*lorenz.history)
    45                                           
    46         1        657.6    657.6      0.0      fig = plt.figure()
    47         1      21871.8  21871.8      0.2      ax = fig.add_subplot(111, projection="3d")
    48                                           
    49                                               # Create a color array (from 0 to 1) one for each point in the trajectory
    50         1        192.7    192.7      0.0      colors = plt.cm.viridis(np.linspace(0, 1, len(x)))
    51                                           
    52                                               # Plot the trajectory with color corresponding to time
    53      5000       3519.2      0.7      0.0      for i in range(1, len(x)):
    54      5000    7109007.8   1421.8     67.3          ax.plot(x[i - 1 : i + 1], y[i - 1 : i + 1], z[i - 1 : i + 1], color=colors[i])
    55                                           
    56         1        104.9    104.9      0.0      ax.set_xlabel("X Axis")
    57         1         82.5     82.5      0.0      ax.set_ylabel("Y Axis")
    58         1         44.2     44.2      0.0      ax.set_zlabel("Z Axis")
    59         1        273.9    273.9      0.0      ax.set_title("Lorenz Attractor")
    60                                           
    61         1         33.6     33.6      0.0      plt.show()
    62         1    3388905.2 3388905.2     32.1      plt.savefig(filename)

Total time: 1.34617 s
File: /workspaces/scientific_computing_in_python/Scientific_Computing_Lorenz/lorenz/plot_lorenz.py
Function: plot_lorenz2D at line 65

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    65                                           @profile
    66                                           def plot_lorenz2D(
    67                                               lorenz: Lorenz, directions: list = ["xy", "xz", "yz"], filename: str = None
    68                                           ):
    69                                               """Plotting of the Lorenz system in 2D.
    70                                           
    71                                               This function takes a Lorenz object and plots the trajectory of the system
    72                                               in 2D for the specified directions.
    73                                           
    74                                               Args:
    75                                                   lorenz (Lorenz): A Lorenz object
    76                                                   directions (list, optional): A list of strings specifying the directions
    77                                                   filename (str, optional): The filename to save the plot to
    78                                           
    79                                               Returns:
    80                                                   A plot of the trajectory of the Lorenz system in 2D
    81                                           
    82                                           
    83                                               """
    84                                           
    85                                               # Ensure the system has been solved before plotting
    86         1          0.6      0.6      0.0      if not lorenz.history:
    87         1      37468.4  37468.4      2.8          lorenz.solve()
    88                                           
    89                                               # Unpack the history into separate x, y, and z lists
    90         1        646.7    646.7      0.0      x, y, z = zip(*lorenz.history)
    91                                           
    92                                               # Create a time array for each point in the trajectory
    93         1         35.9     35.9      0.0      time = np.arange(len(x)) * lorenz.dt
    94                                           
    95                                               # Normalize time array for color mapping
    96         1         41.4     41.4      0.0      time_norm = time / time.max()
    97                                           
    98                                               # Create 1 row by 3 columns subplots
    99         1      73445.1  73445.1      5.5      fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
   100                                           
   101         3          3.1      1.0      0.0      for index, direction in enumerate(directions):
   102         3          2.0      0.7      0.0          ax = axs[index]
   103         2          0.7      0.3      0.0          if direction == "xy":
   104         1      66437.6  66437.6      4.9              sc = ax.scatter(
   105         1          0.3      0.3      0.0                  x, y, c=time_norm, cmap="viridis", s=5
   106                                                       )  # use time for color map
   107         1         86.9     86.9      0.0              ax.set_xlabel("X Axis")
   108         1         67.0     67.0      0.0              ax.set_ylabel("Y Axis")
   109         1          0.2      0.2      0.0          elif direction == "xz":
   110         1      65886.6  65886.6      4.9              sc = ax.scatter(
   111         1          0.2      0.2      0.0                  x, z, c=time_norm, cmap="viridis", s=5
   112                                                       )  # use time for color map
   113         1         79.7     79.7      0.0              ax.set_xlabel("X Axis")
   114         1         61.5     61.5      0.0              ax.set_ylabel("Z Axis")
   115         1          0.2      0.2      0.0          elif direction == "yz":
   116         1      65926.9  65926.9      4.9              sc = ax.scatter(
   117         1          0.2      0.2      0.0                  y, z, c=time_norm, cmap="viridis", s=5
   118                                                       )  # use time for color map
   119         1         81.2     81.2      0.0              ax.set_xlabel("Y Axis")
   120         1         63.4     63.4      0.0              ax.set_ylabel("Z Axis")
   121                                                   else:
   122                                                       raise ValueError("Invalid direction. Must be one of 'xy', 'xz', or 'yz'")
   123                                           
   124         3        776.9    259.0      0.1          ax.set_title(f"Lorenz Attractor ({direction})")
   125                                           
   126                                               # Create a colorbar on the right side
   127         1      23770.0  23770.0      1.8      cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
   128         1         33.3     33.3      0.0      sm = plt.cm.ScalarMappable(
   129         1         30.0     30.0      0.0          cmap=plt.cm.viridis, norm=plt.Normalize(time.min(), time.max())
   130                                               )
   131         1         72.4     72.4      0.0      sm.set_array([])
   132         1       6814.3   6814.3      0.5      fig.colorbar(sm, cax=cbar_ax, label="Time")
   133                                           
   134         1     240993.2 240993.2     17.9      plt.tight_layout()  # Ensure subplots do not overlap
   135         1        578.2    578.2      0.0      plt.subplots_adjust(right=0.9)  # Adjust the right boundary of the plot window
   136         1         39.3     39.3      0.0      plt.show()
   137         1     762730.1 762730.1     56.7      plt.savefig(filename)
```

Overall saving the file takes a lot of time, and for the 3D plot assigning a color to the line segment.


### Results
All results are saved in the `results` folder. The results are saved in the following format:
```
results
├── case1
├── case2
...
``` 


## Computer system
The code was run on a ubuntu 22.04 machine with Intel(R) Core(TM) i5-10400T CPU @ 2.00GHz with 6 cores and 24 GB of RAM.
