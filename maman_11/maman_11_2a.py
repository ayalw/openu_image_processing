import sys
from PIL import Image


def swap_red_with_blue(img):
    width, height = img.size
    for x in range(width):
        for y in range(height):
            (r, g, b) = img.getpixel((x, y))
            img.putpixel((x, y), (b, g, r))
    return img


assert len(sys.argv) > 1, "Usage: python maman_11_main.py [image file name]"
input_file = sys.argv[1]
picture = Image.open(input_file)
output_img = swap_red_with_blue(picture)
output_img.show()
output_img.save("output.png", "PNG")

