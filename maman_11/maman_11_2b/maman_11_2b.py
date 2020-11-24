import sys
import math
import numpy as np
from PIL import Image


def error_diff(im, levels):
    im_arr = np.asarray(im, float)
    out = np.copy(im_arr)
    n, m = np.shape(out)
    for i in range(n):
        for j in range(m):
            out[i][j] = math.ceil(out[i][j] * (levels - 1) / 256 - 0.5) * round(255 / (levels - 1))
            err = im_arr[i][j] - out[i][j]

            if i + 1 < n:
                out[i + 1][j] = out[i + 1][j] + 3 * err / 8

            if j + 1 < m:
                out[i][j + 1] = out[i][j + 1] + 3 * err / 8

            if i + 1 < n and j + 1 < m:
                out[i + 1][j + 1] = out[i + 1][j + 1] + err / 4
    return Image.fromarray(np.uint8(out))


assert len(sys.argv) > 1, "Usage: python maman_11_2b.py [image file name]"
input_img = Image.open(sys.argv[1]).convert("L")
output_img = error_diff(input_img, 4)
output_img.show()
output_img.save("output.png", "PNG")





