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
import numpy
import os
import cv2

from alinea.phenomenal.binarization.threshold import meanshift
from alinea.phenomenal.binarization.routines import mean
# ==============================================================================


def test_wrong_parameters_1():
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    try:
        meanshift(None, mean_image)
    except Exception, e:
        assert e.message == 'image should be a numpy.ndarray'
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_2():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    try:
        meanshift(image, None)
    except Exception, e:
        assert e.message == 'mean should be a numpy.ndarray'
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_3():

    image = numpy.zeros((25, 25), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image)
    except Exception, e:
        assert e.message == 'image should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_4():

    image = numpy.zeros((25, 25), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image)
    except Exception, e:
        assert e.message == 'image should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_5():

    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image)
    except Exception, e:
        assert e.message == 'mean should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_6():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((10, 10, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image)
    except Exception, e:
        assert e.message == 'image and mean must have equal sizes'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_7():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image)
    except Exception, e:
        assert e.message == 'mean should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_8():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image, threshold=2)
    except Exception, e:
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_9():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image, reverse=None)
    except Exception, e:
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_10():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mask = [[1, 1, 1]]

    try:
        meanshift(image, mean_image, mask=mask)
    except Exception, e:
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_11():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mask = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image, mask=mask)
    except Exception, e:
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_12():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mask = numpy.zeros((25, 26), dtype=numpy.uint8)

    try:
        meanshift(image, mean_image, mask=mask)
    except Exception, e:
        assert type(e) == ValueError
    else:
        assert False


def test_simply_working_1():

    im1 = numpy.zeros((25, 25, 3), numpy.uint8)
    im2 = numpy.zeros((25, 25, 3), numpy.uint8)

    mean_image = mean(list([im1, im2]))

    bin_img = meanshift(im1, mean_image)

    assert bin_img.shape == (25, 25)


def test_simply_working_2():
    im1 = numpy.zeros((25, 25, 3), numpy.uint8)
    im2 = numpy.zeros((25, 25, 3), numpy.uint8)
    mask = numpy.zeros((25, 25), numpy.uint8)

    mean_image = mean(list([im1, im2]))

    bin_img = meanshift(im1, mean_image, mask=mask)
    assert bin_img.shape == (25, 25)


def test_simply_working_3():
    im1 = numpy.zeros((25, 25, 3), numpy.uint8)
    im2 = numpy.zeros((25, 25, 3), numpy.uint8)
    mask = numpy.zeros((25, 25), numpy.uint8)

    mean_image = mean(list([im1, im2]))

    bin_img = meanshift(im1, mean_image, mask=mask, threshold=1)
    assert bin_img.shape == (25, 25)


def test_simply_working_4():
    im1 = numpy.zeros((25, 25, 3), numpy.uint8)
    im2 = numpy.zeros((25, 25, 3), numpy.uint8)
    mask = numpy.zeros((25, 25), numpy.uint8)

    mean_image = mean(list([im1, im2]))

    bin_img = meanshift(im1, mean_image, mask=mask, reverse=True)
    assert bin_img.shape == (25, 25)


def test_no_regression_1():

    images = dict()
    for angle in range(0, 360, 30):
        file_name = os.path.dirname(__file__) + "/data/" + str(angle) + ".png"
        im = cv2.imread(file_name, flags=cv2.IMREAD_COLOR)
        images[angle] = im

    file_name_mask = os.path.dirname(__file__) + "/data/mask_mean_shift.png"
    mask = cv2.imread(file_name_mask, flags=cv2.IMREAD_GRAYSCALE)

    mean_image = mean(images.values())

    refs = [(0, 4798),
            (30, 4114),
            (60, 5987),
            (90, 5359),
            (120, 4737),
            (150, 4977),
            (180, 4907),
            (210, 3096),
            (240, 5657),
            (270, 4932),
            (300, 4332),
            (330, 4617)]

    for angle, ref in refs:

        im_bin = meanshift(images[angle], mean_image, mask=mask)
        im_bin *= 255
        # Acceptation error of 0.01 %
        acceptation_error = ref * 0.001

        print abs(numpy.count_nonzero(im_bin) - ref), acceptation_error
        if abs(numpy.count_nonzero(im_bin) - ref) > acceptation_error:
            assert False
