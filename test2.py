import win32gui
import win32con
import time

# Trouver la fenêtre PokeMMO (attention aux caractères bizarres)
def get_pokemmo_hwnd():
    def enum_windows_callback(hwnd, wildcard):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "Poke" in title:
                handles.append(hwnd)
    handles = []
    win32gui.EnumWindows(enum_windows_callback, None)
    return handles[0] if handles else None

hwnd = get_pokemmo_hwnd()

if hwnd:
    print(f"Fenêtre trouvée: {hwnd}")
    time.sleep(1)

    # Utiliser le code virtuel pour la flèche "Up"
    UP_ARROW = 0x56

    # Appuyer sur la touche fléchée vers le haut
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, UP_ARROW, 0)
    time.sleep(0.1)

    # Relâcher la touche fléchée vers le haut
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, UP_ARROW, 0)

    print("Flèche 'Up' envoyée à la fenêtre PokeMMO.")
else:
    print("Fenêtre PokeMMO non trouvée.")
