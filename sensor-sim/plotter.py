import matplotlib.pyplot as plt
import numpy as np

def plot(arr: list[tuple[float, ...]]):
    # arr[:, 0] = all x values
    # arr[:, 1] = all y values
    plt.plot(arr[:, 0], arr[:, 1], marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of 2-tuple array')
    plt.show()
