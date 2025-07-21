# pipeline:
# path function -> path creator -> sensor part (?)

# layout with GDSII -> bitmap -> error masks for bitmap

#

import gdspy

from reticle.cpu_components.bus import create_routed_bus
from reticle.cpu_die import get_short_path_point_offset_left, get_short_path_point_offset_right, \
    get_long_path_point_offset_right, get_long_path_point_offset_left
from reticle.reticle_field import build

lib = gdspy.GdsLibrary()
cell, points = build()
lib.cells[cell.name] = cell

# first CCD
for i in range(4):
    if i == 0:
        route = get_short_path_point_offset_left()
    elif i == 1:
        route = get_short_path_point_offset_right()
    elif i == 2:
        route = get_long_path_point_offset_left()
    else:
        route = get_long_path_point_offset_right()
    translated_points = [(x + points[i][0], y + points[i][1]) for x, y in route]
    bus = create_routed_bus(translated_points, 8)
    bus_cell = gdspy.Cell(f'Bus {i}')
    bus_cell.add(bus)
    ref = gdspy.CellReference(bus_cell)
    cell.add(ref)

cell.flatten()

gdspy.LayoutViewer(library=lib)

