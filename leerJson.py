import json

file_name = "data.json"

with open(file_name) as data:
    datos= json.load(data)

print(datos["SO"]+"\n"+datos["hostname"]+"\n"+datos["ip"])
print(datos["Version"][0])
print(datos["Version"][4])
print(datos["Version"][5])

