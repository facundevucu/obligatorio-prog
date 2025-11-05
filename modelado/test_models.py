# ejercicio 1.3 de la semana 2

from models import Aerolinea, Aeronave, Aeropuerto, Vuelo
import json

#cargar json real de vuelos
with open("vuelos_prueba.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#tomo los primeros 5 vuelos reales
arrivals = data["arrivals"][:5]  

vuelos_objetos = []

for vuelo_data in arrivals:

    aerolinea = Aerolinea(
        vuelo_data.get("operator"),
        vuelo_data.get("operator_iata"),
        vuelo_data.get("operator_icao")
    )

    aeronave = Aeronave(
        vuelo_data.get("registration"),
        vuelo_data.get("aircraft_type"),
        vuelo_data.get("aircraft_type")
    )

    origen_data = vuelo_data.get("origin", {})
    destino_data = vuelo_data.get("destination", {})

    origen = Aeropuerto(
        origen_data.get("city"),
        origen_data.get("code_iata"),
        origen_data.get("code_icao"),
        origen_data.get("name")
    )

    destino = Aeropuerto(
        destino_data.get("city"),
        destino_data.get("code_iata"),
        destino_data.get("code_icao"),
        destino_data.get("name")
    )

    vuelo = Vuelo(
        vuelo_data.get("ident"),
        aerolinea,
        aeronave,
        origen,
        destino,
        vuelo_data.get("status")
    )

    vuelos_objetos.append(vuelo)

print("\n--vuelos de llegada--\n")
for v in vuelos_objetos:
    v.mostrar_info()
