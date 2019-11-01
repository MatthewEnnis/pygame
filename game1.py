import pygame
import random

def starfill(background,amount):
	for i in range(amount):
		s = random.random() * 2 + .5
		
		colour = random.randint(0,255)
		
		x = random.randint(0,512)
		y = colour * 2.6
		
		star = ((x+10*s,y),(x+17*s,y+20*s),(x,y+7*s),(x+20*s,y+7*s),(x+3*s,y+20*s))
		pygame.draw.polygon(background, (255,colour,255), star, 1)

pygame.init()
 
screen = pygame.display.set_mode((512,768))
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
starfill(background,500)
background = background.convert()
screen.blit(background, (0,0))
clock = pygame.time.Clock()
FPS = 60
running = True

player = pygame.Surface((20,30))
player.fill((0,0,0))
pygame.draw.polygon(player, (255,255,255), ((10,0),(20,30),(10,20),(0,30)), 1)
player = player.convert()
playerx = 256
playervx = 0

while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				running = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and playervx > -8:
		playervx -= 2
	if keys[pygame.K_RIGHT] and playervx < 8:
		playervx += 2
	if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
		if playervx > 0:
			playervx -= .5
		elif playervx < 0:
			playervx += .5
	
	background.fill((0,0,0))
	starfill(background,10)
	
	playerx += playervx
	screen.blit(background, (0,0))
	screen.blit(player, (playerx, 710))
	pygame.display.set_caption(str(clock.get_fps()))
	pygame.display.flip()
