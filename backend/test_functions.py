import json
from functions import normalizar_aerolinea

# 🔹 Cargar el archivo con los datos de vuelos
with open("vuelos_prueba.json", "r", encoding="utf-8") as f:
    data = json.load(f)

arrivals = data.get("arrivals", [])

print("=== AEROLÍNEAS NORMALIZADAS (Primeros 15 vuelos) ===")

# 🔹 Recorremos solo los primeros 15
for vuelo in arrivals[:15]:
    codigo = vuelo.get("operator_iata") or vuelo.get("operator_icao")
    nombre = normalizar_aerolinea(codigo)
    vuelo_id = vuelo.get("ident", "N/A")
    origen = vuelo.get("origin", {}).get("code_iata", "Desconocido")
    destino = vuelo.get("destination", {}).get("code_iata", "Desconocido")

    print(f"{vuelo_id:10} | {codigo or '---':4} → {nombre:35} | {origen} → {destino}")
