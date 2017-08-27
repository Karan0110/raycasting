import pygame

from math import atan2

from ray import Ray, NoIntersectionException
from line import Line

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Raycasting AI")

lines = Line.get_aabb_lines(0, 0, 800, 600) + [
	Line(200, 300, 300, 200),
]

running = True

rx, ry = (800 / 2, 600 / 2)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: running = False

	mx, my = pygame.mouse.get_pos()
	direction = atan2(my - ry, mx - rx)

	screen.fill((0xFF, 0xFF, 0xFF))

	for line in lines: line.render(screen)

	try:
		ray = Ray(rx, ry, direction, lines)
		ray.render(screen)
	except NoIntersectionException:
		pass

	pygame.display.flip()

