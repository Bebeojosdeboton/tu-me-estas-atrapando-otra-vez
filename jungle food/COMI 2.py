import json
import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk


imagen_index = 0
opcion_seleccionada = 0

imagen_por_defecto = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ciudad-cordoba.jpg"
]

imagenes_bonafide = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafidet.jpg"
    # Agrega más rutas de imágenes si es necesario
]

imagenes_lapana = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/lapana5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]

imagenes_Starbucks = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/starbucks5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_Caseratto = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/caseratto6.jpg"

    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_bros= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bros6.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]

imagenes_santacalma= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/santacalma5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_dimetro= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/dimetro6.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_ilpanino= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino6.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_mostaza= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_antares= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/antares5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_canario= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/canario.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/canario1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/canario2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/canario3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/canario4.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_visionaire= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/visionaire.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/visionaire2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/visionaire3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/visionaire4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/visionaire5.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]

# Nombres de los archivos JSON
datos = {
     "Nombre": "Ciudad de Cordoba",
     "Caracteristica": "es conocida por su arquitectura colonial española. Alberga la Manzana Jesuítica, un complejo del siglo XVII con claustros activos, iglesias y el campus original de la Universidad Nacional de Córdoba, una de las universidades más antiguas de Sudamérica. El punto central de la ciudad es la Plaza San Martín y la Catedral de Córdoba de estilo neobarroco."
}
{
    "Nombre": "Bonafide Colón y Cañada",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Cafe, Queso, Bebidas.",
    "Precio minimo": "$2000",
    "Precio Maximo": "$6000",
    "Disponibilidad": "Lunes a viernes 7 a 22 hs\nSábado y Domingo 7:30 a 22hs",
    "Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
    
},
{
    "Nombre": "Lapana",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Desayuno, Brunch",
    "Precio minimo": "$4000",
    "Precio Maximo": "$7000",
    "Disponibilidad": "Lunes a viernes 08:00 a 21:00, Sabados de 8:00 -00.00 , Domingos de 8:00 a 22:00",
    "Ubicacion": "Hipolito Yrigoyen 198, San Lorenzo 47",
    
},
{
    "Nombre": "Starbucks",
    "Tipo de Cocina": "Estadounidense",
    "Ingredientes": "Desayuno, Brunch",
    "Precio minimo": "$3000",
    "Precio Maximo": "$7000",
    "Disponibilidad": " Lunes a Domingo de 07:00-21:00 ",
    "Ubicacion": "San lorenzo 25",
    
},
{
    "Nombre": "Caseratto",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Desayuno,Helados, Bebidas",
    "Precio minimo": "$3000",
    "Precio Maximo": "$8000",
    "Disponibilidad": "Lunes a Domingo de 8:00 a 01:00 am",
    "Ubicacion": "José Manuel Estrada 122",
    
}
{
    "Nombre": "Bros. Comedor",
    "Tipo de Cocina": "Internacional, Contemporánea, Argentina, Saludable",
    "Ingredientes": "Almuerzos y Cenas",
    "Precio minimo": "$3000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Martes a Domingo de 12:00 a 15:00 y 20:00 a 23:30 ",
    "Ubicacion": "Calle 27 de Abril 568"
},
{
    "Nombre": "Santa Calma",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Desayuno, Almuerzo, Cena, Brunch, Bebidas",
    "Precio minimo": "$5000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "lunes a Domingo de 12:00 a 00:00",
    "Ubicacion": "Deodoro Roca 1137 Parque Sarmiento"
},
{
    "Nombre": "DIMETRO",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Pizzas milanesas y lomos por metro.Servicio de cafeteria",
    "Precio minimo": "$6000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Ubicacion": "José Manuel Estrada 16"
},
{
    "Nombre": "IL PANINO",
    "Tipo de Cocina": "Argentina, Mexicana, Pizzería, Internacional",
    "Ingredientes": "Desayuno, Almuerzo, Cena, Brunch",
    "Precio minimo": "$4000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Ubicacion": "Velez Sarsfield 361, Patio Olmos"
},
{
    "Nombre": "Mostaza",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Restaurante de hamburguesas,Cafe",
    "Precio minimo": "$3000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 10:00 a 22:00",
    "Ubicacion": "Velez Sarsfield 361, Patio Olmos"
}
{
    "Nombre": "Antares",
    "Tipo de Cocina": "Bar, Comida rápida, Pub, Argentina",
    "Ingredientes": "Almuerzo, Cena, Brunch, Bebidas",
    "Precio minimo": "$2000",
    "Precio Maximo": "$9000",
    "Disponibilidad": "Lunes a Domingo de 16:00 a 04:00 am",
    "Ubicacion": "Calle San Lorenzo 79"
},
{
    "Nombre": "Bonanza Bar",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Cena,Bebidas",
    "Precio minimo": "$4000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "",
    "Ubicacion": "Rondeau 150"
}
{
    "Nombre": "VISIONAIRE",
    "Tipo de Cocina": "Sudamericana",
    "Ingredientes": "Almuerzo,Cena,Bebidas",
    "Precio minimo": "$5000",
    "Precio Maximo": "$10000",
    "Disponibilidad": "Lunes a Domingo de 08:00 a 03:00",
    "Ubicacion": "Chacabuco 436"
}


