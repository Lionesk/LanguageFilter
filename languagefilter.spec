# -*- mode: python -*-
a = Analysis(['languagefilter.py'],
             pathex=['/home/emilio/work/LanguageFilter'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='languagefilter',
          debug=False,
          strip=None,
          upx=True,
          console=True )
