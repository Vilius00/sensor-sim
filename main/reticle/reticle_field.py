import gdspy
from reticle.cpu_die import CCD

#constants
HORIZONTAL_SPACING = 67.5
VERTICAL_SPACING = 19

def build(ccd_count = 4) -> (gdspy.Cell, list[tuple[float,float]]):
    ccd = CCD()
    cell = gdspy.Cell(name='CPU')
    ccd_bounding_box = ccd.cell.get_bounding_box()
    ccd_width = (ccd_bounding_box[1]-ccd_bounding_box[0])[0]
    ccd_height = (ccd_bounding_box[1]-ccd_bounding_box[0])[1]
    points = []

    for i in range((int)(ccd_count/2)):
        for j in range(2):
            ref = gdspy.CellReference(ccd.cell, (j * (HORIZONTAL_SPACING + ccd_width), i * (VERTICAL_SPACING + ccd_height)))
            cell.add(element=ref)
            bounding_box = ref.get_bounding_box()
            points.append(((bounding_box[0][0] + bounding_box[1][0]) / 2, max(bounding_box[0][1], bounding_box[1][1])))

    return cell, points