def cargar_imagen(index):
    try:
        global opcion_seleccionada

        if opcion_seleccionada == 0:
            texto_ciudad_cordoba = "Nombre: Ciudad de Cordoba, Caracteristica: es conocida por su arquitectura colonial española. Alberga la Manzana Jesuítica, un complejo del siglo XVII con claustros activos, iglesias y el campus original de la Universidad Nacional de Córdoba, una de las universidades más antiguas de Sudamérica. El punto central de la ciudad es la Plaza San Martín y la Catedral de Córdoba de estilo neobarroco."
        ruta_imagen = imagen_por_defecto[index] + texto_ciudad_cordoba
        elif opcion_seleccionada == 1:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide
        elif opcion_seleccionada == 2:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide        elif opcion_seleccionada == 3:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide         
        elif opcion_seleccionada == 4:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide
            elif opcion_seleccionada == 5:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
            ruta_imagen = imagenes_bros[index] + f"_Nombre-{datos['_Nombre']}_Tipo de Cocina-{datos['Tipo de Cocina']}_Precio minimo-{datos['Precio minimo']}_Precio Maximo-{datos['Precio Maximo']}Disponibilidad-{datos['Disponibilidad']}Ubicacion-{datos['Ubicacion']}.jpg"
        elif opcion_seleccionada == 6:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
            ruta_imagen = imagenes_santacalma[index] + f"_Nombre-{datos['_Nombre']}_Tipo de Cocina-{datos['Tipo de Cocina']}_Precio minimo-{datos['Precio minimo']}_Precio Maximo-{datos['Precio Maximo']}Disponibilidad-{datos['Disponibilidad']}Ubicacion-{datos['Ubicacion']}.jpg"
        elif opcion_seleccionada == 7:
          texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
            ruta_imagen = imagenes_dimetro[index] + f"_Nombre-{datos['_Nombre']}_Tipo de Cocina-{datos['Tipo de Cocina']}_Precio minimo-{datos['Precio minimo']}_Precio Maximo-{datos['Precio Maximo']}Disponibilidad-{datos['Disponibilidad']}Ubicacion-{datos['Ubicacion']}.jpg"
        elif opcion_seleccionada == 8:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
            ruta_imagen = imagenes_ilpanino[index] + f"_Nombre-{datos['_Nombre']}_Tipo de Cocina-{datos['Tipo de Cocina']}_Precio minimo-{datos['Precio minimo']}_Precio Maximo-{datos['Precio Maximo']}Disponibilidad-{datos['Disponibilidad']}Ubicacion-{datos['Ubicacion']}.jpg"
        elif opcion_seleccionada == 9:
           texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",

        elif opcion_seleccionada == 10:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide
        elif opcion_seleccionada == 11:
            texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide
        elif opcion_seleccionada == 12:texto_bonafide="Nombre": "Bonafide Colón y Cañada,Tipo de Cocina": "Sudamericana,Ingredientes": "Cafe, Queso, Bebidas,Precio minimo: $2000,Precio Maximo:$6000,Disponibilidad: Lunes a viernes 7 a 22 hs Sábado y Domingo 7:30 a 22hs,Ubicacion": "Av. Figueroa Alcorta 192\nCórdoba",
        ruta_imagen = imagenes_bonafide[index] +texto_bonafide
        else:
            return

imagen = Image.open(ruta_imagen)
imagen = imagen.resize((550, 400))  # Ajusta el tamaño de la imagen según tus necesidades
imagen = ImageTk.PhotoImage(imagen)
imagen_label.config(image=imagen)
imagen_label.image = imagen

       
    except Exception as e:
        print("Error al cargar la imagen:", e)

def imagen_siguiente():
    global imagen_index
    imagen_index = (imagen_index + 1) % len(imagenes_bonafide)
    cargar_imagen(imagen_index)

def imagen_anterior():
    global imagen_index
    imagen_index = (imagen_index - 1) % len(imagenes_bonafide)
    cargar_imagen(imagen_index)

def cambiar_categoria(opcion):
    global opcion_seleccionada, imagen_index

    opcion_seleccionada = opcion
    imagen_index = 0
    cargar_imagen(imagen_index)

def mostrar_quienes_somos():
    texto_quienes_somos = "Aplicacion creada por Alejandra Reales, Angel maldito"
    tk.messagebox.showinfo("Quienes somos", texto_quienes_somos)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenidos a Jungle Food")
ventana.geometry("1000x600")

# Crear los frames para dividir la ventana
frame_izquierdo = tk.Frame(ventana)
frame_derecho = tk.Frame(ventana)
frame_izquierdo.pack(side="left", padx=10, pady=10, fill="both", expand=True)
frame_derecho.pack(side="right", padx=10, pady=10, fill="both", expand=True)

