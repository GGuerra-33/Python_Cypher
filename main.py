import tkinter
from Crypto.Cipher import AES


window = tkinter.Tk()
window.title("Encriptador")
window.geometry("300x200")
window.config(bg="black")

def encrypt_file(event):
    file_path = event.widget.tk.call("selection", "get")
    file = open(file_path)
    data = file.read()
    file.close()

    key = b"1234567890123456"

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext,tag = cipher.encrypt_and_digest(data)

    new_file_path = file_path + ".enc"
    new_file = open(new_file_path, "wb")

    new_file.write(cipher.nonce)
    new_file.write(tag)
    new_file.write(ciphertext)
    new_file.close()

    message = tkinter.Label(window, text="Archivo encriptado correctamente", fg="green", bg="black")
    message.pack()


def show_instruction():
    instruction = tkinter.Label(window, text="Arrastra y suelta el archivo que deseas encriptar", fg="white", bg="black") 
    instruction.pack()

window.bind("<B1-Motion>", encrypt_file)
show_instruction()

window.mainloop()