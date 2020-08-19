import cv2

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
frame_cnt = 0
while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('Read frame failed!')
        break

    cv2.imshow('0', frame1)
    cv2.imshow('1', frame2)
    if cv2.waitKey(1) == 13:
        cv2.imwrite('./0/%d.jpg' % frame_cnt, frame1)
        cv2.imwrite('./1/%d.jpg' % frame_cnt, frame2)
        frame_cnt += 1
