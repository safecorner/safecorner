# -*- mode: python ; coding: utf-8 -*-
import os
from kivy_deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal,hookspath
from PyInstaller.utils.hooks import collect_submodules
import kivyblocks
blockspath=os.path.dirname(kivyblocks.__file__)

import ffpyplayer
import PIL

block_cipher = None
excludekivy = get_deps_minimal(video=['ffpyplayer'], audio=['ffpyplayer'],spelling=None,camera=None)['excludes']

a = Analysis(['main.py'],
             pathex=['E:\\share\\py\\safecorner'],
             binaries=[],
             datas=[
				('%s/ttf/*.ttf' %  blockspath, './kivyblocks/ttf'),
				('%s/imgs/*.png' % blockspath, './kivyblocks/imgs'),
				('%s/imgs/*.jpg' % blockspath, './kivyblocks/imgs'),
				('%s/imgs/*.gif' % blockspath, './kivyblocks/imgs')
			 ],
             hiddenimports=[
			 	"ffpyplayer.threading",
				"ffpyplayer.player",
				"ffpyplayer.player.queue",
				"ffpyplayer.player.core",
				"ffpyplayer.player.clock",
				"ffpyplayer.player.decoder",
				"ffpyplayer.player.player",
				"ffpyplayer.player.frame_queue",
				"ffpyplayer.tools",
				"ffpyplayer.pic",
				"ffpyplayer.writer"
			 ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
			a.scripts,
			a.binaries,
			a.zipfiles,
			a.datas,
			*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins )],
			[],
			name='safecorner',
			debug=False,
			bootloader_ignore_signals=False,
			strip=False,
			upx=True,
			upx_exclude=[],
			runtime_tmpdir=None,
			console=True )
