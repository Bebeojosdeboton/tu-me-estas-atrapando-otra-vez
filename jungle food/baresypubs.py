import json
# bares y pubs Opciones
datos_lugares = [
    { "Nombre": "Antares",
    "Tipo de Cocina": "Bar, Comida rápida, Pub, Argentina",
    "Ingredientes": "Almuerzo, Cena, Brunch, Bebidas",
    "Precio minimo": "$2000",
    "Precio Maximo": "$9000",
    "Disponibilidad": "Lunes a Domingo de 16:00 a 04:00 am",
    "Id Ubicacion":"Calle San Lorenzo 79",
    
    },
    
    { "Nombre": "Canario Negro",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Cena,Bebidas",
    "Precio minimo": "$6000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 16:00 a 04:00 am",
    "Id Ubicacion":"Rondeau 155",
   
    },

    { "Nombre": "VISIONAIRE",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Almuerzo,Cena,Bebidas",
    "Precio minimo": "$5000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 08:00 a 03:00",
    "Id Ubicacion":"Chacabuco 436",
    },

]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("baresypubs.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)