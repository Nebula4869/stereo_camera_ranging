import cv2
import numpy as np

cameraMatrix1 = np.array([[586.829978497819, 0, 0],
                          [0.179149707866171, 586.330015853109, 0],
                          [645.992221312647, 349.806425817981, 1]]).transpose()
distCoeffs1 = np.array([[0.0193298639022541, -0.0789285114925871, 0.000518367443180117, 0.00255033064722926, 0.0319714563601892]])

cameraMatrix2 = np.array([[593.217944192284, 0, 0],
                          [0.280590817518164, 591.466073643200, 0],
                          [631.398142107881, 355.596009712245, 1]]).transpose()
distCoeffs2 = np.array([[0.0176032314408665, -0.0236444568133413, 0.000954288949709830, 0.00516602213170503, -0.0775193466824424]])

R = np.array([[0.999872242079515, -0.00193943213036696, 0.0158662573373666],
              [0.00189113322896206, 0.999993534378719, 0.00305856434747378],
              [-0.0158720866301238, -0.00302816838518311, 0.999869445008816]]).transpose()  # Rotation relation vector
T = np.array([-18.5570654154461, -0.0869463330698457, 0.585121748350652])  # Translation relation vector

imageSize = (1280, 720)

# Computing rectification transforms
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R, T)

# Computing transformation map
left_map1, left_map2 = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, imageSize, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, imageSize, cv2.CV_16SC2)
