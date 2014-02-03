#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# gameLife.py
# 
# Alumno: Alvaro Henry Mamani Aliaga
#

from gi.repository import Gtk

class GameLife(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Conway's Game if Life")
		
		# Boxes container
		mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.add(mainBox)
		optionsBox = Gtk.Box(spacing=10)
		
		# options Box
		# Plive
		labelPlive = Gtk.Label("Enter Plive (Default PLive = 0.5)")
		optionsBox.pack_start(labelPlive, True, True, 0)
		
		self.entryPlive = Gtk.Entry()
		optionsBox.pack_start(self.entryPlive, True, True, 0)
		
		# Prand
		labelPrand = Gtk.Label("Enter Prand")
		optionsBox.pack_start(labelPrand, True, True, 0)
		
		self.entryPrand = Gtk.Entry()
		optionsBox.pack_start(self.entryPrand, True, True, 0)
		
		# Start Game Button
		button = Gtk.Button("Start Game")
		button.connect("clicked", self.on_click_start_button)
		optionsBox.pack_start(button, True, True, 0)

		mainBox.pack_start(optionsBox, True, True, 0)


	def on_click_start_button(self, button):
		print "CLick on the start button"
				

win = GameLife()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

