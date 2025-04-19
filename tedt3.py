import time
import keyboard
import pygetwindow as gw
import ctypes
import win32gui
import win32con

# Unicode pour la flèche "Up"
UP_ARROW_UNICODE = "\u2191"  # Symbole flèche haut

# Fonction pour envoyer la touche "Up" (flèche haut)
def send_up_arrow():
    # Utiliser le code Unicode pour "Up"
    keyboard.write(UP_ARROW_UNICODE)
    time.sleep(0.1)

# Récupérer le handle de la fenêtre PokeMMO
def get_pokemmo_hwnd():
    # Recherche de la fenêtre par le titre
    window_title = "PokeМMO"
    hwnd = None
    for window in gw.getWindowsWithTitle(window_title):
        if window.title == window_title:
            hwnd = window._hWnd
            break
    return hwnd

# Mettre la fenêtre en avant-plan
def bring_window_to_foreground(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restaurer la fenêtre si elle est minimisée
    win32gui.SetForegroundWindow(hwnd)

# Main execution
hwnd = get_pokemmo_hwnd()

if hwnd:
    print(f"Fenêtre PokeMMO trouvée: {hwnd}")
    bring_window_to_foreground(hwnd)

    # Envoi de la touche 'Up'
    send_up_arrow()
    print("Touche 'Up' envoyée à la fenêtre PokeMMO.")
else:
    print("Fenêtre PokeMMO non trouvée.")
