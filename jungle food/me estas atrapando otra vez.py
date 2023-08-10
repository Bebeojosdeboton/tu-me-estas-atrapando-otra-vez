import json
import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
import tkintermapview
import tkinter as ttk


imagen_index = 0
opcion_seleccionada = 0
#defino listas con rutas de imagenes
imagen_por_defecto = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ciudad-cordoba.jpg"
]

imagenes_bonafide = [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide2.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/bonafide5.jpg"
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
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/ilpanino6.jpg"
    # Agrega más rutas de imágenes para las opciones aquí
]
imagenes_mostaza= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza3.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/mostaza2.jpg",
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
   
]



imagenes_alojamiento= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/alojamiento.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/alojamiento1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/alojamiento2.jpg",
 
]
imagenes_circuito= [
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/circuito1.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/circuito4.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/circuito5.jpg",
    "C:/Users/shirl/Downloads/PYTHON/Tkinter/circuito2.jpg"

 
]


#definir funciones(IMAGEN SELECCIONADA Y SU INDICE)

def cargar_imagen(index):
    try:
        global opcion_seleccionada

        if opcion_seleccionada == 0:
            ruta_imagen = imagen_por_defecto[index]
        elif opcion_seleccionada == 1:
            ruta_imagen = imagenes_bonafide[index]
        elif opcion_seleccionada == 2:
            ruta_imagen = imagenes_lapana[index]
        elif opcion_seleccionada == 3:
            ruta_imagen = imagenes_Starbucks[index]
        elif opcion_seleccionada == 4:
            ruta_imagen = imagenes_Caseratto[index]
        elif opcion_seleccionada == 5:
            ruta_imagen = imagenes_bros[index]
        elif opcion_seleccionada == 6:
            ruta_imagen = imagenes_santacalma[index]
        elif opcion_seleccionada == 7:
            ruta_imagen = imagenes_dimetro[index]
        elif opcion_seleccionada == 8:
            ruta_imagen = imagenes_ilpanino[index]
        elif opcion_seleccionada == 9:
            ruta_imagen = imagenes_mostaza[index]
        elif opcion_seleccionada == 10:
            ruta_imagen = imagenes_antares[index]
        elif opcion_seleccionada == 11:
            ruta_imagen = imagenes_canario[index]
        elif opcion_seleccionada == 12:
            ruta_imagen = imagenes_visionaire[index]
        elif opcion_seleccionada == 13:
            ruta_imagen = imagenes_circuito[index]
        elif opcion_seleccionada == 14:
            ruta_imagen = imagenes_alojamiento[index]
            
            
        else:
            return

        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((600, 500))  # Ajusta el tamaño de la imagen
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen)
        imagen_label.image = imagen

        
    except Exception as e:
        print("Error al cargar la imagen:", e)

#PASAR A LA IMAGEN SIGUIENTE

def imagen_siguiente():
    global imagen_index
    imagen_index = (imagen_index + 1) % len(imagenes_bonafide)
    cargar_imagen(imagen_index)
#PASA A LA IMAGEN ANTERIOR
def imagen_anterior():
    global imagen_index
    imagen_index = (imagen_index - 1) % len(imagenes_bonafide)
    cargar_imagen(imagen_index)
#CAMBIA LA CATEGORIA DE IMAGENES Y MUESTRA EL MAPA CON EL MARCADOR DE COORDENADAS
def cambiar_categoria(opcion,mapa=None,lat=None,long=None,nombre=None):
    global opcion_seleccionada, imagen_index

    opcion_seleccionada = opcion
    imagen_index = 0
    cargar_imagen(imagen_index)
   
    setear_punto_coordenada(mapa,lat,long,nombre)
#MENSAJE DE QUE YO HICE LA AP
def mostrar_quienes_somos():
    texto_quienes_somos = "Aplicacion creada por Alejandra Reales, Angel maldito"
    tk.messagebox.showinfo("Quienes somos", texto_quienes_somos)

#SETEA LA COORDENADA

