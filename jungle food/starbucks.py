
import json
# Desayunos Opciones
datos_lugares = [
    {
        "Nombre": "Starbucks",
        "Tipo de Cocina": "Estadounidense",
        "Ingredientes": "Desayuno, Brunch",
        "Precio minimo": "$3000",
        "Precio Maximo": "$7000",
        "Disponibilidad": " Lunes a Domingo de 07:00-21:00 ",
        "Id Ubicacion":"San lorenzo 25"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("starbucks.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)