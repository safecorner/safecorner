from kivy.uix.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivyblocks.utils import CSize

class MovieViewer(ButtonBehavior, BoxLayout):
	def __init__(self,ancestor=None,record={}, **options):
		options['orientation'] = 'vertical'
		self.initflag = False
		self.options = options
		self.rec_data = record
		super().__init__(**options)
		self.init()
		self.bind(size=self.on_size,
					pos=self.on_size)
		self.bind(on_press=self.do_press)

	def getRecord(self):
		return self.rec_data

	def do_press(self,o, v=None):
		print('MovieViewer():on_press fired ........')

	def init(self):
		if self.initflag:
			return
		self.initflag = True
		tname = self.rec_data['name']
		nane = Label(text=tname,font_size=CSize(1),
					size_hint_y=None,
					height=CSize(2))
		self.add_widget(nane)

	def on_size(self,o,v=None):
		pass
