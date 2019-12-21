import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"
import sys
from appPublic.folderUtils import ProgramPath
from appPublic.jsonConfig import getConfig
from kivyblocks.blocksapp import BlocksApp
from kivyblocks.blocks import registerWidget

from channelbox import ChannelBox
from livetv import LiveTV
from songviewer import SongViewer
from picviewer import PicViewer

if __name__ == '__main__':
	pp = ProgramPath()
	workdir = pp
	if len(sys.argv) > 1:
		workdir = sys.argv[1]
	print('ProgramPath=',pp,'workdir=',workdir)
	config = getConfig(workdir,NS={'workdir':workdir,'ProgramPath':pp})
	registerWidget('LiveTV',LiveTV)
	registerWidget('SongViewer',SongViewer)
	registerWidget('PicViewer',PicViewer)
	registerWidget('ChannelBox', ChannelBox)
	myapp = BlocksApp()
	myapp.run()

