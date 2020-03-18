import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"
import sys
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.logger import Logger
from appPublic.folderUtils import ProgramPath
from appPublic.jsonConfig import getConfig
from kivyblocks.blocksapp import appBlocksHack
from kivyblocks.blocks import registerWidget
from kivyblocks.pagescontainer import PageContainer

from channelbox import ChannelBox
from livetv import LiveTV
from songviewer import SongViewer
from picviewer import PicViewer
from movieviewer import MovieViewer

class MyApp(App):
	def build(self):
		x = PageContainer()
		Clock.schedule_once(self.build1,0)
		return x

	def build1(self,t=None):
		x = None
		config = getConfig()
		Logger.info('*****************Use Intranet IP***********************')
		config.uihome = config.uihome_local
		x = self.blocks.widgetBuild(config.root)
		if x is None:
			config.uihome = config.uihome_internet
			Logger.info('*****************Use Internet IP***********************')
			x = self.blocks.widgetBuild(config.root)
			if x is None:
				alert(str(self.config.root)+': cannt build widget')
		self.root.add_widget(x)
		return 
	
if __name__ == '__main__':
	pp = ProgramPath()
	workdir = pp
	if len(sys.argv) > 1:
		workdir = sys.argv[1]
	print('ProgramPath=',pp,'workdir=',workdir)
	config = getConfig(workdir,NS={'workdir':workdir,'ProgramPath':pp})
	registerWidget('LiveTV',LiveTV)
	registerWidget('SongViewer',SongViewer)
	registerWidget('MovieViewer',MovieViewer)
	registerWidget('PicViewer',PicViewer)
	registerWidget('ChannelBox', ChannelBox)
	myapp = MyApp()
	appBlocksHack(myapp)
	myapp.run()

