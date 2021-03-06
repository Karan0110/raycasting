import pygame

class Line(object):
	"""Represents a line segment that is used for ray intersection"""

	def __init__(self, ax, ay, bx, by):
		"""Creates Line instance given x and y coordinates of start and end point"""

		self.ax = ax
		self.ay = ay
		self.bx = bx
		self.by = by

		self.dx = self.bx - self.ax
		self.dy = self.by - self.ay

	def render(self, screen, color=(0x00, 0x00, 0x00), width=1):
		"""Draws the line, with a default color of black and a default width of 1"""

		pygame.draw.line(screen, (0x00, 0x00, 0x00), (self.ax, self.ay), (self.bx, self.by), width)

	@staticmethod
	def get_aabb_lines(x, y, width, height):
		"""Returns the lines that constitute the sides of an AABB"""

		return [
			Line(x, y, x + width, y),
			Line(x + width, y, x + width, y + height),
			Line(x + width, y + height, x, y + height),
			Line(x, y + height, x, y),
		]
		
