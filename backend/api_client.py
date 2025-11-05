import requests
import json

BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
API_KEY = "UlHHqAChlmsEAGUv301gaRGqA72PGGEl"

def obtener_vuelos_por_aeropuerto(codigo_aeropuerto, limite=5, tipo="arrivals"):
    url = f"{BASE_URL}/airports/{codigo_aeropuerto}/flights"
    headers = {"x-apikey": API_KEY}
    params = {
        "type": tipo,      # arrivals, departures, enroute, scheduled
        "max_pages": 1,    # 1 sola página
        "howMany": 10  # cantidad máxima de vuelos
    }

    respuesta = requests.get(url, headers=headers, params=params)
    return respuesta.json()



if __name__ == "__main__":
    aeropuerto = "SUMU"  #Codigo del aereopuerto de carrasco
    vuelos = obtener_vuelos_por_aeropuerto(aeropuerto)
    print(vuelos)

    #Guardo los archivos en un json
    with open("modelado/vuelos_prueba.json", "w", encoding="utf-8") as f:
        json.dump(vuelos, f, ensure_ascii=False, indent=2)

    print("\n Datos guardados en vuelos_prueba.json")

