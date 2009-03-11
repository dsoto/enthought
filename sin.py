#!/usr/bin/env python

# simple interactive plot example using
# ChacoPlotItem as the plot object


from enthought.traits.api import HasTraits, Array, Range, Float
from enthought.traits.ui.api import View, Item
from enthought.traits.ui.menu import OKButton
from enthought.chaco.chaco_plot_editor import ChacoPlotItem
from numpy import arange, sin

class sinBox(HasTraits):
	# data for plotting goes in these arrays
	x = Array
	y = Array
	# the Range is an object that has a slider in the UI view
	freq = Range(low=1.0,high=10.0,value=1.0)
	amp = Range(low=1.0,high=10.0,value=1.0)

	def __init__(self):
		super(sinBox,self).__init__()

	traits_view = View(
	              ChacoPlotItem("x", "y",
	                            type='line',
	                            resizable=True,
	                            x_label="x", y_label="y",
	                            x_bounds=(-10,10), x_auto=False,
	                            y_bounds=(-10,10), y_auto=False,
	                            title='y vs. x'),
	              Item(name='freq'),
	              Item(name='amp'),
	              buttons=[OKButton],
	              title='Window Title',
	              width=400,height=400)


	def _freq_changed(self):
	# callback for frequency slider
		self.x = arange(-10,10,.01)
		self.y = self.amp*sin(self.freq*self.x)

	def _amp_changed(self):
	# callback for amplitude slider
		self.x = arange(-10,10,.01)
		self.y = self.amp*sin(self.freq*self.x)


if __name__ == '__main__':
	mySinBox = sinBox()
	# i don't know why i have to call _freq_changed to get first plot
	mySinBox._freq_changed()
	mySinBox.configure_traits()