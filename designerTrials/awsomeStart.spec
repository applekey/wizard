# -*- mode: python -*-
a = Analysis(['awsomeStart.py'],
             pathex=['uiLib', 'componentConfiguration', 'contentPage', 'imageFiles', 'C:\\Users\\applekey\\Desktop\\designerTrials'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
		  Tree('imageFiles',prefix='imageFiles'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MeshWiz.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
