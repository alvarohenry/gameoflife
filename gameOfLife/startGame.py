#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# gameLife.py
# 
# Author: Alvaro Henry Mamani Aliaga
#

from gi.repository import Gtk
import GameOfLife as gol

class GameLife(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Juego de la Vida de Conway")
		
		# Boxes container
		mainBox = Gtk.Box(spacing=10)
		mainBox.set_homogeneous(False)
		self.add(mainBox)

		labelBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)	
		labelBox.set_homogeneous(False)
		entryBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)	
		entryBox.set_homogeneous(False)

		mainBox.pack_start(labelBox, True, True, 0)
		mainBox.pack_start(entryBox, True, True, 0)

		# options Box
		labelDimension = Gtk.Label("Ingrese dimension de la matriz \n(Por defecto = 50x50)")
		self.entryDimension = Gtk.Entry()
		labelBox.pack_start(labelDimension, True, True, 0)
		entryBox.pack_start(self.entryDimension, True, True, 0)

#mainBox.pack_start(dimensionBox, True, True, 0)

		# Plive
		labelPlive = Gtk.Label("Ingrese Plive \n(Por defecto = 0.5)")
		self.entryPLive = Gtk.Entry()
		labelBox.pack_start(labelPlive, True, True, 0)
		entryBox.pack_start(self.entryPLive, True, True, 0)
		
		# Prand
		labelPrand = Gtk.Label("Ingrese Prand \n(Por defecto = 0.005). \nPara activar/desactivar precione R")
		self.entryPRand = Gtk.Entry()
		labelBox.pack_start(labelPrand, True, True, 0)
		entryBox.pack_start(self.entryPRand, True, True, 0)
		
		labelInstruction = Gtk.Label("La flecha para abajo disminuye la velocidad \nLa fecha para arriba aumenta la velocidad")
		labelBox.pack_start(labelInstruction, True, True, 0)
		# Start Game Button
		button = Gtk.Button("Start Game")
		button.connect("clicked", self.on_click_start_button)
		entryBox.pack_start(button, True, True, 0)

	def set_dimension(self):
		if self.entryDimension.get_text() == "" or self.entryDimension.get_text() == None:
			self.dimension = 50
		else:
			self.dimension = self.entryDimension.get_text()
			
	def set_pLife(self):
		if self.entryPLive.get_text() == "" or self.entryPLive.get_text() == None:
			self.pLife = 0.5
		else:
			self.pLife = self.entryPLive.get_text()
		
	def set_pRand(self):
		if self.entryPRand.get_text() == "" or self.entryPRand.get_text() == None:
			self.pRand = 0.005
		else:
			self.pRand = self.entryPRand.get_text()
		
	def on_click_start_button(self, button):
		print "CLick on the start button"
		self.set_dimension()
		self.set_pLife()
		self.set_pRand()
		gameOfLife = gol.RectableGridGame(self.dimension, self.pLife, self.pRand)
		gameOfLife.main()

win = GameLife()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

