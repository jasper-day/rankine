import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline


def get_points_from_click():
    print("Click points on the plot. Close the plot window when done.")
    plt.figure()
    plt.title("Click to input points. Close when done.")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    points = plt.ginput(n=-1, timeout=0)
    plt.close()
    return points


def get_points_from_input():
    points = []
    n = int(input("Enter the number of points: "))
    for i in range(n):
        x = float(input(f"Enter x coordinate for point {i+1}: "))
        y = float(input(f"Enter y coordinate for point {i+1}: "))
        points.append((x, y))
    return points


def main():
    method = (
        input(
            "Enter 'click' to input points via clicking, or 'manual' to input coordinates manually: "
        )
        .strip()
        .lower()
    )
    if method == "click":
        points = get_points_from_click()
    elif method == "manual":
        points = get_points_from_input()
    else:
        print("Invalid input method.")
        return

    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    n = len(x)

    print("\nYou have entered the following points:")
    for i in range(n):
        print(f"Point {i}: ({x[i]:.2f}, {y[i]:.2f})")

    # Get 'left' or 'right' direction for each point
    directions = []
    for i in range(n):
        while True:
            dir = (
                input(
                    f"For point {i} ({x[i]:.2f}, {y[i]:.2f}), enter 'left' or 'right': "
                )
                .strip()
                .lower()
            )
            if dir in ["left", "right"]:
                directions.append(dir)
                break
            else:
                print("Invalid input. Please enter 'left' or 'right'.")

    # Parameter t (cumulative distance)
    t = np.zeros(n)
    for i in range(1, n):
        dx = x[i] - x[i - 1]
        dy = y[i] - y[i - 1]
        t[i] = t[i - 1] + np.hypot(dx, dy)

    # Derivatives
    dx_i = np.zeros(n)
    dy_i = np.zeros(n)

    for i in range(n):
        if directions[i] == "left":
            if i == 0:
                dx_i[i] = x[i + 1] - x[i]
                dy_i[i] = y[i + 1] - y[i]
            else:
                dx_i[i] = x[i] - x[i - 1]
                dy_i[i] = y[i] - y[i - 1]
        elif directions[i] == "right":
            if i == n - 1:
                dx_i[i] = x[i] - x[i - 1]
                dy_i[i] = y[i] - y[i - 1]
            else:
                dx_i[i] = x[i + 1] - x[i]
                dy_i[i] = y[i + 1] - y[i]

    # Normalize derivatives
    for i in range(n):
        norm = np.hypot(dx_i[i], dy_i[i])
        if norm != 0:
            dx_i[i] /= norm
            dy_i[i] /= norm
        else:
            dx_i[i] = 0
            dy_i[i] = 0

    # Create Cubic Hermite Splines
    spl_x = CubicHermiteSpline(t, x, dx_i)
    spl_y = CubicHermiteSpline(t, y, dy_i)

    # Evaluate spline
    t_new = np.linspace(t[0], t[-1], num=200)
    x_new = spl_x(t_new)
    y_new = spl_y(t_new)

    # Plot the spline
    plt.figure()
    plt.plot(x, y, "o", label="Points")
    plt.plot(x_new, y_new, "-", label="B-spline Curve")
    plt.legend()
    plt.title("B-spline Curve with Direction Control")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()


# By Muhammad Masood
# Copyright 2024
