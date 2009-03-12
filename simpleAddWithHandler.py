#!/usr/bin/env python

from enthought.traits.api import (Int, HasTraits, Button, on_trait_change)
from enthought.traits.ui.api import (View, Item, Handler)
from enthought.traits.ui.menu import (OKButton, CancelButton, Action)

class mathBoxHandler(Handler):

	def object_a_changed(self,info):
		info.object.c = info.object.a + info.object.b

	def object_b_changed(self,info):
		info.object.c = info.object.a + info.object.b

# 	@on_trait_change('a,b')
#   doesn't work for me
# 	def add(self,info):
# 		info.object.c = info.object.a + info.object.b

# 	@on_trait_change('info.object.a,info.object.b')
#   doesn't work for me
# 	def add(self,info):
# 		info.object.c = info.object.a + info.object.b


class mathBox(HasTraits):
	a      = Int
	b      = Int
	c      = Int

	def __init__(self,x,y):
		super(mathBox,self).__init__()
		self.a = x
		self.b = y
		self.c = x + y
	
	view = View('a','b','c', 
	            title = 'This Title',
	            handler = mathBoxHandler(),
	            buttons = [OKButton, CancelButton])


myMathBox = mathBox(1,2)
myMathBox.configure_traits()
