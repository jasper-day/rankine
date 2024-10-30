import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from scipy.interpolate import CubicHermiteSpline
import splipy as sp # spline provider
import splipy.curve_factory as curve_factory

def plot_image():
    image = mpimg.imread("controls_notebooks/resources/contest_layout.png")
    plt.imshow(image, extent=[0,1100,0,1110])

def get_points_from_click():
    image = mpimg.imread("controls_notebooks/resources/contest_layout.png")
    print("Click points on the plot. Close the plot window when done.")
    plt.figure()
    plt.title("Click to input points. Close when done.")
    plot_image()
    plt.grid()
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

def get_spline_from_points(points):
    # cubic interpolation with free boundaries
    spline = curve_factory.cubic_curve(np.asarray(points))
    return spline
    

def main():
    method = (
        input(
            "Enter 'click' to input points via clicking, or 'manual' to input coordinates manually (default click): "
        )
        .strip()
        .lower()
    )
    if method == "click" or method == "":
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
    print("[\n" + 
          "\n".join([f"\t[{x:.2f}, {y:.2f}]," for x, y in zip(x, y)]) 
          + "\n]")

    # small abstraction to allow importing
    spline = get_spline_from_points(points)
    
    # Evaluate spline
    t_new = np.linspace(spline.start(), spline.end(), 200).ravel()
    xi_new = spline(t_new)

    # Plot the spline
    plt.figure()
    plot_image()
    plt.plot(x, y, "o", label="Points")
    plt.plot(xi_new[:,0], xi_new[:,1], "-", label="Cubic Curve")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()


# By Muhammad Masood
# Copyright 2024
