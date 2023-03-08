"""
File: blur.py
Name: Audrey Tsang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, smiley-face.png
    :return: blurred img(The blur algorithm uses the average RGB values of a pixel's nearest neighbors.)
    """
    old_img = img
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for y in range(old_img.height):
        for x in range(old_img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            #  Find out all neighbors
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    neighbor_x = x+i
                    neighbor_y = y+j
                    #  Boundary conditions: only use pixels in the image
                    if 0 <= neighbor_x < old_img.width:
                        if 0 <= neighbor_y < old_img.height:
                            neighbor = old_img.get_pixel(neighbor_x, neighbor_y)
                            r_sum += neighbor.red
                            g_sum += neighbor.green
                            b_sum += neighbor.blue
                            count += 1
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return blurred


def main():
    """
    This program shows the original image first, smiley-face.png,
    and then compare to its blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
