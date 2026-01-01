# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import os, sys

# ========= CONFIG À ADAPTER (Windows) =========
APP_NAME = "ARRERA OPALE"
ENTRY_SCRIPT = "main.py"
ICON_FILE = None
UPX_ENABLED = True
DEBUG_BUILD = False
HIDDENIMPORTS = []
EXCLUDES = []
# ========= FIN CONFIG =========

block_cipher = None

# Sécurité: ce .spec ne doit être utilisé que sous Windows
if not sys.platform.startswith("win"):
    raise SystemExit("Ce fichier .spec est prévu uniquement pour Windows.")

PROJECT_ROOT = os.path.abspath(".")

# -----------------------------------------------------------
# AJOUT POUR LLAMA CPP
# On récupère automatiquement les binaires, les datas et les imports cachés
# -----------------------------------------------------------
tmp_ret = collect_all('llama_cpp')
datas_llama, binaries_llama, hiddenimports_llama = tmp_ret

# On fusionne avec vos listes existantes
HIDDENIMPORTS += hiddenimports_llama

# --- Ajout des dossiers asset, config, keyword, language ---
extra_datas = []
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        extra_datas.append((source_path, folder))

final_datas = datas_llama + extra_datas

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=binaries_llama,      # Ajout des binaires llama
    datas=final_datas,            # Ajout des fichiers de données (lib, etc.)
    hiddenimports=HIDDENIMPORTS,
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
    console=False, # Mettre à True si vous voulez voir les erreurs au lancement pour tester
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