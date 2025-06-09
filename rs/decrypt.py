import pyaes

# FILE
filename = "image.png.pyransom"
KEY = b"0123456789123456"

with open(filename, "rb") as file:
    content = file.read()

# REMOVE FILENAME
decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(content)

new_filename = filename.replace(".pyransom","")
with open(new_filename, "wb") as file:
    file.write(decrypt_data)
