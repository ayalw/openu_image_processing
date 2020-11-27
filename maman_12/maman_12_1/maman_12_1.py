import sys
from PIL import Image, ImageFilter


def apply_filter(img):
    km = (
        -1, -1, -1,
        -1, 8, -1,
        -1, -1, -1
    )
    k = ImageFilter.Kernel(
        size=(3, 3),
        kernel=km,
        scale=1,
        offset=0
    )
    return img.filter(k)


assert len(sys.argv) > 1, "Usage: python maman_12_1.py [image file name]"
input_img = Image.open(sys.argv[1])
output_img = apply_filter(input_img)
output_img.show()
output_img.save("output.png", "PNG")

