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
        "Id Ubicacion":"Calle 27 de Abril 568",
    },
    
    {
        "Nombre": "Santa Calma",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Desayuno, Almuerzo, Cena, Brunch, Bebidas",
    "Precio minimo": "$5000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "lunes a Domingo de 12:00 a 00:00",
    "Id Ubicacion":"Deodoro Roca 1137 Parque Sarmiento",
    },

    {  "Nombre": "DIMETRO",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Pizzas milanesas y lomos por metro.Servicio de cafeteria",
    "Precio minimo": "$6000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Id Ubicacion":"Velez Sarsfield 361, Patio Olmos",
    },

    {    "Nombre": "IL PANINO",
    "Tipo de Cocina": "Argentina, Mexicana, Pizzería, Internacional",
    "Ingredientes": "Desayuno, Almuerzo, Cena, Brunch",
    "Precio minimo": "$4000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Id Ubicacion":"Velez Sarsfield 361, Patio Olmos",
    },

    { "Nombre": "Mostaza",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Restaurante de hamburguesas,Cafe",
    "Precio minimo": "$3000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Id Ubicacion":"Velez Sarsfield 361, Patio Olmos",
    }
]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("almuerzos.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)
