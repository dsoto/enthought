#!/usr/bin/env python

from enthought.traits.api import Int, HasTraits
from enthought.traits.ui.api import View
from enthought.traits.ui.menu import OKButton

# TODO : use separate handler class

class mathBox(HasTraits):
	a = Int
	b = Int
	c = Int

	def __init__(self,x,y):
		self.a = x
		self.b = y
		self.c = x + y

	def _a_changed(self):
		self.c = self.a + self.b

	def _b_changed(self):
		self.c = self.a + self.b

	view = View('a','b','c',
	            buttons = [OKButton])

myMathBox = mathBox(1,2)
myMathBox.configure_traits()
