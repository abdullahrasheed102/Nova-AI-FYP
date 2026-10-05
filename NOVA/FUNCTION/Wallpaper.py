import os
import random
import time
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from FUNCTION.platform_utils import set_wallpaper

def change_wallpaper(image_path):
    set_wallpaper(image_path)

def get_random_image_from_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return os.path.join(folder_path, random.choice(image_files))

def change_wallpaper_once(folder_path):
    random_image = get_random_image_from_folder(folder_path)
    change_wallpaper(random_image)


# if __name__ == "__main__":
#     folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Wallpapers")
#     change_interval = 60  

#     while True: 
#         random_image = get_random_image_from_folder(folder_path) 
#         change_wallpaper(random_image)
#         time.sleep(change_interval)