# Agregar botones en el frame izquierdo (parte superior)
# Agregar botones en el frame izquierdo (parte superior) con tamaños personalizados
boton1 = tk.Button(frame_izquierdo, text="CIRCUITOS", command=lambda: cambiar_categoria(0), bg="gainsboro", width=15, height=0, font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton2 = tk.Button(frame_izquierdo, text="ALOJAMIENTO", command=lambda: cambiar_categoria(1), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton3 = tk.Button(frame_izquierdo, text="EXPERIENCIAS", command=lambda: cambiar_categoria(2), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton4 = tk.Button(frame_izquierdo, text="ATRACTIVOS", command=lambda: cambiar_categoria(3), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton5 = tk.Button(frame_izquierdo, text="OFICINA TURISTICA", command=lambda: cambiar_categoria(4), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton6 = tk.Button(frame_izquierdo, text="DATOS UTILES", command=lambda: cambiar_categoria(5), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton7 = tk.Button(frame_izquierdo, text="INICIO", command=lambda: cambiar_categoria(0), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton4.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton5.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton6.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton7.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Crear un sub-frame para el mapa en el frame izquierdo (parte inferior)
sub_frame_izquierdo = tk.Frame(frame_izquierdo)
sub_frame_izquierdo.pack(side=tk.BOTTOM, padx=10, pady=5, fill="both", expand=True)

# Agregar espacio para el mapa en el sub-frame izquierdo
espacio_mapa = tk.Label(sub_frame_izquierdo, text="Espacio para el mapa")
espacio_mapa.pack(fill="both", expand=True)

imagen_label = tk.Label(frame_derecho)
imagen_label.pack(padx=20, fill="both", expand=True)


# Crear un subframe para la imagen (parte superior)
frame_imagen = tk.Frame(frame_derecho)
frame_imagen.pack(fill="both", expand=True)

# Crear un subframe para el texto (parte inferior)
frame_texto = tk.Frame(frame_derecho)
frame_texto.pack(fill="both", expand=True)

# Agregar la imagen en el subframe de la imagen
imagen_label = tk.Label(frame_imagen)
imagen_label.pack(padx=20, pady=20, fill="both", expand=True)

# Agregar el texto en el subframe del texto
texto_label = tk.Label(frame_texto, text="Texto relacionado a la imagen")
texto_label.pack(padx=10, pady=5)


# Crear un Frame para la etiqueta de imagen
frame_imagen = tk.Frame(frame_derecho)
frame_imagen.pack(side=tk.TOP, fill="both", expand=True)

# Crear un Frame para los botones de flecha
frame_botones = tk.Frame(frame_derecho)
frame_botones.pack(side=tk.BOTTOM, pady=10)

# Agregar la etiqueta de imagen al frame_imagen
imagen_label = tk.Label(frame_imagen)
imagen_label.pack(padx=20, fill="both", expand=True)

# Agregar botones de flecha al frame_botones
btn_anterior = tk.Button(frame_botones, text="<", command=imagen_anterior, bg="lightgray")
btn_anterior.pack(side=tk.LEFT, padx=10, pady=5)

btn_siguiente = tk.Button(frame_botones, text=">", command=imagen_siguiente, bg="lightgray")
btn_siguiente.pack(side=tk.LEFT, padx=10, pady=5)

# Crear los menús en la parte superior
menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)

Desayunos = Menu(menu_bar, tearoff=0)
Desayunos.add_command(label="Bonafide Colon", command=lambda: cambiar_categoria(1))
Desayunos.add_command(label="La Pana", command=lambda: cambiar_categoria(2))
Desayunos.add_command(label="Starbucks", command=lambda: cambiar_categoria(3))
Desayunos.add_command(label="Caseratto", command=lambda: cambiar_categoria(4))
menu_bar.add_cascade(label="Desayunos", menu=Desayunos)

Almuerzos = Menu(menu_bar, tearoff=0)
Almuerzos.add_command(label="Bros Comedor", command=lambda: cambiar_categoria(5))
Almuerzos.add_command(label="Santa Calma", command=lambda: cambiar_categoria(6))
Almuerzos.add_command(label="Dimetro", command=lambda: cambiar_categoria(7))
Almuerzos.add_command(label="Il Panino", command=lambda: cambiar_categoria(8))
Almuerzos.add_command(label="Mostaza", command=lambda: cambiar_categoria(9))
menu_bar.add_cascade(label="Almuerzos", menu=Almuerzos)

bares_y_Pubs = Menu(menu_bar, tearoff=0)
bares_y_Pubs.add_command(label="Antares", command=lambda: cambiar_categoria(10))
bares_y_Pubs.add_command(label="Canario Negro", command=lambda: cambiar_categoria(11))
bares_y_Pubs.add_command(label="Visionaire", command=lambda: cambiar_categoria(12))
menu_bar.add_cascade(label="Bares y Pubs", menu=bares_y_Pubs)


Quienes_somos = tk.Menu(menu_bar, tearoff=0)
Quienes_somos.add_command(label="Aplicación creada por Alejandra Reales, Angel maldito", command=mostrar_quienes_somos)
menu_bar.add_cascade(label="Quienes somos", menu=Quienes_somos)

# Cargar la primera imagen al iniciar la ventana
cargar_imagen(imagen_index)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()