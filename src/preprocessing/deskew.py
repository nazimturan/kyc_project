import cv2
from PIL import Image
import numpy as np

def deskew(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar cascades xml files for face and eye
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        # Detect eyes within the face
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            # Get the coordinates of the eyes
            x1, y1, _, _ = eyes[0]
            x2, y2, _, _ = eyes[1]

            # Calculate the angle between the line of 2 eyes with the horizontal line
            if x1 < x2:
                angle = np.arctan((y2-y1)/(x2-x1))
            else:
                angle = np.arctan((y1-y2)/(x1-x2))

            # Convert the angle from radian to degree
            angle = (angle * 180) / np.pi

            # Rotate the image to deskew it
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            deskewed = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

            return deskewed

    # If no face or insufficient eyes detected, return original image
    return image




def process_and_save_image(input_file_path, output_file_path):
    # Load the image
    image = cv2.imread(input_file_path)

    if image is None:
        raise ValueError(f"Could not open or find the image: {input_file_path}")
    
    # Rotate the image based on face detection
    from .face_detection import get_rotation_angle, rotate_image
    angle = get_rotation_angle(image)
    rotated_image = rotate_image(image, angle)

    # Deskew the image
    deskewed_image = deskew(rotated_image)
    
    # Convert the deskewed image to a PIL Image and save it
    pil_image = Image.fromarray(deskewed_image)
    pil_image.save(output_file_path)