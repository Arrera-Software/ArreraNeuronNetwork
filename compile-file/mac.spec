# -*- mode: python ; coding: utf-8 -*-

# ========= CONFIG À ADAPTER =========
APP_NAME = "ARRERA OPALE"               # Nom de l'app .app
ENTRY_SCRIPT = "main.py"                     # Script d'entrée
ICON_ICNS = None           # .icns pour l'icône du dock (ou None)
BUNDLE_ID = "com.arrera.opale"            # Identifiant de bundle macOS
MIN_MACOS = "10.13"                          # Version minimale macOS
TARGET_ARCH = None                           # "arm64" ou "x86_64" si besoin
RESOURCE_EXTS = ["png", "json"]              # Extensions à embarquer comme ressources
# ========= FIN CONFIG =========

import os, glob

block_cipher = None
PROJECT_ROOT = os.path.abspath(".")

EXCLUDE_DIRS = {"build", "dist", ".git", "__pycache__"}

def is_excluded(path):
    # Exclut si un segment de chemin correspond à une entrée d'exclusion
    parts = set(os.path.normpath(path).split(os.sep))
    return any(x in parts for x in EXCLUDE_DIRS)

def collect_files_by_ext(root, exts):
    # Recherche récursive, insensible à la casse
    files = []
    patterns = []
    for ext in exts:
        patterns.append(glob.glob(os.path.join(root, "**", f"*.{ext}"), recursive=True))
        patterns.append(glob.glob(os.path.join(root, "**", f"*.{ext.upper()}"), recursive=True))
    for group in patterns:
        for p in group:
            if os.path.isfile(p) and not is_excluded(p):
                files.append(os.path.normpath(p))
    # Déduplique en préservant l'ordre
    seen, unique = set(), []
    for p in files:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique

# Collecte des ressources (PNG, JSON, etc.)
resource_files = collect_files_by_ext(PROJECT_ROOT, RESOURCE_EXTS)

# Construit "datas" en préservant l'arborescence relative.
# IMPORTANT: remplace "" par "." pour les fichiers à la racine.
datas = []
for fp in resource_files:
    relpath = os.path.relpath(fp, PROJECT_ROOT)
    dest = os.path.dirname(relpath) or "."   # <-- le correctif principal
    datas.append((fp, dest))

# Ajoute le fichier VERSION situé à la racine (s'il existe)
version_file = os.path.join(PROJECT_ROOT, "VERSION")
if os.path.isfile(version_file):
    datas.append((version_file, "."))  # ira dans Contents/Resources/

# Si tu as des imports dynamiques, renseigne-les ici (sinon laisse vide)
hiddenimports = [
    "pyaudio",
    "sounddevice",
    "AppKit", "Foundation", "objc",
]

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[PROJECT_ROOT],
    binaries=[],
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
    upx=True,                    # désactive si UPX n'est pas installé sur ta machine
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,               # pas de fenêtre terminal
    disable_windowed_traceback=False,
    target_arch=TARGET_ARCH,     # "arm64" ou "x86_64" si tu veux forcer
    codesign_identity=None,      # tu pourras signer plus tard si besoin
    entitlements_file=None,
)

# Lis la version si disponible (pour Info.plist)
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
    "CFBundleShortVersionString": version_str,  # visible dans “Lire les informations”
    "CFBundleVersion": version_str,             # build number
    "LSMinimumSystemVersion": MIN_MACOS,
    "NSHighResolutionCapable": "True",
    # Ajoute ici des clés Info.plist spécifiques à ta GUI (ex: autorisations)
    "NSMicrophoneUsageDescription": "L’application a besoin du micro pour enregistrer/traiter l’audio.",
}

app = BUNDLE(
    exe,
    name=f"{APP_NAME}.app",
    icon=ICON_ICNS,               # .icns pour l’icône du dock (optionnel)
    bundle_identifier=BUNDLE_ID,
    info_plist=info_plist,
)