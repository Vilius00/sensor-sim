from typing import Callable
import numpy as np
from path_functions import linear

# Parameters
START = 0
END = 100
SAMPLE_COUNT = 1000 # how many samples in between x and x+1

class Path:
    def __init__(self, function: Callable[[float], float]):
        self.path_function: Callable[[float], float] = np.vectorize(function)
        self.points: list[tuple[float, ...]] = []

def build(function: Callable[[float], float]) -> Path:
    path = Path(function)
    x_values = np.linspace(START, END, SAMPLE_COUNT)
    y_values = path.path_function(x_values)
    path.points = np.column_stack((x_values, y_values))
    return path
