import subprocess
import psutil

com = "ifconfig"
a = subprocess.Popen(com, shell=True)
b = a.wait()

mem = psutil.virtual_memory()
print("PC Memory status:\n", mem)

with open('version.txt', 'r') as file:
    file_data = file.read()
    file_data = file_data.replace('1.1', '1.2')

with open('version.txt', 'w') as file:
    file.write(file_data)
