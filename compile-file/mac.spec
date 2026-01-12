# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_all

# ========= CONFIGURATION =========
APP_NAME = "ARRERA OPALE"
ENTRY_SCRIPT = "main.py"
ICON_ICNS = None  # Mets le chemin vers ton icone.icns si tu en as une, ex: "asset/icon.icns"
BUNDLE_ID = "com.arrera.opale"
MIN_MACOS = "10.13"
TARGET_ARCH = None
# =================================

PROJECT_ROOT = os.path.abspath(".")

# --- PARTIE 1 : FONCTION DE COLLECTE INTELLIGENTE ---
def collect_data_recursive_no_py(folders_list):
    """
    Parcourt récursivement les dossiers donnés, ajoute tous les fichiers
    SAUF les fichiers .py, .pyc et .DS_Store.
    Garde la structure des dossiers.
    """
    collected_datas = []

    for folder_name in folders_list:
        source_folder = os.path.join(PROJECT_ROOT, folder_name)

        if not os.path.exists(source_folder):
            print(f"⚠️ Attention : Le dossier '{folder_name}' n'existe pas, ignoré.")
            continue

        for root, dirs, files in os.walk(source_folder):
            for file in files:
                # 🚫 ON EXCLUT LES FICHIERS PYTHON ET SYSTÈME
                if file.endswith(('.py', '.pyc', '.DS_Store')):
                    continue

                # Chemin complet du fichier source
                full_source_path = os.path.join(root, file)

                # On calcule le dossier de destination pour garder la structure
                # Ex: si fichier est dans 'language/vouvoiment/dict.json'
                # rel_path sera 'language/vouvoiment'
                rel_path = os.path.relpath(root, PROJECT_ROOT)

                collected_datas.append((full_source_path, rel_path))

    return collected_datas

# --- PARTIE 2 : PREPARATION DES DONNÉES ---
datas = []
binaries = []

# 2.1 Collecte des dossiers demandés (sans les .py)
# Note : 'language' inclura automatiquement 'vouvoiment' et 'tutoiment' grâce à os.walk
target_folders = ['asset', 'config', 'keyword', 'language']
datas += collect_data_recursive_no_py(target_folders)

# 2.2 Fichier VERSION (s'il existe à la racine)
version_file = os.path.join(PROJECT_ROOT, "VERSION")
if os.path.isfile(version_file):
    datas.append((version_file, "."))

# 2.3 LLAMA CPP (Gestion des binaires si présents)
try:
    llama_datas, llama_binaries, llama_hiddenimports = collect_all('llama_cpp')
    datas += llama_datas
    binaries += llama_binaries
except Exception:
    llama_hiddenimports = []

# --- PARTIE 3 : CONFIGURATION TECHNIQUE ---

# Modules à exclure totalement (pour éviter tes crashs précédents)
excludes_modules = [
    "tensorflow",
    "tensorflow_estimator",
    "tensorboard",
    "keras",
    "cv2",
    "torch"
]

# Imports nécessaires mais parfois non détectés
hiddenimports = [
    "pyaudio", "sounddevice", "AppKit", "Foundation", "objc",
    "numpy", "google.protobuf", "PIL", "PIL.Image", "tkinter", "customtkinter"
] + llama_hiddenimports

# --- PARTIE 4 : BUILD ---
block_cipher = None

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes_modules,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # Application graphique (fenêtrée)
    disable_windowed_traceback=False,
    target_arch=TARGET_ARCH,
    codesign_identity=None,
    entitlements_file=None,
)

# Infos pour le fichier Info.plist dans le .app
version_str = "1.0.0"
try:
    with open(version_file, "r", encoding="utf-8") as f:
        version_str = f.read().strip() or version_str
except Exception:
    pass

info_plist = {
    "CFBundleName": APP_NAME,
    "CFBundleDisplayName": APP_NAME,
    "CFBundleIdentifier": BUNDLE_ID,
    "CFBundleShortVersionString": version_str,
    "CFBundleVersion": version_str,
    "LSMinimumSystemVersion": MIN_MACOS,
    "NSHighResolutionCapable": "True",
    "NSMicrophoneUsageDescription": "Cette application utilise le microphone pour la reconnaissance vocale.",
    "LSEnvironment": {
        "LANG": "fr_FR.UTF-8",
        "LC_ALL": "fr_FR.UTF-8"
    }
}

app = BUNDLE(
    exe,
    name=f"{APP_NAME}.app",
    icon=ICON_ICNS,
    bundle_identifier=BUNDLE_ID,
    info_plist=info_plist,
)