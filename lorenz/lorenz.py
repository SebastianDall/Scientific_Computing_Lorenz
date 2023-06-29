from typing import Tuple, List

try:

    @profile
    def f(x):
        return x

except:

    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner


class Lorenz:
    """
    A class to represent the Lorenz system and simulate its evolution.

    Attributes
    ----------
    state : tuple of float
        The current state of the system (x, y, z).
    sigma : float
        The sigma parameter of the Lorenz system.
    beta : float
        The beta parameter of the Lorenz system.
    rho : float
        The rho parameter of the Lorenz system.
    dt : float
        The time step for the simulation.

    Methods
    -------
    step_euler():
        Advances the state of the system one time step using the Euler method.
    step_rk4():
        Advances the state of the system one time step using the Runge-Kutta 4 method.
    solve(method="euler"):
        Solves the Lorenz system for N time steps.

    Examples
    --------
    >>> lorenz = Lorenz((0.0, 1.0, 1.05))
    >>> lorenz.solve()


    """

    def __init__(
        self,
        initial_state: Tuple[float, float, float],
        sigma: float = 10.0,
        beta: float = 2.667,
        rho: float = 28.0,
        dt: float = 0.01,
        N: int = 5000,
    ) -> None:
        """
        Constructs all the necessary attributes for the Lorenz object.

        Parameters
        ----------
            initial_state : tuple of float
                The initial state of the system (x, y, z).
            sigma : float, optional
                The sigma parameter of the Lorenz system (default is 10.0).
            beta : float, optional
                The beta parameter of the Lorenz system (default is 2.667).
            rho : float, optional
                The rho parameter of the Lorenz system (default is 28.0).
            dt : float, optional
                The time step for the simulation (default is 0.01).
            N : int, optional
        """
        self.state = initial_state
        self.sigma = sigma
        self.beta = beta
        self.rho = rho
        self.dt = dt
        self.N = N

        self.history = []

    @profile
    def solve(self, method: str = "euler") -> List[Tuple[float, float, float]]:
        """
        Solves the Lorenz system for N time steps.

        Parameters
        ----------
        method : str, optional
            The integration method to use (either "euler" or "rk4").
            Default is "euler".

        Returns
        -------
        list of tuple of float
            The state of the system (x, y, z) at each time step.

        Examples
        --------
        >>> lorenz = Lorenz((0.0, 1.0, 1.05)).solve()

        """
        if method not in ("euler", "rk4"):
            raise ValueError('Method must be either "euler" or "rk4"')

        self.history = []  # Reset the history at the beginning of each simulation
        self.history.append(self.state)  # Record the initial state

        for _ in range(self.N):
            if method == "euler":
                self.step_euler()
            else:
                self.step_rk4()
            self.history.append(self.state)  # Record the state after each step

        return self.history

    @profile
    def step_euler(self) -> Tuple[float, float, float]:
        """
        Advances the state of the system one time step using the Euler method.

        Returns
        -------
        tuple of float
            The new state of the system (x, y, z).

        Examples
        --------
        lorenz = Lorenz((0.0, 1.0, 1.05)).step_euler()
        """
        x, y, z = self.state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        self.state = x + dx * self.dt, y + dy * self.dt, z + dz * self.dt
        return self.state

    def step_rk4(self) -> Tuple[float, float, float]:
        """
        Advances the state of the system one time step using the Runge-Kutta 4 method.

        Returns
        -------
        tuple of float
            The new state of the system (x, y, z).

        Note
        ----
        This method has not been implemented yet.
        """
        # def rk4(x, y, z, dt):
        #     k1 = dt*f(x, y, z)
        #     l1 = dt*g(x, y, z)
        #     m1 = dt*h(x, y, z)
        #     k2 = dt*f(x+k1/2, y+l1/2, z+m1/2)
        #     l2 = dt*g(x+k1/2, y+l1/2, z+m1/2)
        #     m2 = dt*h(x+k1/2, y+l1/2, z+m1/2)
        #     k3 = dt*f(x+k2/2, y+l2/2, z+m2/2)
        #     l3 = dt*g(x+k2/2, y+l2/2, z+m2/2)
        #     m3 = dt*h(x+k2/2, y+l2/2, z+m2/2)
        #     k4 = dt*f(x+k3, y+l3, z+m3)
        #     l4 = dt*g(x+k3, y+l3, z+m3)
        #     m4 = dt*h(x+k3, y+l3, z+m3)
        #     x += (k1+2*k2+2*k3+k4)/6
        #     y += (l1+2*l2+2*l3+l4)/6
        #     z += (m1+2*m2+2*m3+m4)/6
        pass  # implement RK4 approximation here
