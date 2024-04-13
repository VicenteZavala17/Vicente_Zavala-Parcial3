import requests  # Importa la biblioteca requests

# URL a la que se hará la solicitud GET
url = "https://jsonplaceholder.typicode.com/posts/1"

# Realiza la solicitud GET a la URL especificada
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Si la solicitud fue exitosa, convierte la respuesta a JSON
    data = response.json()  # Obtiene los datos de la respuesta en formato JSON
    print('Solicitud Exitosa')  # Imprime un mensaje indicando que la solicitud fue exitosa
    print("Datos: ", data)  # Imprime los datos obtenidos en formato JSON
else:
    # Si la solicitud no fue exitosa, imprime el mensaje de error
    print("Error en la solicitud: ", response.text)  # Imprime el mensaje de error devuelto por la solicitud
