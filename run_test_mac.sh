#!/bin/bash

echo "🧹 Nettoyage total des dossiers 'build' et 'dist'..."
rm -rf build dist

choix=$1

# Si aucun argument n'a été fourni, on affiche le menu interactif
if [ -z "$choix" ]; then
    echo "======================================"
    echo "    MENU DE COMPILATION ET LANCEMENT  "
    echo "======================================"
    echo "1. Lancer main (ARRERA OPALE)"
    echo "2. Lancer test-fnc"
    echo "3. Lancer test-gui"
    echo "4. Lancer test-user-setting"
    echo "======================================"
    read -p "Choix : " choix
fi

case $choix in
    1|main)
        echo "🛠️  Compilation de main (ARRERA OPALE)..."
        pyinstaller --clean compilation_mac/test_main.spec
        echo "🚀 Lancement de l'application graphique dans le terminal..."
        "./dist/ARRERA OPALE.app/Contents/MacOS/ARRERA OPALE"
        ;;
    2|test-fnc)
        echo "🛠️  Compilation de test-fnc..."
        pyinstaller --clean compilation_mac/test-fnc.spec
        echo "🚀 Lancement de test-fnc dans le terminal..."
        ./dist/test-fnc.app/Contents/MacOS/test-fnc
        ;;
    3|test-gui)
        echo "🛠️  Compilation de test-gui..."
        pyinstaller --clean compilation_mac/test-gui.spec
        echo "🚀 Lancement de l'application graphique test-gui dans le terminal..."
        "./dist/Test-GUI.app/Contents/MacOS/Test-GUI"
        ;;
    4|test-user-setting)
        echo "🛠️  Compilation de test-user-setting..."
        pyinstaller --clean compilation_mac/test-user-setting.spec
        echo "🚀 Lancement de test-user-setting dans le terminal..."
        ./dist/Test-User-Setting.app/Contents/MacOS/Test-User-Setting
        ;;
    *)
        echo "❌ Choix invalide. Arguments acceptés : 1, 2, 3, 4 ou main, test-fnc, test-gui, test-user-setting"
        ;;
esac
