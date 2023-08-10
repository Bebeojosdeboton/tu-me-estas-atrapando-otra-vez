import json
# Cordoba
datos_ciudad = [
    {
        "Nombre": "Ciudad de Cordoba",
        "Caracteristica": "es conocida por su arquitectura colonial española. Alberga la Manzana Jesuítica, un complejo del siglo XVII con claustros activos, iglesias y el campus original de la Universidad Nacional de Córdoba, una de las universidades más antiguas de Sudamérica. El punto central de la ciudad es la Plaza San Martín y la Catedral de Córdoba de estilo neobarroco."
 },       
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_ciudad, indent=2)

# Guardar la cadena JSON en un archivo
with open("cordoba.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)