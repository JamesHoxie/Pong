import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

DISPLAY_HEIGHT = 800
SCREEN_BOTTOM = DISPLAY_HEIGHT - 210
DISPLAY_WIDTH = 600
BLOCK_SIZE_X = 10
BLOCK_SIZE_Y = 75
BALL_SIZE = 10
FPS = 30
FONT = pygame.font.SysFont(None, 25)
SCORE_FONT = pygame.font.SysFont(None, 100)
CLOCK = pygame.time.Clock()

def pause():
	paused = True
	game_display.fill(black)
	message_to_screen("Paused, Press C to continue or Q to quit.", white)
	pygame.display.update()

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()

		
		CLOCK.tick(5)

def display_p1_score(updated_score):
	score_update = SCORE_FONT.render(str(updated_score), True, white)
	game_display.blit(score_update, [DISPLAY_WIDTH/4, DISPLAY_HEIGHT/10])

def display_p2_score(updated_score):
	score_update = SCORE_FONT.render(str(updated_score), True, white)
	game_display.blit(score_update, [DISPLAY_WIDTH/4 + DISPLAY_WIDTH/2, DISPLAY_HEIGHT/10])

def text_objects(text, color):
	text_surface = FONT.render(text, True, color)
	return text_surface, text_surface.get_rect()

def message_to_screen(msg, color):
	text_surface, text_rect = text_objects(msg, color)
	text_rect.center = (DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3)
	game_display.blit(text_surface, text_rect)
	# screen_text = FONT.render(msg, True, color)
	# game_display.blit(screen_text, [DISPLAY_WIDTH/8, DISPLAY_HEIGHT/4])

def game_loop():
	game_exit = False
	game_over = False
	p1_x_pos = 0
	p1_y_pos = DISPLAY_HEIGHT/2
	p1_y_change = 0
	p2_x_pos = DISPLAY_WIDTH - BLOCK_SIZE_X
	p2_y_pos = 300
	p2_y_change = 0
	ball_x_pos = 300
	ball_y_pos = 1
	ball_x_change = BALL_SIZE/3
	ball_y_change = BALL_SIZE/3
	p1_score = 0
	p2_score = 0

	while not game_exit:

		while game_over == True:
			game_display.fill(black)

			if p1_score >= 10:
				message_to_screen("Player 1 wins! Press c to play again or q to quit", white)
			elif p2_score >= 10: 
				message_to_screen("Player 2 wins! Press c to play again or q to quit", white)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_exit = True
					game_over = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_exit = True
						game_over = False
					if event.key == pygame.K_c:
						p1_score = 0
						p2_score = 0
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					p1_y_change = -BLOCK_SIZE_Y/4
				if event.key == pygame.K_s:
					p1_y_change = BLOCK_SIZE_Y/4
				if event.key == pygame.K_UP:
					p2_y_change = -BLOCK_SIZE_Y/4
				if event.key == pygame.K_DOWN:
					p2_y_change = BLOCK_SIZE_Y/4
				if event.key == pygame.K_p:
					pause()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_s:
					p1_y_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					p2_y_change = 0


		if ball_x_pos <= p1_x_pos + BLOCK_SIZE_X and ball_y_pos >= p1_y_pos and ball_y_pos <= p1_y_pos + BLOCK_SIZE_Y:
			ball_x_change = BALL_SIZE/3

		if ball_x_pos >= p2_x_pos - BLOCK_SIZE_X and ball_y_pos >= p2_y_pos and ball_y_pos <= p2_y_pos + BLOCK_SIZE_Y:
			ball_x_change = -BALL_SIZE/3

		if ball_y_pos <= 0:
			ball_y_change = BALL_SIZE/3

		if ball_y_pos >= SCREEN_BOTTOM:
			ball_y_change = -BALL_SIZE/3

		if ball_x_pos < 0:
			ball_x_pos = DISPLAY_WIDTH/2
			ball_y_pos = random.randrange(0, SCREEN_BOTTOM)
			p2_score += 1

		if ball_x_pos > DISPLAY_WIDTH:
			ball_x_pos = DISPLAY_WIDTH/2
			ball_y_pos = random.randrange(0, SCREEN_BOTTOM)
			p1_score += 1

		if p1_y_pos < 0:
			p1_y_pos = 0

		if p1_y_pos > SCREEN_BOTTOM - BLOCK_SIZE_Y:
			p1_y_pos = SCREEN_BOTTOM - BLOCK_SIZE_Y

		if p2_y_pos < 0:
			p2_y_pos = 0

		if p2_y_pos > SCREEN_BOTTOM - BLOCK_SIZE_Y:
			p2_y_pos = SCREEN_BOTTOM - BLOCK_SIZE_Y

		if p1_score >= 10 or p2_score >= 10:
			game_over = True

		p1_y_pos += p1_y_change
		p2_y_pos += p2_y_change
		ball_x_pos += 2*ball_x_change
		ball_y_pos += 2*ball_y_change
		game_display.fill(black)
		display_p1_score(p1_score)
		display_p2_score(p2_score)
		game_display.fill(white, rect=[p1_x_pos, p1_y_pos, BLOCK_SIZE_X, BLOCK_SIZE_Y])
		game_display.fill(white, rect=[p2_x_pos, p2_y_pos, BLOCK_SIZE_X, BLOCK_SIZE_Y])
		game_display.fill(white, rect=[ball_x_pos, ball_y_pos, BALL_SIZE, BALL_SIZE])
		game_display.fill(white, rect=[DISPLAY_WIDTH/2, 0,BLOCK_SIZE_X,DISPLAY_HEIGHT])
		#game_display.fill(red, rect=[p1_x_pos, p1_y_pos + BLOCK_SIZE_Y, BLOCK_SIZE_X, 1])
		#game_display.fill(red, rect=[0, 0, DISPLAY_WIDTH, 10])
		#game_display.fill(red, rect=[0, SCREEN_BOTTOM - BLOCK_SIZE_Y - 10, DISPLAY_WIDTH, 1])
		pygame.display.update()
		CLOCK.tick(FPS)

	#unitialize pygame
	pygame.quit()
	#exit out of python
	quit()

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_WIDTH))
pygame.display.set_caption('Python Pong')

game_loop()
