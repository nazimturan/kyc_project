import os
import logging
from background_removal import remove_background
from deskew import process_and_save_image as deskew_image
from perspective_transformation import align_images
from pathlib import Path




#Erstellen der Logging-Instanz
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO) #DEBUG, INFO, WARNING, ERROR, CRITICAL  




"""def perform_preprocessing(input_dir, intermediate_dir, output_dir):
    # Check if the intermediate and output directories exist, if not, create them
    if not os.path.exists(intermediate_dir):
        os.makedirs(intermediate_dir)
        logging.info(f"Created intermediate directory {intermediate_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f"Created output directory {output_dir}")

    # Step 1: Remove background from images
    logging.info("Starting background removal...")
    remove_background(input_dir, intermediate_dir)

    # Step 2: Deskew the images
    logging.info("Starting image deskewing...")
    for file in os.listdir(intermediate_dir):
        if file.endswith(".jpg"):
            input_file_path = os.path.join(intermediate_dir, file)
            output_file_path = os.path.join(output_dir, f'deskewed_{file}')
            deskew_image(input_file_path, output_file_path)


    logging.info("Preprocessing completed.")"""


def perform_preprocessing(input_dir, intermediate_dir, output_dir):

    # Check if the intermediate and output directories exist, if not, create them
    if not os.path.exists(intermediate_dir):
        os.makedirs(intermediate_dir)
        logging.info(f"Created intermediate directory {intermediate_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    logging.info(f"Created output directory {output_dir}")

    # Step 1: Remove background from images
    logging.info("Starting background removal...")
    remove_background(input_dir, intermediate_dir)

    # Step 2: Rotate and Deskew the images
    logging.info("Starting image rotation and deskewing...")
    for file in os.listdir(intermediate_dir):
        if file.endswith(".jpg"):
            input_file_path = os.path.join(intermediate_dir, file)
            output_file_path = os.path.join(output_dir, f'deskewed_{file}')
            deskew_image(input_file_path, output_file_path)

    logging.info("Preprocessing completed.")