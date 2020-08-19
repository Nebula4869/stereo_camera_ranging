# stereo_camera_ranging
Disparity map calculation and ranging with stereo camera parameters obtained by calibration

### Environment

- python==3.6.5
- opencv-python==4.2.0

### Getting Started

1. Run "take_photos.py" to call the stereo camera to take several standard chessboard images.
2. Import the chessboard image group into the stereoCameraCalibrator tool in Matlab for calibration to obtain camera parameters.
3. Set camera parameters in "camera_configs.py".
4. Run "demo.py" to perform disparity map calculation and ranging.
