#!/usr/bin/env python

# simple interactive plot example using 
# ChacoPlotItem as the plot object


from enthought.traits.api import (HasTraits, Array, Range,
                                  Float, Enum)
from enthought.traits.ui.api import View, Item
from enthought.chaco.chaco_plot_editor import ChacoPlotItem
from numpy import arange, sin

class Data(HasTraits):
	x = Array
	y = Array
	freq = Range(low=1.0,high=10.0,value=1.0)
	
	traits_view = View(
	              ChacoPlotItem("x", "y",
	                            type='line',
	                            resizable=True,
	                            x_label="x", y_label="y",
	                            x_bounds=(-10,10), x_auto=False,
	                            y_bounds=(-10,10), y_auto=False,
	                            title='y vs. x'),
	              Item(name='freq'),
	              buttons=["quit"],
	              title='Window Title',
	              width=800,height=800)
	              
	def _freq_changed(self):
		self.x = arange(-10,10,.01)
		self.y = self.freq*sin(self.freq*self.x)
		return

if __name__ == '__main__':
	viewer = Data()
	viewer._freq_changed()
	viewer.configure_traits()