def setear_punto_coordenada(mapa=None,lat=None,long=None,nombre=None):
    try:
        mapa.delete_all_marker()
        mapa.set_marker(lat,long,text=nombre)
    except:
            pass 


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
boton1 = tk.Button(frame_izquierdo, text="CIRCUITOS", command=lambda: cambiar_categoria(13), bg="gainsboro", width=15, height=0, font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")
boton2 = tk.Button(frame_izquierdo, text="ALOJAMIENTO", command=lambda: cambiar_categoria(14), bg="gainsboro", width=15, height=0,font=("Comic Sans MS", 12), borderwidth=2, relief="ridge")



map_widget = tkintermapview.TkinterMapView(frame_izquierdo, width=400, height=400, corner_radius=0)
map_widget.set_position(-31.41292, -64.18193)
map_widget.set_zoom(13) 
 



boton1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
boton2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)


map_widget.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
# Crear un sub-frame para el mapa en el frame izquierdo (parte inferior)
sub_frame_izquierdo = tk.Frame(frame_izquierdo)
sub_frame_izquierdo.pack(side=tk.BOTTOM, padx=10, pady=5, fill="both", expand=True)

# Agregar espacio para el mapa en el sub-frame izquierdo
espacio_mapa = tk.Label(sub_frame_izquierdo)
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
Desayunos.add_command(label="Bonafide Colon", command=lambda: cambiar_categoria(1,map_widget,-31.41292, -64.18193,"Bonafide"))
Desayunos.add_command(label="La Pana", command=lambda: cambiar_categoria(2,map_widget,-31.422708579040552, -64.18776086231496,"La Pana"))
Desayunos.add_command(label="Starbucks", command=lambda: cambiar_categoria(3,map_widget,-31.42297221179353, -64.18690611813612,"Starbucks"))
Desayunos.add_command(label="Caseratto", command=lambda: cambiar_categoria(4,map_widget,-31.427770237509552, -64.18730330649359,"Caseratto"))
menu_bar.add_cascade(label="Desayunos", menu=Desayunos)

Almuerzos = Menu(menu_bar, tearoff=0)
Almuerzos.add_command(label="Bros Comedor", command=lambda: cambiar_categoria(5,map_widget,-31.41292, -64.18193,"Bros Comedor"))
Almuerzos.add_command(label="Santa Calma", command=lambda: cambiar_categoria(6,map_widget,-31.41292, -64.18193,"Santa Calma"))
Almuerzos.add_command(label="Dimetro", command=lambda: cambiar_categoria(7,map_widget,-31.41292, -64.18193,"Dimetro"))
Almuerzos.add_command(label="Il Panino", command=lambda: cambiar_categoria(8,map_widget,-31.41292, -64.18193,"Il Panino"))
Almuerzos.add_command(label="Mostaza", command=lambda: cambiar_categoria(9,map_widget,-31.41292, -64.18193,"Mostaza"))
menu_bar.add_cascade(label="Almuerzos", menu=Almuerzos)

bares_y_Pubs = Menu(menu_bar, tearoff=0)
bares_y_Pubs.add_command(label="Antares", command=lambda: cambiar_categoria(10,map_widget,-31.41292, -64.18193,"Antares"))
bares_y_Pubs.add_command(label="Canario Negro", command=lambda: cambiar_categoria(11,map_widget,-31.41292, -64.18193,"Canario Negro"))
bares_y_Pubs.add_command(label="Visionaire", command=lambda: cambiar_categoria(12,map_widget,-31.41292, -64.18193,"Visionaire"))
menu_bar.add_cascade(label="Bares y Pubs", menu=bares_y_Pubs)


Quienes_somos = tk.Menu(menu_bar, tearoff=0)
Quienes_somos.add_command(label="Aplicación creada por Alejandra Reales, Angel maldito", command=mostrar_quienes_somos)
menu_bar.add_cascade(label="Quienes somos", menu=Quienes_somos)

# Cargar la primera imagen al iniciar la ventana
cargar_imagen(imagen_index)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()