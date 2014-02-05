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
		mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.add(mainBox)

		# options Box
		dimensionBox = Gtk.Box(spacing=10)
		labelDimension = Gtk.Label("Ingrese dimension de la matriz (Por defecto = 50)")
		self.entryDimension = Gtk.Entry()
		dimensionBox.pack_start(labelDimension, True, True, 0)
		dimensionBox.pack_start(self.entryDimension, True, True, 0)
		mainBox.pack_start(dimensionBox, True, True, 0)

		# Plive
		pLiveBox = Gtk.Box(spacing=10)
		labelPlive = Gtk.Label("Ingrese Plive (Por defecto = 0.5)")
		self.entryPLive = Gtk.Entry()
		pLiveBox.pack_start(labelPlive, True, True, 0)
		pLiveBox.pack_start(self.entryPLive, True, True, 0)
		mainBox.pack_start(pLiveBox, True, True, 0)
		
		# Prand
		pRandBox = Gtk.Box(spacing=10)
		labelPrand = Gtk.Label("Ingrese Prand (Por defecto = 0.005). Para activar precione R")
		self.entryPRand = Gtk.Entry()
		pRandBox.pack_start(labelPrand, True, True, 0)
		pRandBox.pack_start(self.entryPRand, True, True, 0)
		mainBox.pack_start(pRandBox, True, True, 0)
		
		# Start Game Button
		button = Gtk.Button("Start Game")
		button.connect("clicked", self.on_click_start_button)
		mainBox.pack_start(button, True, True, 0)

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

