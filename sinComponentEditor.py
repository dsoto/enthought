#!/usr/bin/env python

# simple interactive plot example using 
# ComponentEditor and ArrayPlotData

# TODO : find how to turn off autoscale axis

from enthought.traits.api import HasTraits, Instance, Array, Range, Button
from enthought.traits.ui.api import View, Item
# enthought.chaco.plot.Plot inherits from DataView
from enthought.chaco.api import Plot, ArrayPlotData, PlotGraphicsContext
from enthought.chaco.pdf_graphics_context import PdfPlotGraphicsContext
from enthought.chaco.tools.api import PanTool, ZoomTool, DragZoom
from enthought.enable.component_editor import ComponentEditor
from numpy import arange, sin

class sinDataView(HasTraits):
	x = Array
	y = Array
	y2 = Array
	freq = Range(low=1.0,high=10.0,value=1.0)
	printPNG = Button
	printPDF = Button
	plotAttribute = Instance(Plot)
	
	traits_view = View(
	              Item('plotAttribute',
	                   editor=ComponentEditor(),
	                   show_label=False),
	              Item(name='freq'),
	              Item(name='printPNG'),
	              Item(name='printPDF'),
	              resizable=True,
	              title='Window Title',
	              width=500,height=500)

	def __init__(self):
		
		# data ranges
		self.x = arange(-10,10,0.01)
		self.y = self.freq*sin(self.x)
		self.y2 = sin(self.freq * self.x)

		self.plotdata = ArrayPlotData(x=self.x,y=self.y,y2=self.y2)
		self.plotAttribute = Plot(self.plotdata)
		self.plotAttribute.plot(("x","y"),type="line", color="blue",name = 'amp')
		self.plotAttribute.plot(("x","y2"),type="line", color="red",name = 'freq')
		self.plotAttribute.index_range.set_bounds(-20,20)
		self.plotAttribute.legend.visible = True
		self.plotAttribute.title = "Using Component Editor"
		self.plotAttribute.tools.append(PanTool(self.plotAttribute))
		self.plotAttribute.tools.append(DragZoom(self.plotAttribute,
		                                         drag_button='right'))

	def plotPNG(self):		
		# now plot object to png file
		size = (500,500)
		self.plotAttribute.outer_bounds = list(size)
		self.plotAttribute.do_layout(force=True)
		gc = PlotGraphicsContext(size, dpi=72)
		gc.render_component(self.plotAttribute)
		gc.save('testPGC.png')

	def plotPDF(self):
		size = (500,500)
		self.plotAttribute.bounds = list(size)
		self.plotAttribute.do_layout(force=True)
		# negative dest_box values are from upper right corner
		gc = PdfPlotGraphicsContext(filename = 'testPPGC.pdf', 
		                            dest_box = (0.5, 0.5, -0.5, -0.5))
		gc.render_component(self.plotAttribute)
		gc.save()
		
	def _freq_changed(self):
		self.y = self.freq*sin(self.x)
		self.y2 = sin(self.freq*self.x)
		self.plotdata.set_data("y",self.y)
		self.plotdata.set_data("y2",self.y2)
		return

	def _printPNG_fired(self):
		self.plotPNG()
		
	def _printPDF_fired(self):
		self.plotPDF()

if __name__ == '__main__':
	viewer = sinDataView()
	viewer.configure_traits()