import os
import pyaes

file_name = "teste.txt.ransomwaretroll"

with open(file_name, "rb") as file:
    file_data = file.read()

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file_name = file_name.replace(".ransomwaretroll", "")
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"Arquivo '{file_name}' descriptografado como '{new_file_name}'.")
