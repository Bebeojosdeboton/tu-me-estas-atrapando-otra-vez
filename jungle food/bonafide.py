import json
# Desayunos Opciones
datos_lugares = [
    {
        "Nombre": "Bonafide Colón y Cañada",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Cafe, Queso, Bebidas.",
        "Precio minimo": "$2000",
        "Precio Maximo": "$6000",
        "Disponibilidad": "Lunes a viernes 7 a 22 hs\nSábado y Domingo 7:30 a 22hs",
        "Id Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("bonafide.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)