import gdspy
from reticle.cpu_components import core
from reticle.cpu_components.bus import BusBuilder

# constants
CORE_WIDTH = 80
CORE_HEIGHT = 30
VERTICAL_SPACING = 8
HORIZONTAL_SPACING = 23
MIDDLE = (CORE_WIDTH * 2 + HORIZONTAL_SPACING) / 2
EIGHT_LANE_OFFSET = 9.5
CCD_VERTICAL_SPACING = 19 # code duplication

class CCD:
    
    cell: gdspy.Cell
    bus_point: tuple[float, float]
    wire_count: int
    
    def __init__(self, core_count = 8):
        self.cell = gdspy.Cell('CCD')
        self.wire_count = core_count

        # Create the core layout
        cell_core = core.build(width=CORE_WIDTH, height=CORE_HEIGHT)  # this returns a gdspy.Cell

        # Define spacing between cores
        self.bus_point = (MIDDLE, core_count / 2 * CORE_HEIGHT + (core_count / 2 - 1) * VERTICAL_SPACING)
        bus_builder = BusBuilder()

        # Arrange in 2x2 grid
        core_pair = 0
        for i in range(int(core_count / 2)):  # levels of cores (floors, layers, height of core stack...)

            for j in range(2):  # cores in one level
                if j == 1:
                    x = CORE_WIDTH + HORIZONTAL_SPACING
                else:
                    x = 0
                if core_pair != 0:
                    y = core_pair * (CORE_HEIGHT + VERTICAL_SPACING)
                else:
                    y = 0

                ref = gdspy.CellReference(cell_core, (x, y))
                self.cell.add(ref)

                left_edge = x
                right_edge = x + CORE_WIDTH
                middle_of_edge = y + CORE_HEIGHT / 2

                if j == 0:
                    wire_start = (right_edge, middle_of_edge)
                    wire = bus_builder.connect(wire_start, self.bus_point, fromLeft=True)
                else:
                    wire_start = (left_edge, middle_of_edge)
                    wire = bus_builder.connect(wire_start, self.bus_point, fromLeft=False)
                self.cell.add(wire)

            core_pair += 1


def get_short_path_point_offset_left():
    return [(0,0),
            (0,EIGHT_LANE_OFFSET),
            (MIDDLE + EIGHT_LANE_OFFSET, EIGHT_LANE_OFFSET),
            (MIDDLE + EIGHT_LANE_OFFSET, -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - CCD_VERTICAL_SPACING + 11)]

def get_short_path_point_offset_right():
    return [(0,0),
            (0,EIGHT_LANE_OFFSET),
            (-(MIDDLE + EIGHT_LANE_OFFSET), EIGHT_LANE_OFFSET),
            (-(MIDDLE + EIGHT_LANE_OFFSET), -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - CCD_VERTICAL_SPACING + 11)]
def get_long_path_point_offset_left():
    return [(0, 0),
            (0, EIGHT_LANE_OFFSET),
            (MIDDLE + EIGHT_LANE_OFFSET, EIGHT_LANE_OFFSET),
            (MIDDLE + EIGHT_LANE_OFFSET, -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - 1.5),
            (MIDDLE + EIGHT_LANE_OFFSET * 2.7, -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - 1.5),
            (MIDDLE + EIGHT_LANE_OFFSET * 2.7, -CORE_HEIGHT * 9 - 5 * VERTICAL_SPACING + 3)]

def get_long_path_point_offset_right():
    return [(0,0),
            (0,EIGHT_LANE_OFFSET),
            (-(MIDDLE + EIGHT_LANE_OFFSET), EIGHT_LANE_OFFSET),
            (-(MIDDLE + EIGHT_LANE_OFFSET), -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - 1.5),
            (-(MIDDLE + EIGHT_LANE_OFFSET * 2.7), -CORE_HEIGHT * 4 - 2 * VERTICAL_SPACING - 1.5),
            (-(MIDDLE + EIGHT_LANE_OFFSET * 2.7), -CORE_HEIGHT * 9 - 5 * VERTICAL_SPACING + 3)]