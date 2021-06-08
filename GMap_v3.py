import folium
from tkinter import *
from tkinter import ttk, scrolledtext
from tkinter import messagebox
import webbrowser as wb
from geopy.geocoders import Nominatim
from geopy.distance import distance
import geopy


ventana = Tk()
ventana.geometry("600x500+400+125")
ventana.title("GMap_V3")
ventana.iconbitmap("img/map.ico")
ventana.config(background="#373434")

# Creando el control de ventanas

tab_control = ttk.Notebook(ventana)

ventana1 = ttk.Frame(tab_control)
ventana2 = ttk.Frame(tab_control)
ventana3 = ttk.Frame(tab_control)
ventana4 = ttk.Frame(tab_control)

tab_control.add(ventana1, text='LOCALIZACIÓN')
tab_control.add(ventana2, text='BUSCAR COORDENADAS')
tab_control.add(ventana3, text='DISTANCIA ENTRE DOS PUNTO')
tab_control.add(ventana4, text='ACERCA DE')
tab_control.pack(expand=1, fill='both')


###################### ventana1 ##########################################

Titulo = Label(ventana1, text="GMap Localizador", font=("Cambria", 20), bg="#373434", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(ventana1, text="Creador: N05TR4  Version: 3.0", font=("Cambria", 10), bg="#373434", fg="white", width="500",
                height="1").pack()

Titulo2 = Label(ventana1, text="", font=("Cambria", 15), bg="#373434", fg="white", width="500", height="1")
Titulo2.place(x=0, y=450)

# Variables principales
longitud = StringVar()
latitud = StringVar()
tipoMapa = StringVar()

# barra de captura de los datos
label = Label(ventana1, text="Longitud", font=("Cambria", 12), fg="black")
label.place(x=40, y=150)
longitud_entry = Entry(ventana1, textvariable=longitud, width=50)
longitud_entry.place(x=180, y=150)

label = Label(ventana1, text="Latitud", font=("Cambria", 12), fg="black")
label.place(x=40, y=200)
latitud_entry = Entry(ventana1, textvariable=latitud, width=50)
latitud_entry.place(x=180, y=200)

label = Label(ventana1, text="Tipos de Mapas Disponibles", font=("Cambria", 16), fg="black")
label.place(x=40, y=250)

# Creando los RadioButton
rad1 = Radiobutton(ventana1, text='OpenStreetMap', value='OpenStreetMap', variable=tipoMapa)
rad1.place(x=40, y=290)

rad2 = Radiobutton(ventana1, text='Stamen Toner', value='Stamen Toner', variable=tipoMapa)
rad2.place(x=40, y=310)

rad3 = Radiobutton(ventana1, text='Stamen Terrain', value='Stamen Terrain', variable=tipoMapa)
rad3.place(x=40, y=330)

# Funcion para realizar la busqueda con los parametros
def Map():
    try:
        longitud_data = longitud.get()
        latitud_data = latitud.get()
        tipoMapa_data = tipoMapa.get()
        Gmap = folium.Map(location=[longitud_data, latitud_data], tiles=tipoMapa_data, zoom_start=30,
                          control_scale=True)
        Gmap.save('index.html')
        messagebox.showinfo(title="Listo", message="Ubicacion Encontrada")
        wb.open_new(r'C:\Users\Nerkito21\Desktop\Proyectos de python\GMap_V3\index.html')

    except:
        messagebox.showerror(title="ERROR!", message="ERROR! de los parametros")



# Creacion del boton
btnGenerar = Button(ventana1, text="Buscar", font=("Cambria", 12), command=Map, width="20", fg="white",
                    height="1", bg="#24b43c")
btnGenerar.place(x=210, y=400)

############################## Ventana2 ####################################################

Titulo = Label(ventana2, text="GMap Buscador de Coordenadas", font=("Cambria", 20), bg="#373434", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(ventana2, text="Creador: N05TR4  Version: 3.0", font=("Cambria", 10), bg="#373434", fg="white", width="500",
                height="1").pack()

Titulo2 = Label(ventana2, text="", font=("Cambria", 15), bg="#373434", fg="white", width="500", height="1")
Titulo2.place(x=0, y=450)

lugar_busqueda = StringVar()

# barra de captura de los datos de la ventana2
label=Label(ventana2).pack()
label = Label(ventana2, text="INGRESA EL NOMBRE DE LA CALLE, CIUDAD, PROVINCIA, ESTADO O PAIS", font=("Cambria", 12), fg="black")
label.pack()
label=Label(ventana2).pack()
lugar_busqueda_entry = Entry(ventana2, textvariable=lugar_busqueda, width=90)
lugar_busqueda_entry.pack()

#Creando la caja de texto
txt1 = scrolledtext.ScrolledText(ventana2, width=55, height=10)
txt1.place(x=70, y=200)

def buscar_lugar():
    try:
        lugar_busqueda_data = lugar_busqueda.get()
        geo = Nominatim(user_agent="GMap")
        localizacion = geo.geocode(lugar_busqueda_data)
        localizacion_latitude =localizacion.latitude
        localizacion_longitude = localizacion.longitude

        print(localizacion)
        print(localizacion_latitude, localizacion_longitude)


        txt1.insert(INSERT, format(f"La Ubicacion de {localizacion} es {localizacion_latitude, localizacion_longitude} ") + "\n", " ")

    except:
        messagebox.showerror(title="ERROR!", message="ERROR! de los parametros")


btnGenerar = Button(ventana2, text="Calcular", font=("Cambria", 12), command=buscar_lugar, width="20", fg="white", height="1", bg="#24b43c")
btnGenerar.place(x=215, y=400)







############################## Ventana3 ####################################################


Titulo = Label(ventana3, text="GMap Distancia Entre Dos Puntos", font=("Cambria", 20), bg="#373434", fg="white", width="500", height="2")
Titulo.pack()


lugar_Origen = StringVar()
lugar_Destino = StringVar()


# barra de captura de los datos de la ventana2
label = Label(ventana3, text="Lugar de Origen:", font=("Cambria", 12), fg="black")
label.place(x=40, y=100)
lugar_Origen_entry = Entry(ventana3, textvariable=lugar_Origen, width=50)
lugar_Origen_entry.place(x=180, y=100)

label = Label(ventana3, text="Lugar de Destino:", font=("Cambria", 12), fg="black")
label.place(x=40, y=150)
latitud_entry = Entry(ventana3, textvariable=lugar_Destino, width=50)
latitud_entry.place(x=180, y=150)

#Creando la caja de texto
txt = scrolledtext.ScrolledText(ventana3, width=55, height=10)
txt.place(x=70, y=200)


def Busqueda():
    try:
        lugar_Origen_data = lugar_Origen.get()
        lugar_Destino_data = lugar_Destino.get()
        geo = Nominatim(user_agent="GMap")
        ciudad1 = geo.geocode(lugar_Origen_data)
        ciudad2 = geo.geocode(lugar_Destino_data)

        coord1 = (ciudad1.longitude, ciudad1.latitude)
        coord2 = (ciudad2.longitude, ciudad2.latitude)
        dist = geopy.distance.distance(coord1, coord2)

        #Insertando los datos a la caja de textos
        txt.insert(INSERT, format(f"{coord1}, {coord2}, La distancia entre {lugar_Origen_data} y {lugar_Destino_data} es de: ") + str(dist) + "\n")
    except:
        messagebox.showerror(title="ERROR!", message="ERROR! de los parametros")


btnGenerar = Button(ventana3, text="Calcular", font=("Cambria", 12), command=Busqueda, width="20", fg="white", height="1", bg="#24b43c")
btnGenerar.place(x=215, y=400)


##################################### Ventana4 ###################################################

Titulo = Label(ventana4, text="Acerca De", font=("Cambria", 20), bg="#373434", fg="white", width="500", height="2")
Titulo.pack()
# label = Label(ventana4).pack()

acerca = '''
    Aplicacion: GMap_v3.
    Version: 3.0
    Lenguaje de Programacion: Python 3.8.5
    Creador: N05TR4
    Fecha: 08/06/2021.
    
    Descripcion: 
    Este programa te permite obtener
    las coordenadas de una Calle,
    Avenida, Provicia o Estado de 
    cualquier Pais. Puedes calcular 
    la distancia entre dos puntos
    geograficos. Genera un archivo
    con la ubicacion que le indiques.
    '''

label1 = Label(ventana4, text=acerca, font=("Cambria", 14))
label1.pack()







if __name__ == '__main__':
    ventana.mainloop()
