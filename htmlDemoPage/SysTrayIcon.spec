# -*- mode: python -*-
a = Analysis(['SysTrayIcon.py'],
             pathex=['G:\\github\\wizard\\htmlDemoPage'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SysTrayIcon.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
