# Crea un software che stampi il nome del tasto cliccato su tastiera (solo lettere)
# Usa la libreria: pynput

from pynput import keyboard

def on_press(key):
    try:
        # Controlla se il tasto è una lettera
        if hasattr(key, 'char') and key.char is not None:
            print(f'Tasto premuto: {key.char}')
    except Exception as e:
        print(f'Errore: {e}')

def on_release(key):
    # Ferma l'ascolto se viene premuto il tasto ESC
    if key == keyboard.Key.esc:
        return False

# Inizia l'ascolto della tastiera
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
