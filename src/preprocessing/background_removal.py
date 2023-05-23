from pathlib import Path
from rembg import remove, new_session




def remove_background(input_dir: str, output_dir: str):
    session = new_session()

    for file in Path(input_dir).glob('*.jpg'):
        input_path = str(file)
        output_path = str(Path(output_dir) / (file.stem + ".out.jpg"))

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input_img = i.read()
                output_img = remove(input_img, session=session)
                o.write(output_img)