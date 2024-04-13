from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_api_data():
    api_url = "https://swapi.dev/api/films/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return jsonify("Recuperamos todos los datos del API y los mostramos",data)
    else:
        return jsonify({"error": "No se pudo obtener los datos de la API"})
    
@app.route('/peliculas')
def get_api_data_peliculas():
    api_url = "https://swapi.dev/api/films/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        peliculas = [movie['title'] for movie in data['results']]
        print(peliculas)
        return jsonify("Obtenemos solo el nombre las peliculas de la response, solo para consultar el title, no todos los datos: ",peliculas)
    else:
        return jsonify({"error": "No se pudo obtener los datos de la API"})

@app.route('/<int:episode_id>', methods=['GET'])
def get_movie_details(episode_id):
    api_url = "https://swapi.dev/api/films/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        results = data['results']
        movie_url = "vacio" 
        for movie in results:
            print(movie)
            if movie['episode_id'] == episode_id:
                movie_url = movie['url']
                print("*****",movie_url)
                movie_response = requests.get(movie_url)
                if movie_response.status_code == 200:
                    movie_data = movie_response.json()
                    return jsonify(movie_data)
                else: return jsonify({"error": "No se pudo obtener los datos de la pelicula"})
        if movie_url == "vacio":
            return jsonify({"Pelicula inexistente": "No hay pelicula con ese numero de episodio"})

    else:
        return jsonify({"error": "No se pudo obtener los datos de la API"})

if __name__ == '__main__':
    app.run(debug=True)
