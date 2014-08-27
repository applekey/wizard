##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
                print d
            else:
              print 'blah\n'
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))
   
    print '\n'
    return extra_datas
###########################################
# -*- mode: python -*-
a = Analysis(['awsomeStart.py'],
             pathex=['componentConfiguration',
             'contentPage',
             'meshController',
             'extensionController',
             'uiLib',
             'meshController/implementation',
             'meshController/pythonApi',
             'htmlPages'
             ],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += extra_datas('componentConfiguration/')
a.datas += extra_datas('contentPage/')
a.datas += extra_datas('extensionController/')
a.datas += extra_datas('meshController/')
a.datas += extra_datas('uiLib/')


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wiz.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

coll = COLLECT(exe,
               Tree('imageFiles',prefix='imageFiles'),
               Tree('htmlPages',prefix='htmlPages'),            
               strip=None,
               upx=True,
               name='awsomeStart')




