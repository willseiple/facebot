# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['/Users/Will/Documents/idmission/code/facebot'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          Tree('reader/data', prefix='data'),
          a.zipfiles,
          a.datas,
          [],
          name='FaceBot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='reader/icon.ico' )
app = BUNDLE(exe,
             name='FaceBot.app',
             icon='reader/icon.icns',
             bundle_identifier='com.idmission.facebot.macos')
