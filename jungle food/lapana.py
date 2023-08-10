
import json
# Desayunos Opciones
datos_lugares = [
    {
        "Nombre": "Lapana",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Desayuno, Brunch",
        "Precio minimo": "$4000",
        "Precio Maximo": "$7000",
        "Disponibilidad": "Lunes a viernes 08:00 a 21:00, Sabados de 8:00 -00.00 , Domingos de 8:00 a 22:00",
        "Id Ubicacion":"Hipolito Yrigoyen 198, San Lorenzo 47"
    },
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("lapana.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)