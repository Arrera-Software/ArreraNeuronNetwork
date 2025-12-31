# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os

# ========= CONFIG =========
APP_NAME = "ARRERA_OPALE"
ENTRY_SCRIPT = "main.py"
ICON_FILE = None
UPX_ENABLED = True
DEBUG_BUILD = False
HIDDENIMPORTS = []
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None
PROJECT_ROOT = os.path.abspath(".")

# --- Récupération de llama_cpp ---
tmp_ret = collect_all('llama_cpp')
llama_datas = tmp_ret[0]
llama_binaries = tmp_ret[1]
llama_hiddenimports = tmp_ret[2]

final_hiddenimports = HIDDENIMPORTS + llama_hiddenimports

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=llama_binaries,
    datas=llama_datas,
    hiddenimports=final_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --- MODE ONE-DIR (Dossier) ---
# L'EXE ne contient que le script de démarrage, pas les bibliothèques
exe = EXE(
    pyz,
    a.scripts,
    [], # <-- VIDE : On ne met pas les binaires ici
    exclude_binaries=True, # <-- IMPORTANT : On sépare les binaires
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=True,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True, # Mettre à True pour voir les erreurs au début, False pour la prod
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_FILE,
)

# --- SECTION COLLECT (Création du dossier) ---
# C'est ici que tout est rassemblé dans un dossier dist/ARRERA_OPALE
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=UPX_ENABLED,
    upx_exclude=[],
    name=APP_NAME
)