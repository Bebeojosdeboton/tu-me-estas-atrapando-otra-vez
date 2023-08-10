
import json
# Desayunos Opciones
datos_lugares = [
    {
        "Nombre": "Bonafide Colón y Cañada",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Cafe, Queso, Bebidas.",
        "Precio minimo": "$2000",
        "Precio Maximo": "$6000",
        "Disponibilidad": "Lunes a viernes 7 a 22 hs\nSábado y Domingo 7:30 a 22hs",
        "Id Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        "RutaImagen":"C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide.jpg"
    },
    
    {
        "Nombre": "Lapana",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Desayuno, Brunch",
        "Precio minimo": "$4000",
        "Precio Maximo": "$7000",
        "Disponibilidad": "Lunes a viernes 08:00 a 21:00, Sabados de 8:00 -00.00 , Domingos de 8:00 a 22:00",
        "Id Ubicacion":"Hipolito Yrigoyen 198, San Lorenzo 47",
        "RutaImagen":"C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana.jpg"
    },

    {   "Nombre": "Starbucks",
        "Tipo de Cocina": "Estadounidense",
        "Ingredientes": "Desayuno, Brunch",
        "Precio minimo": "$3000",
        "Precio Maximo": "$7000",
        "Disponibilidad": " Lunes a Domingo de 07:00-21:00 ",
        "Id Ubicacion":"San lorenzo 25",
        "RutaImagen":"C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks.jpg"
    },

    {   "Nombre": "Caseratto",
        "Tipo de Cocina": "Sudamericana",
        "Ingredientes": "Desayuno,Helados, Bebidas",
        "Precio minimo": "$3000",
        "Precio Maximo": "$8000",
        "Disponibilidad": "Lunes a Domingo de 8:00 a 01:00 am",
        "Id Ubicacion":"José Manuel Estrada 122",
        "RutaImagen":"C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto.jpg"
    }

]

# Convertir el diccionario a formato JSON
json_data = json.dumps(datos_lugares, indent=2)

# Guardar la cadena JSON en un archivo
with open("desayunos.json", "w") as archivo_json:
    archivo_json.write(json_data)

print(json_data)

