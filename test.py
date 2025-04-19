import win32gui
import win32con
import time

# Trouver la fenêtre PokeMMO
def get_pokemmo_hwnd():
    def enum_windows_callback(hwnd, wildcard):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "Poke" in title:  # On vérifie le titre de la fenêtre
                handles.append(hwnd)
    handles = []
    win32gui.EnumWindows(enum_windows_callback, None)
    return handles[0] if handles else None

# Fonction pour envoyer la touche 'Up' à la fenêtre
def send_up_arrow(hwnd):
    # Code de la touche 'Up' (flèche haut)
    UP_ARROW_KEY = 0x26  # Scancode pour la touche flèche haut

    # Envoi de la touche 'Up' (flèche haut) - KeyDown
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, UP_ARROW_KEY, 0)
    time.sleep(0.1)  # Petit délai pour simuler une pression réaliste
    # Relâchement de la touche 'Up' - KeyUp
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, UP_ARROW_KEY, 0)

# Main
hwnd = get_pokemmo_hwnd()

if hwnd:
    print(f"Fenêtre trouvée: {hwnd}")
    time.sleep(1)

    # Envoie de la touche 'Up'
    send_up_arrow(hwnd)
    print("Touche 'Up' envoyée à la fenêtre PokeMMO.")
else:
    print("Fenêtre PokeMMO non trouvée.")
