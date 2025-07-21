import gdspy

LAYER = 1

def build(width, height, name="CPU_CORE") -> gdspy.Cell:
    cell = gdspy.Cell(name)
    rect = gdspy.Rectangle((0, 0), (width, height), layer=LAYER)
    cell.add(rect)
    return cell
