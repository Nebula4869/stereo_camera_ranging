from camera_configs import *
import numpy as np
import cv2


cv2.namedWindow('depth')
cv2.createTrackbar('num', 'depth', 0, 10, lambda x: None)
cv2.createTrackbar('blockSize', 'depth', 5, 255, lambda x: None)

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Click the left mouse button to output the distance
def callback(event, x, y, flags, param):
    _ = flags
    _ = param
    if event == cv2.EVENT_LBUTTONDOWN:
        print('distance: %dmm' % max(threeD[y][x][2], 0))


cv2.setMouseCallback('depth', callback, None)


while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('Read frame failed!')
        break

    # Applying transformation
    img1_rectified = cv2.remap(frame1, left_map1, left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, right_map1, right_map2, cv2.INTER_LINEAR)

    # StereoBM requires grayscale images
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    num = cv2.getTrackbarPos('num', 'depth')
    blockSize = cv2.getTrackbarPos('blockSize', 'depth')
    blockSize = max(blockSize // 2 * 2 + 1, blockSize)
    blockSize = max(blockSize, 5)

    # Computing disparity map
    stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)
    disparity = stereo.compute(imgL, imgR)

    # Reprojecting disparity image to 3D space
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., Q)

    cv2.imshow('left', img1_rectified)
    cv2.imshow('right', img2_rectified)
    cv2.imshow('depth', cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U))

    if cv2.waitKey(1) == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
