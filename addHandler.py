#!/usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Instance, Button,
                                  on_trait_change)
from enthought.traits.ui.api import (View, Item, Handler)
from enthought.traits.ui.menu import (OKButton, CancelButton, Action)

class mathBoxHandler(Handler):
	mathbox = Instance('mathBox')

	def init(self, info):
		super(mathBoxHandler, self).init(info)
		self.mathbox = info.object

	@on_trait_change('mathbox.a,mathbox.b')
	def callAdd(self,old,new):
		self.mathbox.add()

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
	
	view = View('a','b','c', 
	            title = 'Adder',
	            handler = mathBoxHandler(),
	            buttons = [OKButton, CancelButton])


myMathBox = mathBox(1,2)
myMathBox.configure_traits()
