import tkinter
import hashlib
import base64

window = tkinter.Tk()
window.title("Encriptador")
window.geometry("300x200")
window.config(bg="black")

def encrypt_file(event):
    file_path = event.widget.tk.call("selection", "get")
    file = open(file_path)
    data = file.read()
    file.close()

    key = hashlib.sha256(b"1234567890123456").digest()

    ciphertext = base64.b64encode(hashlib.pbkdf2_hmac('sha256', data.encode(), key, 100000))

    new_file_path = file_path + ".enc"
    new_file = open(new_file_path, "wb")

    new_file.write(ciphertext)
    new_file.close()

    message = tkinter.Label(window, text="Archivo encriptado correctamente", fg="green", bg="black")
    message.pack()

def decrypt_file(event):
    file_path = event.widget.tk.call("selection", "get")
    file = open(file_path, "rb")
    data = file.read()
    file.close()

    key = hashlib.sha256(b"1234567890123456").digest()

    plaintext = hashlib.pbkdf2_hmac('sha256', base64.b64decode(data), key, 100000).decode()

    new_file_path = file_path.replace(".enc", "")
    new_file = open(new_file_path, "w")

    new_file.write(plaintext)
    new_file.close()

    message = tkinter.Label(window, text="Archivo desencriptado correctamente", fg="green", bg="black")
    message.pack()

def show_instruction():
    instruction = tkinter.Label(window, text="Arrastra y suelta el archivo que deseas encriptar o desencriptar", fg="white", bg="black") 
    instruction.pack()

window.bind("<B1-Motion>", encrypt_file)
window.bind("<B3-Motion>", decrypt_file)
show_instruction()

window.mainloop()
