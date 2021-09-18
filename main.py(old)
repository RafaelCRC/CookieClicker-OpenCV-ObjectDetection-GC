import cv2 as cv
import numpy as np


def findClickPositions(needle_img_path, haystack_img_path, threshold=0.5, debug_mode=None):
    #haystack_img = cv.imread('cgame.jpg', cv.IMREAD_UNCHANGED)
    haystack_img = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, method)
    #result = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)

    # print(result)

    #threshold = 0.35
    # threshold = 0.20 #SQDIFF_NORMED
    locations = np.where(result >= threshold)
    # locations = np.where(result <= threshold) #SQDIFF_NORMED
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    points = []
    if len(rectangles):
        print('Found needle')

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:

            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x, center_y))

            if debug_mode == 'rectangles':

                top_left = (x, y)
                bottom_right = (x + w, y + h)

                cv.rectangle(haystack_img, top_left,
                             bottom_right, line_color, line_type)

            elif debug_mode == 'points':

                cv.drawMarker(haystack_img, (center_x, center_y),
                              marker_color, marker_type)

        if debug_mode:

            cv.imshow('Matches', haystack_img)
            cv.waitKey()
    # cv.imwrite('result.jpg', haystack_img) #use isto para criar uma foto resultado
    return points


#points = findClickPositions('gallery/gcrop.jpg', 'gallery/gameimgsec.png', 0.35, 'points')
points = findClickPositions('gallery/bcookie.png',
                            'gallery/gameimgsec.png', 0.35, 'rectangles')
