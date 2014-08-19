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

    return extra_datas
###########################################

# -*- mode: python -*-
a = Analysis(['awsomeStart.py'],
             pathex=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('pageConfiguration.json',"C:\\Users\\applekey2\\Documents\\wizard\\pythonProject\\pageConfiguration.json", 'DATA')]
a.datas += extra_datas('C:/Users/applekey2/Documents/wizard/pythonProject/componentConfiguration/')
a.datas += extra_datas('C:/Users/applekey2/Documents/wizard/pythonProject/contentPage/')
a.datas += extra_datas('C:/Users/applekey2/Documents/wizard/pythonProject/extensionController/')
a.datas += extra_datas('C:/Users/applekey2/Documents/wizard/pythonProject/meshController/')
a.datas += extra_datas('C:/Users/applekey2/Documents/wizard/pythonProject/uiLib/')


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
          console=True )
