#!/usr/bin/env python

from enthought.traits.api import Int, HasTraits, Button
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.menu import OKButton, CancelButton

# TODO : use separate handler class

class mathBox(HasTraits):
	a = Int
	b = Int
	c = Int
	mult = Button()
	
	def __init__(self,x,y):
		self.a = x
		self.b = y
		self.c = x + y
		
	def _mult_fired(self):
		self.c = self.a * self.b
	
	def _a_changed(self):
		self.c = self.a + self.b
	
	def _b_changed(self):
		self.c = self.a + self.b
	
	view = View('a','b','c', 
	            Item('mult', show_label=False),
	            buttons = [OKButton, CancelButton])

for i in range(1,4):
	myMathBox = mathBox(i,i+1)
	myMathBox.configure_traits()
