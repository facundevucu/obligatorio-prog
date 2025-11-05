def obtener_vuelos_desde(data, codigo_aereopuerto):
    vuelos = []
    for vuelo in data.get("departures", []):
        #obtiene la lista de departures, si no existe devuelve [], lista vacia
        origen = vuelo.get("origin", {}).get("code", "")
        #entra al diccionario vuelo y saca el valor de code
        if origen == codigo_aereopuerto:
            vuelos.append(vuelo)
    return vuelos

def obtener_vuelos_hacia(data, codigo_aereopuerto):
    vuelos = []
    for vuelo in data.get("arrivals", []):
        destino = vuelo.get("destination", {}).get("code", "")
        if destino == codigo_aereopuerto:
            vuelos.append(vuelo)
    return vuelos

def buscar_vuelo_por_codigo(data, codigo_vuelo):
    for tipo in ["arrivals", "departures", "scheduled_arrivals"]:
        for vuelo in data.get(tipo, []):
            if vuelo.get("ident") == codigo_vuelo:
                return vuelo
    return None

def filtrar_vuelos_por_estado(vuelos, estado):
    filtrados = [v for v in vuelos if estado.lower() in v.get("status", "").lower()]
    return filtrados

import json
def guardar_vuelos_en_json(nombre_archivo, vuelos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(vuelos, f, ensure_ascii = False, indent = 2)
        
    
