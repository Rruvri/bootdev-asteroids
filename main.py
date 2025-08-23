import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from bullet import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

clock = pygame.time.Clock()
dt = 0
player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
AsteroidField()



def main():
	pygame.init()
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black", rect=None, special_flags=0)
		dt = clock.tick(60)/1000
		updatable.update(dt)
		for ast in asteroids:
			if ast.collision(player) == True:
				print("Game over!")
				sys.exit()
		for d in drawable:
			d.draw(screen)

		pygame.display.flip()





if __name__ == "__main__":
    main()
