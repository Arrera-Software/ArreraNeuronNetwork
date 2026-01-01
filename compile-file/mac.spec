# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import glob
from PyInstaller.utils.hooks import collect_all

# ========= CONFIGURATION =========
APP_NAME = "ARRERA OPALE"
ENTRY_SCRIPT = "main.py"
ICON_ICNS = None
BUNDLE_ID = "com.arrera.opale"
MIN_MACOS = "10.13"
TARGET_ARCH = None
RESOURCE_EXTS = ["png", "json"]
# =================================

PROJECT_ROOT = os.path.abspath(".")

# --- PARTIE 1 : VERIFICATION TENSORFLOW ---
try:
    import tensorflow
    tf_init_path = tensorflow.__file__
    tf_root = os.path.dirname(tf_init_path)
    site_packages_root = os.path.dirname(tf_root)
    print(f"\n✅ TensorFlow détecté : {tf_root}")
except ImportError:
    print("\n❌ ERREUR : TensorFlow introuvable. Vérifiez votre venv.")
    sys.exit(1)

# --- PARTIE 2 : FONCTIONS ---
EXCLUDE_DIRS = {"build", "dist", ".git", "__pycache__", "tests"}

def is_excluded(path):
    parts = set(os.path.normpath(path).split(os.sep))
    return any(x in parts for x in EXCLUDE_DIRS)

def collect_files_by_ext(root, exts):
    files = []
    patterns = []
    for ext in exts:
        patterns.append(glob.glob(os.path.join(root, "**", f"*.{ext}"), recursive=True))
        patterns.append(glob.glob(os.path.join(root, "**", f"*.{ext.upper()}"), recursive=True))
    for group in patterns:
        for p in group:
            if os.path.isfile(p) and not is_excluded(p):
                files.append(os.path.normpath(p))
    seen, unique = set(), []
    for p in files:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique

# --- PARTIE 3 : DONNÉES (DATAS) ---
datas = []
binaries = []

# 3.1 Vos ressources
resource_files = collect_files_by_ext(PROJECT_ROOT, RESOURCE_EXTS)
for fp in resource_files:
    relpath = os.path.relpath(fp, PROJECT_ROOT)
    dest = os.path.dirname(relpath) or "."
    datas.append((fp, dest))

# 3.2 Fichier VERSION
version_file = os.path.join(PROJECT_ROOT, "VERSION")
if os.path.isfile(version_file):
    datas.append((version_file, "."))

# 3.3 COPIE FORCÉE TENSORFLOW & DEPENDANCES
libs_to_force = [
    "tensorflow", "keras", "tensorflow_estimator", "google",
    "absl", "astunparse", "gast", "opt_einsum", "termcolor",
    "wrapt", "flatbuffers"
]
for lib in libs_to_force:
    source_path = os.path.join(site_packages_root, lib)
    if os.path.exists(source_path):
        datas.append((source_path, lib))

# 3.4 CORRECTIF LLAMA
try:
    llama_datas, llama_binaries, llama_hiddenimports = collect_all('llama_cpp')
    datas += llama_datas
    binaries += llama_binaries
    print("✅ Llama CPP : Binaires collectés.")
except Exception as e:
    print(f"⚠️ Info : Pas de module llama_cpp trouvé ou erreur ({e})")
    llama_hiddenimports = []

# --- Ajout des dossiers asset, config, keyword, language ---
for folder in ['asset', 'config', 'keyword', 'language']:
    source_path = os.path.join(PROJECT_ROOT, folder)
    if os.path.exists(source_path):
        datas.append((source_path, folder))

# --- PARTIE 4 : IMPORTS CACHÉS ---
hiddenimports = [
    "pyaudio", "sounddevice", "AppKit", "Foundation", "objc",
    "tensorflow", "numpy", "google.protobuf"
] + llama_hiddenimports

# --- PARTIE 5 : ANALYSE ---
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
    excludes=[],
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
    console=False,
    disable_windowed_traceback=False,
    target_arch=TARGET_ARCH,
    codesign_identity=None,
    entitlements_file=None,
)

# Infos Info.plist
version_str = "0.0.0"
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
    "NSMicrophoneUsageDescription": "L'application a besoin du micro.",
}

app = BUNDLE(
    exe,
    name=f"{APP_NAME}.app",
    icon=ICON_ICNS,
    bundle_identifier=BUNDLE_ID,
    info_plist=info_plist,
)