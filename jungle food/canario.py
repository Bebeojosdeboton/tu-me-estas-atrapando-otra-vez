import json
# bares y pubs Opciones
datos_lugares = [
    { "Nombre": "Canario Negro",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Cena,Bebidas",
    "Precio minimo": "$6000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "",
    "Id Ubicacion":"Rondeau 155"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("canario.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)