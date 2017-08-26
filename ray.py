import pygame

from math import sin, cos

class NoIntersectionException(Exception):
	"""Raised when there are no intersections for a ray, which is usually the result of not including lines for the bounds of the window, or  because the ray is cast outside of the window bounds"""

	pass

class Ray(object):
	"""
	Immutable object used to find distance from line in a certain direction
	
	x, y - start position
	direction - direction of ray
	ix, iy - point of intersection
	"""

	def __init__(self, x, y, direction, lines):
		"""Creates Ray instance given the x and y of the start, the direction and all the lines that it can collide with"""

		self.x = x
		self.y = y
		self.direction = direction

		self.ax = self.x
		self.ay = self.y

		self.bx = self.ax + cos(direction)
		self.by = self.ay + sin(direction)

		self.dx = self.bx - self.ax
		self.dy = self.by - self.ay

		self.ix = None
		self.iy = None
		#squared
		best_distance = -1

		t2 = None

		for line in lines:
			try:
				T2 = (self.dx * (line.ay - self.y) + self.dy * (self.x-line.ax)) / (line.dx * self.dy - line.dy * self.dx)
				T1 = (line.ax + line.dx * T2 - self.x) / self.dx	
	
				if T1 > 0 and 0 < T2 < 1:
					ix = self.x + self.dx * T1
					iy = self.y + self.dy * T1
	
					distance = (self.x - ix) ** 2 + (self.y - iy) ** 2
	
					if (self.ix is None and self.iy is None) or best_distance == -1 or distance < best_distance:
						self.ix = ix
						self.iy = iy
						best_distance = distance
						t2 = T2
			except ZeroDivisionError:
				pass

		if self.ix is None or self.iy is None:
			raise NoIntersectionException("Ray has no intersections, have you forgotten to pass in the bounds of the window?")	
				
	def render(self, screen, color=(0xFF, 0x00, 0x00), width=1):
		"""Draws the ray up to the point of intersection with default color red and line width 1, and also draws small circle at point of intersection"""

		pygame.draw.line(screen, color, (self.x, self.y), (self.ix, self.iy), width)
		pygame.draw.circle(screen, color, (int(self.ix), int(self.iy)), 5)

