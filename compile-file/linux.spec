# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all  # <--- IMPORT IMPORTANT

# ========= CONFIG À ADAPTER (Linux, Arch x86_64) =========
APP_NAME = "ARRERA_OPALE"
ENTRY_SCRIPT = "main.py"
ICON_FILE = None
UPX_ENABLED = True
DEBUG_BUILD = False
HIDDENIMPORTS = []
EXCLUDES = []
# ========= FIN CONFIG =========

import os
block_cipher = None

PROJECT_ROOT = os.path.abspath(".")

# --- ÉTAPE 1 : Récupérer tout ce qui concerne llama_cpp ---
# Cela va chercher les .so, les dépendances et les imports cachés
# Note : on utilise 'llama_cpp' car c'est le nom du package importé dans le code
tmp_ret = collect_all('llama_cpp')

# On sépare les résultats pour les ajouter à l'Analysis
llama_datas = tmp_ret[0]
llama_binaries = tmp_ret[1]
llama_hiddenimports = tmp_ret[2]

# On ajoute tes imports manuels s'il y en a
final_hiddenimports = HIDDENIMPORTS + llama_hiddenimports

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=llama_binaries,      # <--- AJOUT DES BINAIRES LLAMA
    datas=llama_datas,            # <--- AJOUT DES DATAS LLAMA
    hiddenimports=final_hiddenimports, # <--- AJOUT DES IMPORTS CACHÉS
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=DEBUG_BUILD,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True, # Si tu as encore des erreurs, passe à True temporairement pour voir les logs au lancement
    disable_windowed_traceback=False,
    icon=ICON_FILE,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=UPX_ENABLED,
    upx_exclude=[],
    name=APP_NAME,
)