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
        

AEROLINEAS_URUGUAY = {
    #LATAM
    "LA": "LATAM Airlines",
    "LXP": "LATAM Express",
    "LAN": "LATAM Chile",

    #aerolíneas Argentinas / Austral
    "AR": "Aerolíneas Argentinas",
    "AUS": "Austral Líneas Aéreas",

    #copa Airlines
    "CM": "Copa Airlines",
    "CMP": "Copa Airlines",

    #avianca
    "AV": "Avianca",
    "AVA": "Avianca Colombia",

    #iberia
    "IB": "Iberia",
    "IBE": "Iberia Líneas Aéreas de España",

    #azul / GOL / TAM Brasil
    "AD": "Azul Linhas Aéreas Brasileiras",
    "AZU": "Azul Linhas Aéreas Brasileiras",
    "G3": "GOL Linhas Aéreas",
    "GLO": "GOL Linhas Aéreas",
    "JJ": "LATAM Brasil",

    #paranair / amaszonas
    "ZP": "Paranair",
    "AZP": "Paranair",
    "Z8": "Amaszonas Uruguay",
    "AZU": "Amaszonas Uruguay",

    #iberia Express / air Europa
    "I2": "Iberia Express",
    "UX": "Air Europa",

    #sky airline
    "H2": "Sky Airline",
    "SKU": "Sky Airline",

    #otros
    "UX": "Air Europa",
    "TA": "TACA",
    "TP": "TAP Air Portugal",
    "AF": "Air France",
    "KL": "KLM",
    "LP": "LATAM Airlines Perú",
    "JZ": "JetSmart Perú",
    "2I": "Star Perú",
    "QCL": "Quick Air Jet Charter",
    "QT": "Avianca Cargo (Tampa Cargo)",
}

def normalizar_aerolinea(codigo: str) -> str:
    """Devuelve el nombre completo de la aerolínea si se conoce, o el código original."""
    if not codigo:
        return "Desconocido"
    return AEROLINEAS_URUGUAY.get(codigo.upper(), codigo)
