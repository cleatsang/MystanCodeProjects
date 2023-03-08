"""
File: sierpinski.py
Name: Audrey Tsang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 700			       # The pause time in milliseconds

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program recursively prints the Sierpinski triangle on GWindow.
	It is a self similar structure that occurs at different levels of iterations.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: Controls the order of Sierpinski Triangle.
	:param length: The length of order 1 Sierpinski Triangle.
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle.
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle.
	:return: Inverted triangles drawn by three lines, number depends on the earliest order.
	"""
	if order == 0:	 # If order equals zero, finishing other side of triangles.
		pass
	else:
		#  Draw upper line for the triangle.
		triangle_upper = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		#  Draw left line for the triangle.
		triangle_left = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		#  Draw right line for the triangle.
		triangle_right = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(triangle_left)
		window.add(triangle_right)
		window.add(triangle_upper)
		#  Pause to see it works step-by-step.
		pause(DELAY)
		#  Upper left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		#  Upper right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		#  Lower middle triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+length*0.866/2)


if __name__ == '__main__':
	main()
