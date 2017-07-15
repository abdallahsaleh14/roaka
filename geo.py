
# This should be based on GeoLocation data provided from each client's GPS sensor
# To make up for this (Since large distences cannot be covered for demostration purposes),
# this script depends on visual map input.


import palgame
from collections import deque
from node import Node
import pygame
import math

SCREEN_WIDTH = 520
SCREEN_HEIGHT = 681
NODER = 7				# Node Radius

USERC = (246, 89, 89)		# Node Color
NODEC = (96, 246, 89)		# User Cell Color


nodes = deque()

user_cell = palgame.get_random_ball()
palgame.set_radius(user_cell, 13)

def distance(node): # returns the PHYSICAL distance between two Nodes
	return math.sqrt((node.cor(0)-palgame.get_x(user_cell))**2 + (node.cor()-palgame.get_y(user_cell))**2)

def trans(value):
	return int(value * 2.5) # TODO

def findNearNode():
	nearest = 0
	for n in range(0, 11):
		if(distance(nodes[n])<distance(nodes[nearest])):
			nearest = n
	return nearest

def draw_objects():
	for _node in nodes:
		x= trans(_node.cor(0))
		y= trans(_node.cor(1))

		palgame.draw_circle(x, y, NODER, NODEC)

		for _route in _node.child():
			route = _route[0]
			palgame.draw_line((x, y), (trans(nodes[route].cor(0)), trans(nodes[route].cor(1))))
			palgame.draw_line((x, y+2), (trans(nodes[route].cor(0)), trans(nodes[route].cor(1))))
			palgame.draw_line((x, y-2), (trans(nodes[route].cor(0)), trans(nodes[route].cor(1))))
			palgame.draw_line((x-2, y), (trans(nodes[route].cor(0)), trans(nodes[route].cor(1))))
			palgame.draw_line((x+2, y), (trans(nodes[route].cor(0)), trans(nodes[route].cor(1))))

	x= trans(palgame.get_x(user_cell))
	y= trans(palgame.get_y(user_cell))
	radius=palgame.get_radius(user_cell)

	palgame.draw_circle(x, y, radius, USERC)

def setNodes(_nodes):
	nodes.clear()
	nodes.extend(_nodes)

def update():
	palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

	palgame.get_event()

	### Write code here that will update the user's cell
	### and update all the other cells. Make sure you first
	### fill in the update_user_ball_position() and update_ball_position
	### functions and then call them here.
	### Now we want to eat the food. Fill in the eat_food function
	### and then call it here
	### Now we want to eat the other cells. Fill in the eat_cells function
	### and then call it here
	keys= pygame.key.get_pressed()
	if(keys[pygame.K_UP]):
		palgame.set_y(user_cell, palgame.get_y(user_cell)-5)
	if(keys[pygame.K_DOWN]):
		palgame.set_y(user_cell, palgame.get_y(user_cell)+5)
	if(keys[pygame.K_RIGHT]):
		palgame.set_x(user_cell, palgame.get_x(user_cell)+5)
	if(keys[pygame.K_LEFT]):
		palgame.set_x(user_cell, palgame.get_x(user_cell)-5)

	palgame.clear_screen()


	### Now we want to actually draw all our objects to the screen.
	### Fill in the draw_objects function. Make sure to draw all the
	### cells and all the food.

	draw_objects()

	palgame.draw_everything()