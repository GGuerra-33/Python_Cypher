#Reemplazar "file_path" con la dirección del archivo que quieres encriptar o desencriptar
import sys
import hashlib
import base64

def encrypt_file(file_path):
    file = open(file_path)
    data = file.read()
    file.close()

    key = hashlib.sha256(b"1234567890123456").digest()

    ciphertext = base64.b64encode(hashlib.pbkdf2_hmac('sha256', data.encode(), key, 100000))

    new_file_path = file_path + ".enc"
    new_file = open(new_file_path, "wb")

    new_file.write(ciphertext)
    new_file.close()

    print("Archivo encriptado correctamente")

def decrypt_file(file_path):
    file = open(file_path, "rb")
    data = file.read()
    file.close()

    key = hashlib.sha256(b"1234567890123456").digest()

    plaintext = hashlib.pbkdf2_hmac('sha256', base64.b64decode(data), key, 100000).decode()

    new_file_path = file_path.replace(".enc", "")
    new_file = open(new_file_path, "w")

    new_file.write(plaintext)
    new_file.close()

    print("Archivo desencriptado correctamente")

if __name__ == "__main__":
    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "encrypt":
        encrypt_file(file_path)
    elif action == "decrypt":
        decrypt_file(file_path)
    else:
        print("Invalid action. Please use 'encrypt' or 'decrypt'.")
