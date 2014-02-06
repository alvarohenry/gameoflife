#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Alvaro Henry Mamani Aliaga
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import random
import sys

class RectableGridGame():
	def __init__(self, dimension, pLife, pRand):
		print "la probabilidad en RectableGridGame es", pLife, dimension
		self.dimension = int(dimension)
		self.pLife = float(pLife)
		self.pRand = float(pRand)
		self.activeRand = False
		self.matrix = np.zeros((self.dimension, self.dimension))
		self.init_matrix()

	def initOpenGl(self):
		glClearColor(1.0, 1.0, 1.0, 1.0)
		gluOrtho2D(-2, self.dimension, -2, self.dimension)

	def plotGame(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(0.0, 0.0, 0.0)
		glPointSize(9.0)

		glBegin(GL_POINTS)
		for x in range(self.dimension):
			for y in range(self.dimension):
				if self.matrix[x][y] == 1:
					glVertex2f(x, y)
		glEnd()
		glFlush()
		glutSwapBuffers()

	def idleFunction(self):
		self.transition_state()
		glutPostRedisplay()

	def keyboardFunction(self, key, x, y):
		print "press", key
		if key == 'r' or key == 'R':
			self.activeRand = not self.activeRand
		

	def main(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
		glutInitWindowPosition(50, 50)
		glutInitWindowSize(500, 500)
		glutCreateWindow("Juego de la vida de Conway")
		glutDisplayFunc(self.plotGame)
		glutIdleFunc(self.idleFunction)
		glutKeyboardFunc(self.keyboardFunction)
		self.initOpenGl()
		glutMainLoop()

	###################################################
	# Game of Life methods
	def init_matrix(self):
		for x in range(self.dimension):
			for y in range(self.dimension):
				if random.random() > self.pLife:
					self.matrix[x][y] = 0
				else:
					self.matrix[x][y] = 1
	
	def rand_probability(self, pRand):
		randVal = random.randint(0, 1000) / 1000. 
		if randVal <= pRand:
			return True
		return False
				
	def transition_state(self):
		life_cells = 0
		tmp_matrix = np.ones((self.dimension, self.dimension)) * -1
		for x in range(self.dimension):
			for y in range(self.dimension):
				if self.activeRand == True and self.rand_probability(self.pRand):
					tmp_matrix[x][y] = random.randint(0, 1)
					continue
				fil = x - 1
				col = y - 1
				if fil == -1:
					fil = self.dimension-1 # 10
				if col == -1:
					col = self.dimension-1 # 10
				for a in range(fil, fil+3):
					for b in range(col, col+3):
						fil_ = a
						col_ = b
						if fil_ == self.dimension: # 11
							fil_ = 0
						if fil_ == self.dimension+1: # 12
							fil_ = 1
						if col_ == self.dimension: # 11
							col_ = 0
						if col_ == self.dimension+1: # 12
							col_ = 1
						if fil_ == x and col_ == y:
							continue
						life_cells += self.matrix[fil_][col_]
				# apply game of life rules
				# Regla del nacimiento: nace si a su alrededor hay 3 celulas vivas
				if self.matrix[x][y] == 0 and life_cells == 3: # si estava muerta
					tmp_matrix[x][y] = 1	# nace
				# Regla de sobrevivencia: permanece vida si hay 2 o 3 celulas vivas a su alrededor
				if self.matrix[x][y] == 1 and (life_cells < 2 or life_cells > 3): # celula viva
					tmp_matrix[x][y] = 0	# muere por soledad o por sobrepoblacion
				life_cells = 0
		for x in range(self.dimension):
			for y in range(self.dimension):
				if tmp_matrix[x][y] != -1:	
					self.matrix[x][y] = tmp_matrix[x][y]
