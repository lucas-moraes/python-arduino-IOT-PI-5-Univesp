import os
from PIL import Image

def list_image_files(folder_path: str):
    """
    Lists image files (JPEG, PNG, GIF, BMP, etc.) in the specified folder.

    Args:
        folder_path (str): The absolute path of the folder.

    Returns:
        list: A list of tuples containing (file_name).
    """
    image_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    file_name, file_extension = os.path.splitext(filename)
                    image_files.append((file_name, file_extension))
            except (IOError, OSError, Image.DecompressionBombError):
                pass

    return image_files