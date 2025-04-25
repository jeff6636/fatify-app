
from PIL import Image, ImageFilter

def simulate_fatify(image_path):
    img = Image.open(image_path)
    fat_img = img.resize((int(img.width * 1.15), int(img.height * 1.15)))
    fat_img = fat_img.filter(ImageFilter.SMOOTH_MORE)
    return fat_img
