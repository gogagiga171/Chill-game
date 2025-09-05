import pygame as pg
import time
import random


# pygame setup
pg.init()
screen = pg.display.set_mode((700, 1500))
clock = pg.time.Clock()
pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 300)
title_font = pg.font.SysFont('Comic Sans MS', 100)
running = True
max_vel = 5
vel_delta = 0.3
wall_speed = 2
pg.mixer.music.load("Relax.mp3")
pg.mixer.music.play()
title_screen_text = "Tap to play."
mode = "title"

while running:
    screen.fill("white")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if mode == "game":
        if pg.mouse.get_pressed()[0]==1:
        	if vel < max_vel:
         	   vel+=vel_delta
        else:
            if vel > (-max_vel):
            	vel -= vel_delta
        if time.time()-start > 4:
        	hole_y = random.randint(50, 1200)
        	walls.append(pg.Rect(700, 0, 30, hole_y))
        	walls.append(pg.Rect(700, hole_y+150, 30, 1350-hole_y))
        	start = time.time()
    	
    	
    
        col = False
        walls_to_remove = []
        for wall in walls:
        	pg.draw.rect(screen, "black", wall)
        	wall.x -= wall_speed
        	if wall.colliderect(pg.Rect(20, y, 30, 30)):
        		col = True
        	if wall.x <= -30:
        	    count += 0.5
        	    walls_to_remove.append(walls.index(wall))
        walls_to_remove.sort(reverse=True)
        for i in walls_to_remove:
            walls.pop(i)
    
        y -= vel
        if y < 0 or y > 1470 or col:
        	mode = "title"
        	title_screen_text = "Tap to retry."
    
        pg.draw.rect(screen, "black", pg.Rect(20, y, 30, 30))
        text_surface = my_font.render(str(int(count)), False, (0, 0, 0))
        screen.blit(text_surface, (300,0))
        
    if mode == "title":
        if pg.mouse.get_pressed()[0]==1:
        	mode = "game"
        	start = time.time()
        	vel = 0
        	walls = []
        	y = 500
        	count = 0
        text_surface = title_font.render(title_screen_text, False, (0, 0, 0))
        screen.blit(text_surface, (170,200))
        
        
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()