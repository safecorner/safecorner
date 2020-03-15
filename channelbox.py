import os
import codecs
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle
from kivyblocks.utils import *
from appPublic.Singleton import SingletonDecorator

@SingletonDecorator
class Channels(list):
	pass

class WebKitPlayer(BoxLayout):
	def __init__(self,url):
		self.b = BoxLayout(size_hint=(None,None),size=CSize(1,1))
		self.w = AWebView(url=url)
		super().__init__()
		self.add_widget(self.b)
		self.add_widget(self.w)
		self.bind(size=self.onSize,pos=self.onSize)

	def onSize(self,o,v=None):
		if self.width > self.height:
			self.orientation = 'vertical'
		else:
			self.orientation = 'horizontal'
		
class ChannelBox(ButtonBehavior, BoxLayout):
	active_channel = BooleanProperty(False)
	active_bgcolor = [0.3,0.3,1,1]
	normal_bgcolor = [0.3,0.3,0.3,1]
	def __init__(self,channel_name=None, 
					vfile=None, 
					box_width=None, 
					**options):
		self.channel_list = Channels()
		self.channel_name = channel_name
		self.url = vfile
		self.options = options
		opts = options.copy()
		opts['width'] = box_width
		opts['height'] = CSize(3)
		opts['size_hint'] = (None,None)
		opts['orientation'] = 'horizontal'
		ButtonBehavior.__init__(self)
		BoxLayout.__init__(self,**opts)
		l = Label(text=self.channel_name)
		self.add_widget(l)
		if self.channel_list == []:
			self.active_channel = True
		else:
			self.active_channel = False
		self.channel_list.append(self)
		"""
		self._keyboard = Window.request_keyboard(None,self)
		if self._keyboard:
			self._keyboard.bind(on_key_down=self.on_keyboard_down)
		"""
		self.bind(pos=self.on_active_channel,
					size=self.on_active_channel)

	def on_press(self,o=None):
		x = [ c for c in self.channel_list if c.active_channel ][0]
		x.active_channel = False
		self.active_channel = True
		self.do_selected()

	def on_keyboard_down(self,keyboard,keycode, text, modifiers):
		print('key=',keycode,'text=',text,'modifiers=', modifiers)
		if not self.active_channel:
			return
		x = [ c for c in self.channel_list if c.active_channel][0]
		if keycode[1] == 'left':
			x.active_previous()
		elif keycode[1] == 'right':
			x.active_next()
		elif keycode[1] == 'enter':
			x.do_selected()
		else:
			return False
		return True

	def active_previous(self):
		i = self.channel_list.index(self)
		x = i - 1
		if x < 0:
			x = len(self.channel_list) - 1
		self.active_channel = False
		self.channel_list[x].active_channel = True

	def active_next(self):
		i = self.channel_list.index(self)
		x = i + 1
		if x >= len(self.channel_list):
			x = 0
		self.active_channel = False
		self.channel_list[x].active_channel = True

	def do_selected(self):
		app = App.get_running_app()
		if platform == 'android':
			url = "%s?src_url=%s&src_name=%s" % ( \
					absurl('play.html.tmpl',self.parenturl) 
					,self.url, self.channel_name) 
			print('on_selected():url=',url)
			x = WebKitPlayer(url=url)
			app.root.add_widget(x)
			return
		else:
			desc = {
				"widgettype":"VPlayer",
				"options":{
					"vfile":self.url
				}
			}
			x = app.blocks.widgetBuild(desc)
			if x is not None:
				app.root.add_widget(x)
			else:
				alert(str(desc)+':create widget error')


	def on_active_channel(self,o=None,v=None):
		if self.active_channel:
			c = [0.3,0.3,1,1]
		else:
			c = [0.3,0.3,0.3,1]
		self.setBGColor(c)

	def setBGColor(self,c):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(*c)
			Rectangle(pos=self.pos,size=self.size)
