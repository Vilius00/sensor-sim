import math
import gdspy

# constants
WIRE_WIDTH = 1
WIRE_SPACING = 1
BEND_LENGTH = 0
BEND_WIDTH = math.sqrt((BEND_LENGTH ** 2) / 2)

class BusBuilder:

    def __init__(self):
        self.left_wire_count = 0
        self.right_wire_count = 0

    def connect(self, start_point: tuple[float, float], end_point: tuple[float, float], fromLeft: bool) -> gdspy.FlexPath:
        # Compute offset for bus wire routing
        if fromLeft:
            offset_index = self.left_wire_count
            x_offset = -WIRE_SPACING/2 - offset_index * (WIRE_WIDTH)
            self.left_wire_count += 1
        else:
            offset_index = self.right_wire_count
            x_offset = WIRE_SPACING/2 + offset_index * (WIRE_WIDTH)
            self.right_wire_count += 1

        end_point = (end_point[0] + x_offset, end_point[1])

        # Initial point with offset
        flex = gdspy.FlexPath(
            [start_point],
            width=WIRE_WIDTH,
            corners="smooth",
            ends="flush"
        )

        sx, sy = start_point
        ex, ey = end_point

        if fromLeft:
            x_target = ex + x_offset
            y_target = ey
            flex.segment((x_target, sy))  # horizontal
            flex.segment((x_target, y_target))  # vertical
        else:
            x_target = ex + x_offset
            y_target = ey
            flex.segment((x_target, sy))  # horizontal
            flex.segment((x_target, y_target))  # vertical
        return flex

def create_routed_bus(points, wire_count):
    offsets = [(i - wire_count / 2) * (WIRE_WIDTH + WIRE_SPACING) + WIRE_SPACING for i in range(wire_count)]
    return gdspy.FlexPath(
        points=points,
        width=WIRE_WIDTH,
        offset=offsets,
        corners="smooth",
        ends="flush"
    )
