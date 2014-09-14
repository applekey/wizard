# -*- mode: python -*-
a = Analysis(['abcdefgh.py'],
             pathex=['C:\\Users\\applekey\\Desktop\\test'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='abcdefgh.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
