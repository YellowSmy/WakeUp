import cv2 as opencv
import dlib
from math import hypot

## OpenCV
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./library/shape_predictor_68_face_landmarks.dat')

r_eye_point = [42,43,44,45,46,47]
l_eye_point = [36,37,38,39,40,41]

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def _get_blinking_ratio(image, eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(
        eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(
        eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(
        eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(
        eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = opencv.line(image, left_point, right_point, (0, 255, 0), 2)
    ver_line = opencv.line(image, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_lenght = hypot(
        (left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot(
        (center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

def _blinking_detect(image, gray_image, face):
    landmarks = predictor(gray_image, face)

    left_eye_ratio = _get_blinking_ratio(image, l_eye_point, landmarks)
    right_eye_ratio = _get_blinking_ratio(image, r_eye_point, landmarks)
    blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

    return blinking_ratio