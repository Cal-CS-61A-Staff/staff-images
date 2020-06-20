from sys import argv
from os import listdir
from simpleimage import SimpleImage

"""
---USAGE---

python image_fix.py <semester>

e.g. python image_fix.py su20

---NOTES---

- this script will override the original image files

- since the cropping is very naive, it can be lead to unintuitive results

TODO:
- allow for adjustment if the crop doesn't look good
"""

PATH = "../" + argv[1] + "/"

images = listdir(PATH)
for file in images:
    img = SimpleImage(PATH + file)
    if img.width != img.height:
        size = min(img.width, img.height)
        result = SimpleImage.blank(size, size)
        crop_x = crop_y = 0
        if img.width > img.height:
            crop_x = (img.width - img.height) / 2
        else:
            crop_y = (img.height - img.width) / 2
        for x in range(size):
            for y in range(size):
                old_x = x + crop_x
                old_y = y + crop_y
                old_pixel = img.get_pixel(old_x, old_y)
                result.set_pixel(x, y, old_pixel)
        result.pil_image.save(PATH + file)
