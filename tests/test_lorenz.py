from scipy.integrate import odeint
from lorenz.lorenz import Lorenz
from pytest import approx


def test_lorenz_step_euler():
    """
    GIVEN the Lorenz system of equations
    WHEN the system is solved using the Euler method
    THEN the solution should be approximately the same as the custom
    """
    lorenz = Lorenz(initial_state=(1.0, 1.0, 1.0))

    # Test the Euler method
    assert lorenz.step_euler() == approx((1.0, 1.26, 0.9833), rel=1e-2)


def test_lorenz_solve_euler():
    """
    GIVEN the Lorenz system of equations
    WHEN the system is solved using the Euler method
    THEN the solution should be of length N + 1 and the second element should be approximately (1.0, 1.26, 0.9833)
    """

    # Test the solve method with Euler
    lorenz = Lorenz(initial_state=(1.0, 1.0, 1.0))
    lorenz.solve(method="euler")

    assert len(lorenz.history) == lorenz.N + 1
    assert lorenz.history[1] == approx((1.0, 1.26, 0.9833), rel=1e-2)


def lorenz_equations(state, t, sigma, beta, rho):
    """
    Define the Lorenz system of equations.
    """
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z


def test_lorenz_vs_scipy():
    """
    GIVEN the Lorenz system of equations
    WHEN the system is solved using scipy's odeint
    THEN the solution should be approximately the same as the custom Euler method
    """
    sigma, beta, rho = 10, 2.667, 28  # common Lorenz system parameters
    initial_state = (1.0, 1.0, 1.0)
    dt = 0.001  # time step
    N = 100  # number of steps

    # Solve the Lorenz system using scipy's odeint
    t = [dt * i for i in range(N + 1)]
    scipy_solution = odeint(lorenz_equations, initial_state, t, args=(sigma, beta, rho))

    # Solve the Lorenz system using the custom Euler method
    lorenz = Lorenz(
        initial_state=initial_state, sigma=sigma, beta=beta, rho=rho, dt=dt, N=N
    )
    lorenz.solve(method="euler")

    # Compare the two solutions
    for i in range(N + 1):
        assert tuple(lorenz.history[i]) == approx(tuple(scipy_solution[i]), rel=1e-2)
