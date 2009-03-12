#!/usr/bin/env python

from enthought.traits.api import Int, HasTraits, on_trait_change
from enthought.traits.ui.api import View
from enthought.traits.ui.menu import OKButton

class mathBox(HasTraits):
	a = Int
	b = Int
	c = Int

	def __init__(self,x,y):
		super(mathBox,self).__init__()
		self.a = x
		self.b = y
		self.add()
	
	def add(self):
		self.c = self.a + self.b

	@on_trait_change('a,b')
	def update(self, name, value):
		self.add()

	view = View('a','b','c',
	            buttons = [OKButton])

myMathBox = mathBox(1,2)
myMathBox.configure_traits()
