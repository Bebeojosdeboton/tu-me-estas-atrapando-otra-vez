
import json
# teycafe Opciones
datos_lugares = [
    {
    "Nombre": "Mil Grullas y una Taza de Té",
    "Tipo de Cocina": "Delicatessen, Saludable",
    "Ingredientes": "Cafe y Te",
    "Precio minimo": "$2000",
    "Precio Maximo": "$6000",
    "Disponibilidad": "Martes a Domingo 16:00 a 21:30",
    "Id Ubicacion":"Belgrano 884",
    },
    
    {
       "Nombre": "Medialunas Calentitas Buen Pastor",
    "Tipo de Cocina": "Britanica",
    "Ingredientes": "Cena, Brunch, Desayuno, Bebidas",
    "Precio minimo": "$3000",
    "Precio Maximo": "$8000",
    "Disponibilidad": "Lunes a Domingo de 8:00 a 22:00",
    "Id Ubicacion":"Av. Hipólito Irigoyen 409",
    },

    {    "Nombre": "Havanna",
    "Tipo de Cocina": "Sudamericana, Café",
    "Ingredientes": "Café y té",
    "Precio minimo": "$3000",
    "Precio Maximo": "$6000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Id Ubicacion":"Velez Sarsfield 361, Patio Olmos",
    },

]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("teycafe.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)
