# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from lorenz.lorenz import Lorenz


# def plot_lorenz(lorenz: Lorenz):
#     """
#     Plots the evolution of the Lorenz system in 3D.

#     Parameters
#     ----------
#     lorenz : Lorenz
#         A Lorenz object.
#     """
#     fig = plt.figure()
#     ax = fig.gca(projection="3d")

#     # Plot the evolution of the Lorenz system
#     ax.plot(
#         lorenz.state_history[:, 0],
#         lorenz.state_history[:, 1],
#         lorenz.state_history[:, 2],
#         "k-",
#     )

#     # Plot the final point with a different color
#     ax.plot(
#         lorenz.state_history[-1, 0],
#         lorenz.state_history[-1, 1],
#         lorenz.state_history[-1, 2],
#         "r.",
#         markersize=15,
#     )

#     # Plot the starting point with a different color
#     ax.plot(
#         lorenz.state_history[0, 0],
#         lorenz.state_history[0, 1],
#         lorenz.state_history[0, 2],
#         "b.",
#         markersize=15,
#     )

#     # Set the axes labels
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_zlabel("z")

#     # Set the axes limits
#     ax.set_xlim((-25, 25))
#     ax.set_ylim((-35, 35))
#     ax.set_zlim((5, 55))

#     # Set the initial view angle
#     ax.view_init(18, 30)

#     plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from lorenz.lorenz import Lorenz
import matplotlib.animation as animation


def plot_lorenz3D(lorenz: Lorenz):
    """Plot the trajectory of the Lorenz system."""

    # Ensure the system has been solved before plotting
    if not lorenz.history:
        lorenz.solve()

    # Unpack the history into separate x, y, and z lists
    x, y, z = zip(*lorenz.history)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Create a color array (from 0 to 1) one for each point in the trajectory
    colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

    # Plot the trajectory with color corresponding to time
    for i in range(1, len(x)):
        ax.plot(x[i - 1 : i + 1], y[i - 1 : i + 1], z[i - 1 : i + 1], color=colors[i])

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.show()


def plot_lorenz2D(lorenz: Lorenz, directions: list = ["xy", "xz", "yz"]):
    """Plot the trajectory of the Lorenz system."""

    # Ensure the system has been solved before plotting
    if not lorenz.history:
        lorenz.solve()

    # Unpack the history into separate x, y, and z lists
    x, y, z = zip(*lorenz.history)

    # Create a color array (from 0 to 1) one for each point in the trajectory
    colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

    # Create 1 row by 3 columns subplots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for index, direction in enumerate(directions):
        ax = axs[index]
        if direction == "xy":
            ax.plot(x, y, color="blue")
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")
        elif direction == "xz":
            ax.plot(x, z, color="green")
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Z Axis")
        elif direction == "yz":
            ax.plot(y, z, color="red")
            ax.set_xlabel("Y Axis")
            ax.set_ylabel("Z Axis")
        else:
            raise ValueError("Invalid direction. Must be one of 'xy', 'xz', or 'yz'")

        ax.set_title(f"Lorenz Attractor ({direction})")

    plt.tight_layout()  # Ensure subplots do not overlap
    plt.show()


def animate_lorenz(lorenz: Lorenz):
    """Plot the trajectory of the Lorenz system."""

    # Ensure the system has been solved before plotting
    if not lorenz.history:
        lorenz.solve()

    # Unpack the history into separate x, y, and z lists
    x, y, z = zip(*lorenz.history)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Create a color array (from 0 to 1) one for each point in the trajectory
    colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

    (line,) = ax.plot([], [], [], color="blue")

    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), max(y)])
    ax.set_zlim([min(z), max(z)])

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    def animate(i):
        line.set_data(x[:i], y[:i])
        line.set_3d_properties(z[:i])
        line.set_color(colors[i])
        return (line,)

    anim = FuncAnimation(fig, animate, frames=len(x), interval=30, blit=True)

    # Save the animation
    anim.save("lorenz_attractor.gif", writer="imagemagick")

    plt.show()