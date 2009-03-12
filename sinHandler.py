#!/usr/bin/env python

# simple interactive plot example using
# ComponentEditor and ArrayPlotData

from enthought.traits.api import HasTraits, Instance, Array, Range, Button, on_trait_change
from enthought.traits.ui.api import View, Item, Handler 
from enthought.chaco.api import Plot, ArrayPlotData
from enthought.enable.component_editor import ComponentEditor
from enthought.traits.ui.menu import OKButton
from numpy import arange, sin

class sinDataViewHandler(Handler):
	sinDataView = Instance('sinDataView')

	def init(self, info):
		super(sinDataViewHandler, self).init(info)
		self.sinDataView = info.object

	@on_trait_change('sinDataView.freqY1')
	def replotY1(self,old,new):
		self.sinDataView.replotY1()
	
	@on_trait_change('sinDataView.freqY2')
	def replotY2(self,old,new):
		self.sinDataView.replotY2()

class sinDataView(HasTraits):
	x = Array
	y1 = Array
	y2 = Array
	freqY1 = Range(low=1.0,high=10.0,value=1.0)
	freqY2 = Range(low=1.0,high=10.0,value=2.0)
	myPlot = Instance(Plot)

	traits_view = View(
	              Item('myPlot',
	                   editor=ComponentEditor(),
	                   show_label=False),
	              Item(name='freqY1'),
	              Item(name='freqY2'),
	              buttons = [OKButton],
	              resizable=True,
	              title='Window Title',
	              handler = sinDataViewHandler(),
	              width=500,height=600)

	def __init__(self):

		# data ranges
		self.x = arange(-10,10,0.01)
		self.y1 = sin(self.freqY1*self.x)
		self.y2 = sin(self.freqY2*self.x)

		self.plotdata = ArrayPlotData(x=self.x,y1=self.y1,y2=self.y2)
		self.myPlot = Plot(self.plotdata)
		self.myPlot.plot(("x","y1"),type="line", color="blue",name = 'Y1')
		self.myPlot.plot(("x","y2"),type="line", color="red",name = 'Y2')
		self.myPlot.legend.visible = True
		self.myPlot.title = "ArrayPlotData Example"

	def replotY1(self):
		self.y1 = sin(self.freqY1*self.x)
		self.plotdata.set_data('y1',self.y1)

	def replotY2(self):
		self.y2 = sin(self.freqY2*self.x)
		self.plotdata.set_data('y2',self.y2)


if __name__ == '__main__':
	viewer = sinDataView()
	viewer.configure_traits()