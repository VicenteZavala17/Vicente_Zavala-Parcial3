#Vicente Zavala IRC9.2
import requests
url = "https://jsonplaceholder.typicode.com/posts/8"
response = requests.get(url)
if response.status_code == 200:
     data = response.json() 
     print('**********Solicitud Exitosa*************')
     print("Datos: ", data)
else:
    print("Error en la solicitud: ", response.text)
