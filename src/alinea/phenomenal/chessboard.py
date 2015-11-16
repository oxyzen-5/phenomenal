# -*- python -*-
#
#       chessboard.py : 
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       File author(s): Simon Artzet <simon.artzet@gmail.com>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
#       ========================================================================

#       ========================================================================
#       External Import
import cv2
import numpy
import json

import alinea.phenomenal.calibration_model

#       ========================================================================
#       Code
class Chessboard(object):
    def __init__(self, square_size, shape):

        # Initialization
        self.square_size = square_size
        self.shape = shape
        self.corners_points = dict()


        self.object_points = numpy.zeros((self.shape[0] * self.shape[1], 3), numpy.float32)

        # Build Chessboard
        self.object_points[:, :2] = numpy.mgrid[0:self.shape[0], 0:self.shape[1]].T.reshape(-1, 2) * self.square_size

        # 48 points are stored in an 48x3 array obj
        # choose bottom-left corner as origin, to match australian convention
        self.object_points = self.object_points - self.object_points[40, :]

    def __str__(self):

        my_str = ''
        my_str += 'Chessboard Object Values :\n'
        my_str += 'Square size (mm): ' + str(self.square_size) + '\n'
        my_str += 'Shape : ' + str(self.shape) + '\n'

        for angle in self.corners_points:
            my_str += str(angle) + '\n'
            my_str += str(self.corners_points[angle]) + '\n'

        return my_str

    def local_corners_position_3d(self):
        square_size = self.square_size
        width, height = self.shape

        chessboard_pts = []
        for j in range(height):
            for i in range(width):
                v = numpy.array([i * square_size, j * square_size, 0.])
                chessboard_pts.append(v)

        print chessboard_pts

        return chessboard_pts

    def global_corners_position_3d(self, x, y, z, elev, tilt):

        chessboard_pts = self.local_corners_position_3d()

        fr_chess = alinea.phenomenal.calibration_model.chess_frame(
            x, y, z, elev, tilt)

        pts = [fr_chess.global_point(pt) for pt in chessboard_pts]

        return pts

    def find_corners(self, image):
        try:

            found, corners = cv2.findChessboardCorners(
                image,
                tuple(self.shape),
                flags=cv2.CALIB_CB_ADAPTIVE_THRESH +
                      cv2.CALIB_CB_NORMALIZE_IMAGE)

            if found:
                cv2.cornerSubPix(image, corners, (11, 11), (-1, -1),
                                 criteria=(cv2.TERM_CRITERIA_EPS +
                                           cv2.TERM_CRITERIA_MAX_ITER,
                                           30,
                                           0.001))
            else:
                print "Error : Corners not find"
                return None

        except cv2.error:
            print "Error : cv2, get_corners, calibration.py"
            return None

        return corners

    def find_and_add_corners(self, angle, image):
        corners_points = self.find_corners(image)
        if corners_points is not None:
            # self.corners_points[angle] = corners_points[:, 0, :]
            self.corners_points[angle] = corners_points

    def write(self, file_path):

        # Convert to json format
        for angle in self.corners_points:
            self.corners_points[angle] = self.corners_points[angle].tolist()

        save_class = dict()
        save_class['square_size'] = self.square_size
        save_class['shape'] = self.shape
        save_class['corners_points'] = self.corners_points

        with open(file_path + '.json', 'w') as file_corners:
            json.dump(save_class, file_corners)

    @staticmethod
    def read(file_path):

        with open(file_path + '.json', 'r') as file_corners:
            save_class = json.load(file_corners)

            square_size = float(save_class['square_size'])
            shape = [int(val) for val in save_class['shape']]

            chessboard = Chessboard(square_size, shape)

            corners_points = save_class['corners_points']

            # Convert to numpy format
            for angle in corners_points:
                chessboard.corners_points[float(angle)] = numpy.array(
                    corners_points[angle]).astype(numpy.float)

        return chessboard

    # def plot_corners(self, corners, image, figure_name='Image'):
    #
    #     y_min = min(corners[:, 0, 0])
    #     y_max = max(corners[:, 0, 0])
    #     x_min = min(corners[:, 0, 1])
    #     x_max = max(corners[:, 0, 1])
    #     r = 50
    #
    #     image = cv2.drawChessboardCorners(image, self.shape, corners, True)
    #     image = image[x_min - r:x_max + r, y_min - r:y_max + r]
    #
    #     cv2.namedWindow(figure_name, cv2.WINDOW_NORMAL)
    #     cv2.imshow(figure_name, image)
    #     cv2.waitKey()
    #
    # def plot_points(self, projection_points, image, figure_name='Image'):
    #
    #     image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    #
    #     projection_points = projection_points.astype(int)
    #     image[projection_points[:, 0, 1],
    #           projection_points[:, 0, 0]] = [0, 0, 255]
    #
    #     f = pylab.figure()
    #     f.canvas.set_window_title(figure_name)
    #     pylab.title(figure_name)
    #     pylab.imshow(image)
    #     pylab.show()
    #
    #     f.clf()
    #     pylab.close()


#       ========================================================================
#       LOCAL TEST

if __name__ == "__main__":
    do_nothing = None
