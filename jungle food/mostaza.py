
import json
# Almuerzos Opciones
datos_lugares = [
    {
     "Nombre": "Mostaza",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Restaurante de hamburguesas,Cafe",
    "Precio minimo": "$3000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Id Ubicacion":"Velez Sarsfield 361, Patio Olmos"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("mostaza.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)