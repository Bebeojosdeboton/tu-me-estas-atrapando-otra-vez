import json
# Postres Opciones
datos_lugares = [
    {
        "Nombre": " Creambury",
        "Tipo de Cocina": "Café, Argentina, Sudamericana",
        "Ingredientes": "Desayuno, Almuerzo",
        "Precio minimo": "$2000",
        "Precio Maximo": "$7000",
        "Disponibilidad": "Lunes a Domingo 8 a 23:30 hs",
        "Id Ubicacion": "Rondeau 390" 
    },
    
    {
        "Nombre": "Maria Antonieta Universodeli",
        "Tipo de Cocina": "Café, Delicatessen",
        "Ingredientes": "Desayuno, Brunch, Almuerzo",
        "Precio minimo": "$4000",
        "Precio Maximo": "$7000",
        "Disponibilidad": "Lunes a Sabado 08:30 a 21:00,  Domingos de 16:00 a 21:00",
        "Id Ubicacion":"Avenida Luis J de Tejeda 4575 Cerro de Las Rosas",
    },

    {       "Nombre": "Wollen ",
        "Tipo de Cocina": "Café, Argentina",
        "Ingredientes": "Helados,Postres",
        "Precio minimo": "$1000",
        "Precio Maximo": "$6000",
        "Disponibilidad": " Lunes a Domingo de 17:00-22:00 ",
        "Id Ubicacion":"27 de Abril 72",
    }
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("postres.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)