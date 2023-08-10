
import json
# Almuerzos Opciones
datos_lugares = [
    {
        "Nombre": "Bros. Comedor",
        "Tipo de Cocina": "Internacional, Contemporánea, Argentina, Saludable",
        "Ingredientes": "Almuerzos y Cenas",
        "Precio minimo": "$3000",
        "Precio Maximo": "$10000",
        "Disponibilidad": "Martes a Domingo de 12:00 a 15:00 y 20:00 a 23:30 ",
        "Id Ubicacion":"Calle 27 de Abril 568"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("bros.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)