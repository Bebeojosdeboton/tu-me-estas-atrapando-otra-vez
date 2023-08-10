
import json
# Desayunos Opciones
datos_lugares = [
    {
        "Nombre": "Caseratto",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Desayuno,Helados, Bebidas",
        "Precio minimo": "$3000",
        "Precio Maximo": "$8000",
        "Disponibilidad": "Lunes a Domingo de 8:00 a 01:00 am",
        "Id Ubicacion":"José Manuel Estrada 122"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("caseratto.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)