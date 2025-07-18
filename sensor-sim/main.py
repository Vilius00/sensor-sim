import path_builder as pb
from path_functions import quadratic
import plotter

# pipeline:
# path function -> path creator -> sensor part (?)

path = pb.build(quadratic)

plotter.plot(path.points)