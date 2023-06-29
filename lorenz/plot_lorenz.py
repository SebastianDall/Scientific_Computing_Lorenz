import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from lorenz.lorenz import Lorenz
import matplotlib.animation as animation


def plot_lorenz3D(lorenz: Lorenz, filename: str = None):
    """Plotting of the Lorenz system in 3D.

    This function takes a Lorenz object and plots the trajectory of the system

    Args:
        lorenz (Lorenz): A Lorenz object
        filename (str, optional): The filename to save the plot to. Defaults to None.

    Returns:
        A plot of the trajectory of the Lorenz system in 3D

    """

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
    plt.savefig(filename)


def plot_lorenz2D(
    lorenz: Lorenz, directions: list = ["xy", "xz", "yz"], filename: str = None
):
    """Plotting of the Lorenz system in 2D.

    This function takes a Lorenz object and plots the trajectory of the system
    in 2D for the specified directions.

    Args:
        lorenz (Lorenz): A Lorenz object
        directions (list, optional): A list of strings specifying the directions
        filename (str, optional): The filename to save the plot to

    Returns:
        A plot of the trajectory of the Lorenz system in 2D


    """

    # Ensure the system has been solved before plotting
    if not lorenz.history:
        lorenz.solve()

    # Unpack the history into separate x, y, and z lists
    x, y, z = zip(*lorenz.history)

    # Create a time array for each point in the trajectory
    time = np.arange(len(x)) * lorenz.dt

    # Normalize time array for color mapping
    time_norm = time / time.max()

    # Create 1 row by 3 columns subplots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for index, direction in enumerate(directions):
        ax = axs[index]
        if direction == "xy":
            sc = ax.scatter(
                x, y, c=time_norm, cmap="viridis", s=5
            )  # use time for color map
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Y Axis")
        elif direction == "xz":
            sc = ax.scatter(
                x, z, c=time_norm, cmap="viridis", s=5
            )  # use time for color map
            ax.set_xlabel("X Axis")
            ax.set_ylabel("Z Axis")
        elif direction == "yz":
            sc = ax.scatter(
                y, z, c=time_norm, cmap="viridis", s=5
            )  # use time for color map
            ax.set_xlabel("Y Axis")
            ax.set_ylabel("Z Axis")
        else:
            raise ValueError("Invalid direction. Must be one of 'xy', 'xz', or 'yz'")

        ax.set_title(f"Lorenz Attractor ({direction})")

    # Create a colorbar on the right side
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    sm = plt.cm.ScalarMappable(
        cmap=plt.cm.viridis, norm=plt.Normalize(time.min(), time.max())
    )
    sm.set_array([])
    fig.colorbar(sm, cax=cbar_ax, label="Time")

    plt.tight_layout()  # Ensure subplots do not overlap
    plt.subplots_adjust(right=0.9)  # Adjust the right boundary of the plot window
    plt.show()
    plt.savefig(filename)


# def animate_lorenz(lorenz: Lorenz):
#     """Plot the trajectory of the Lorenz system."""

#     # Ensure the system has been solved before plotting
#     if not lorenz.history:
#         lorenz.solve()

#     # Unpack the history into separate x, y, and z lists
#     x, y, z = zip(*lorenz.history)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection="3d")

#     # Create a color array (from 0 to 1) one for each point in the trajectory
#     colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

#     (line,) = ax.plot([], [], [], color="blue")

#     ax.set_xlim([min(x), max(x)])
#     ax.set_ylim([min(y), max(y)])
#     ax.set_zlim([min(z), max(z)])

#     ax.set_xlabel("X Axis")
#     ax.set_ylabel("Y Axis")
#     ax.set_zlabel("Z Axis")
#     ax.set_title("Lorenz Attractor")

#     def animate(i):
#         line.set_data(x[:i], y[:i])
#         line.set_3d_properties(z[:i])
#         line.set_color(colors[i])
#         return (line,)

#     anim = FuncAnimation(fig, animate, frames=len(x), interval=30, blit=True)

#     # Save the animation
#     anim.save("lorenz_attractor.gif", writer="imagemagick")

#     plt.show()


# def animate_lorenz(lorenz: Lorenz, filename: str = None):
#     """Animate the trajectory of the Lorenz system in 3D.

#     This function takes a Lorenz object and animates the trajectory of the system
#     in 3D.

#     Args:
#         lorenz (Lorenz): A Lorenz object
#         filename (str, optional): The filename to save the animation as a gif

#     Returns:
#         An animation of the trajectory of the Lorenz system in 3D saved as a gif


#     """

#     # Ensure the system has been solved before plotting
#     if not lorenz.history:
#         lorenz.solve()

#     # Unpack the history into separate x, y, and z lists
#     x, y, z = zip(*lorenz.history)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection="3d")

#     # Create a color array (from 0 to 1) one for each point in the trajectory
#     colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

#     # Add a line object for the trajectory
#     (line,) = ax.plot([], [], [], color="blue", lw=2)

#     # Add a point object for the current position
#     (point,) = ax.plot([], [], [], color="red", marker="o")

#     ax.set_xlim([min(x), max(x)])
#     ax.set_ylim([min(y), max(y)])
#     ax.set_zlim([min(z), max(z)])

#     ax.set_xlabel("X Axis")
#     ax.set_ylabel("Y Axis")
#     ax.set_zlabel("Z Axis")
#     ax.set_title("Lorenz Attractor")

#     def animate(i):
#         # Update the line data
#         line.set_data(x[:i], y[:i])
#         line.set_3d_properties(z[:i])
#         line.set_color(colors[i])

#         # Update the point data
#         point.set_data(x[i], y[i])
#         point.set_3d_properties(z[i])
#         point.set_color(colors[i])

#         return line, point

#     anim = FuncAnimation(fig, animate, frames=len(x), interval=10, blit=True)

#     # Save the animation
#     anim.save(filename, writer="imagemagick")

#     plt.show()


def animate_lorenz(lorenz: Lorenz, filename=None):
    """Animate the trajectory of the Lorenz system in 3D.

    This function takes a Lorenz object and animates the trajectory of the system
    in 3D.

    Args:
        lorenz (Lorenz): A Lorenz object
        filename (str, optional): The filename to save the animation as a gif

    Returns:
        An animation of the trajectory of the Lorenz system in 3D saved as a gif


    """
    # Ensure the system has been solved before plotting
    if not lorenz.history:
        lorenz.solve()

    # Unpack the history into separate x, y, and z lists
    x, y, z = zip(*lorenz.history)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Create a color array (from 0 to 1) one for each point in the trajectory
    colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), max(y)])
    ax.set_zlim([min(z), max(z)])

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    lines = []

    def animate(i):
        # If a line for this time step already exists, just update its data
        if i < len(lines):
            line = lines[i]
            line.set_data(x[:i], y[:i])
            line.set_3d_properties(z[:i])
        else:
            # Otherwise, create a new line for this time step
            (line,) = ax.plot(x[:i], y[:i], z[:i], color=colors[i])
            lines.append(line)

        return lines

    anim = FuncAnimation(fig, animate, frames=len(x), interval=30, blit=True)

    # Save the animation
    anim.save(filename, writer="imagemagick")

    plt.show()
