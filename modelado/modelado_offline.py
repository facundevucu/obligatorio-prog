import json

#Abro el archivo local
with open("modelado/vuelos_prueba.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Funcion para mostrar los vuelos
def mostrar_vuelos(lista_vuelos, tipo):
    print(f"\n --- {tipo.upper()} ---")
    for vuelo in lista_vuelos:
        ident = vuelo.get("ident", "???")

        origen_data = vuelo.get("origin") or {}
        destino_data = vuelo.get("destination") or {}

        origen = origen_data.get("code", "N/A")
        destino = destino_data.get("code", "N/A")

        estado = vuelo.get("status", "Desconocido")
        print(f"{ident} | {origen} → {destino} | {estado}")

#Muestro los resultados filtrados
mostrar_vuelos(data.get("arrivals", []), "Llegadas")
mostrar_vuelos(data.get("departures", []), "Salidas")
mostrar_vuelos(data.get("scheduled_arrivals", []), "Programados")