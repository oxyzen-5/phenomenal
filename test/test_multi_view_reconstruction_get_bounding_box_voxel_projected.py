# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
from alinea.phenomenal.plant_1 import (
    plant_1_calibration_camera_side_2_target)

from alinea.phenomenal.multi_view_reconstruction import (
    get_bounding_box_voxel_projected)
# ==============================================================================


def test_bbox_projection_1():

    voxel_center = (0, 0, 0)
    voxel_size = 20

    projection = lambda pt: (pt[0], pt[1])

    res = get_bounding_box_voxel_projected(voxel_center, voxel_size, projection)
    x_min, x_max, y_min, y_max = res

    assert x_min == -10
    assert x_max == 10
    assert y_min == -10
    assert y_max == 10


def test_bbox_projection_2():
    angle = 0
    calibration = plant_1_calibration_camera_side_2_target()
    projection = calibration.get_projection(angle)

    voxel_center = (0, 0, 0)
    voxel_size = 8
    ref = (1017.3089948473056,
           1025.7875288183795,
           1258.2799614482235,
           1265.171426935121)

    res = get_bounding_box_voxel_projected(voxel_center, voxel_size, projection)

    assert -1 < res[0] - ref[0] < 1
    assert -1 < res[1] - ref[1] < 1
    assert -1 < res[2] - ref[2] < 1
    assert -1 < res[3] - ref[3] < 1

if __name__ == "__main__":
    test_bbox_projection_1()
    test_bbox_projection_2()
