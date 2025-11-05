import json
import re


class Aerolinea:
    def __init__(self, nombre, codigo_iata, codigo_icao):
        self.nombre = nombre
        self.codigo_iata = codigo_iata
        self.codigo_icao = codigo_icao

    def __str__(self):
        codigo = self.codigo_iata or self.codigo_icao or "N/A"
        return f"{self.nombre} ({codigo})"


class Aeronave:
    def __init__(self, matricula, codigo_iata, codigo_icao):
        self.matricula = matricula if self._matricula_valida(matricula) else "Matrícula inválida"
        self.codigo_iata = codigo_iata
        self.codigo_icao = codigo_icao

    def _matricula_valida(self, matricula):
        if not matricula or matricula == "N/A":
            return False
        return bool(re.match(r"^[A-Z]{1,2}-[A-Z0-9]{3,5}$", matricula))

    def es_uruguaya(self):
        return bool(re.match(r"^CX-[A-Z]{3}$", self.matricula))

    def __str__(self):
        bandera = "🇺🇾" if self.es_uruguaya() else ""
        return f"{self.matricula} {bandera}".strip()


class Aeropuerto:
    """Representa un aeropuerto con validación de código ICAO."""

    def __init__(self, nombre, codigo_iata, codigo_icao, pais):
        self.nombre = nombre
        self.codigo_iata = codigo_iata
        self.codigo_icao = codigo_icao if self._icao_valido(codigo_icao) else "Código ICAO inválido"
        self.pais = pais

    def _icao_valido(self, codigo):
        """Valida código ICAO compuesto por 4 letras."""
        return bool(re.match(r"^[A-Z]{4}$", str(codigo)))

    def __str__(self):
        return f"{self.nombre} ({self.codigo_icao}) - {self.pais}"


class Vuelo:
    """Representa un vuelo básico."""

    def __init__(self, numero_vuelo, aerolinea, aeronave, salida, llegada, estado):
        self.numero_vuelo = numero_vuelo if self._numero_vuelo_valido(numero_vuelo) else "Código inválido"
        self.aerolinea = aerolinea
        self.aeronave = aeronave
        self.salida = salida
        self.llegada = llegada
        self.estado = estado

    def _numero_vuelo_valido(self, numero):
        """Valida formato: 2-3 letras/números + 1-4 dígitos (ej: LA1234)."""
        return bool(re.match(r"^[A-Z0-9]{2,3}\d{1,4}$", str(numero)))

    def mostrar_info(self):
        print(f"✈️ {self.numero_vuelo} - {self.aerolinea}")
        print(f"  Origen: {self.salida}")
        print(f"  Destino: {self.llegada}")
        print(f"  Aeronave: {self.aeronave}")
        print(f"  Estado: {self.estado}")
        print("-" * 40)



with open("vuelos_prueba.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

datos_vuelos = datos.get("data", [])
vuelos = []

for vuelo_json in datos_vuelos:
    datos_aerolinea = vuelo_json.get("airline", {})
    datos_aeronave = vuelo_json.get("aircraft", {})
    datos_salida = vuelo_json.get("departure", {})
    datos_llegada = vuelo_json.get("arrival", {})

    aerolinea = Aerolinea(
        datos_aerolinea.get("name", "Desconocida"),
        datos_aerolinea.get("iata"),
        datos_aerolinea.get("icao")
    )

    aeronave = Aeronave(
        datos_aeronave.get("registration", "N/A"),
        datos_aeronave.get("iata", "N/A"),
        datos_aeronave.get("icao", "N/A")
    )

    salida = Aeropuerto(
        datos_salida.get("airport", "N/A"),
        datos_salida.get("iata", "N/A"),
        datos_salida.get("icao", "N/A"),
        datos_salida.get("country", "N/A")
    )

    llegada = Aeropuerto(
        datos_llegada.get("airport", "N/A"),
        datos_llegada.get("iata", "N/A"),
        datos_llegada.get("icao", "N/A"),
        datos_llegada.get("country", "N/A")
    )

    vuelo = Vuelo(
        numero_vuelo=vuelo_json.get("flight", {}).get("iata", "Sin número"),
        aerolinea=aerolinea,
        aeronave=aeronave,
        salida=salida,
        llegada=llegada,
        estado=vuelo_json.get("flight_status", "desconocido")
    )

    vuelos.append(vuelo)

