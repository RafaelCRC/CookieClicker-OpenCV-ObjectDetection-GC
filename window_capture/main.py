import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))

WindowCapture.list_window_names()
wincap = WindowCapture(None)


loop_time = time()
while(True):

    screenshot = wincap.get_Screenshot()

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')