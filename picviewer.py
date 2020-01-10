from kivy.uix.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivyblocks.utils import CSize, absurl
from kivyblocks.baseWidget import PressableImage
from appPublic.jsonConfig import getConfig

class PicViewer(ButtonBehavior, BoxLayout):
	def __init__(self, ancestor=None,record={}, **options):
		print('PicViewer(),options=',options)
		options['orientation'] = 'vertical'
		self.initflag = False
		selfancestor = ancestor
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
		print('SongViewer():on_press fired ........')

	def init(self):
		if self.initflag:
			return
		self.initflag = True
		config = getConfig()
		url = "%s/idfile/%s" % (config.uihome, self.rec_data['id'])
		img = PressableImage(source=url) 
		self.add_widget(img)

	def on_size(self,o,v=None):
		pass
