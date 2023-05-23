import cv2
import dlib
import numpy as np

# Initialize dlib's face detector and facial landmark predictor
# Note: You need to download shape_predictor_68_face_landmarks.dat file and adjust path accordingly
predictor = dlib.shape_predictor('../data/shape_predictor_68_face_landmarks.dat')

def get_rotation_angle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()

    # Detect faces in the grayscale image
    rects = detector(gray, 1)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        coords = np.zeros((68, 2), dtype="int")

        for i in range(0, 68):
            coords[i] = (shape.part(i).x, shape.part(i).y)

        left_eye = coords[36:42]
        right_eye = coords[42:48]

        left_eye_center = left_eye.mean(axis=0).astype("int")
        right_eye_center = right_eye.mean(axis=0).astype("int")

        dY = right_eye_center[1] - left_eye_center[1]
        dX = right_eye_center[0] - left_eye_center[0]
        angle = np.degrees(np.arctan2(dY, dX))

        return angle

    return None

def rotate_image(image, angle):
    if angle is None:
        return image

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated
