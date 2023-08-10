
import json
# Almuerzos Opciones
datos_lugares = [
    {
    "Nombre": "Santa Calma",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Desayuno, Almuerzo, Cena, Brunch, Bebidas",
    "Precio minimo": "$5000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "lunes a Domingo de 12:00 a 00:00",
    "Id Ubicacion":"Deodoro Roca 1137 Parque Sarmiento"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("santacalma.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)