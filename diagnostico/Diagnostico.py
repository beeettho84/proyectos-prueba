import tkinter as tk
from tkinter import ttk
from datetime import datetime

#Elaborado por Carlos Alberto Barba Cardenas 220288515 CUCEI para SSPUAESO 2023A

op=0 #variable opcion, su funcion es hacer que el cronometro inicie o se detenga

root = tk.Tk()

INTERVALO_REFRESCO = 500  # Tiempo en milisegundos para la frecuencia de actualizacion del cronometro

hora_inicio = datetime.now() #Momento de inicio del cronometro, se modifica cada que se presiona el boton de imprimir

def segundos_a_segundos_minutos_y_horas(segundos): #funcion para formatear el tiempo, originalmente esta en segundos
    horas = int(segundos / 3600) # convierte segundos a horas y almacena el resultado
    segundos -= horas*3600 # resta las horas completadas al conteo de segundos
    minutos = int(segundos/60) # convierte segundos a minutos y almacena el resultado
    segundos -= minutos*60 #resta los minutos completados al conteo de segundos
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}" #la funcion devuelve una cadena con el tiempo formateado hh:mm:ss

def obtener_tiempo_transcurrido_formateado(): #esta funcion obtiene la cantidad de segundos transcurridos para convertirlos
    segundos_transcurridos= (datetime.now() - hora_inicio).total_seconds() # se usa la funcion anterior contando el tiempo desde la activacion del cronometro hasta el momento actual
    return segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos)) #devuelve el tiempo resultante

def refrescar_tiempo_transcurrido(): #funcion para la actualizacion del reloj
    global op #se llama a la variable global op
    if op==1: #condicion con la variable global op
        print("Refrescando!") # impresion de control, permite verificar que el programa hace uso de la funcion
        variable_hora_actual.set(obtener_tiempo_transcurrido_formateado()) #almacena el valor de los segundos transcurridos
    root.after(INTERVALO_REFRESCO, refrescar_tiempo_transcurrido) #esta funcion se cicla para funcionar de nuevo cada tiempo determinado, en este caso el valor de la variable intervalo

def piramide(n,c): #funcion para dibujar la piramide
    borrar() #primero borramos el area de texto por si ya hay texto en ella
    global op, hora_inicio #llamamos a las variables op y hora_inicio para modificar su valor en el contexto global
    hora_inicio = datetime.now() #cambiamos el valor del inicio del cronometro
    op=1 #cambiamos el valor de la variable para iniciar el cronometro
    print(hora_inicio) #imprimimos el tiempo de activacion para visualizar cuando se inicio el cronometro
    print(n, " ", c) #imprimimos los valores entrantes para ver el numero de pisos y el caracter que se va a imprimir
    copia = n # copiamos el valor de n para operaciones futuras sin necesidad de modificar la variable original
    for i in range(n): #iniciamos un bucle en relacion al numero recibido
        for x in range((2*copia)-1): #este bucle imprimira 2n-1 espacios para la forma de la piramide
            caja.insert(tk.END," ")
        copia-=1 #restamos uno al valor de copia para usarla en el siguiente bucle del for principal
        for m in range((2*i)+1): #este bucle imprime nuestro caracter recibido mas un espacio, eso le da la forma a la priamide siempre y cuando recibamos un solo simbolo
            caja.insert(tk.END,c+" ") #imprimimos el caracter y un espacio
        caja.insert(tk.END, "\n") #imprimimos un salto de linea para dibujar el siguiente piso

def borrar(): #esta funcion limpia el area de texto
    global op #llamamos a la variable global op para modificar su valor
    op=0 #cambiamos el valor de op para detener el cronometro y que ya no se actualice
    print ("borrando") #imprimimos esto en la consola para saber que esta funcion se ejecuta
    caja.delete(1.0, tk.END) #borramos el contenido del area de texto desde el inicio hasta el final

root.title('Diagnostico') #titulamos la ventana
root.geometry("1000x600") #ingresamos las dimensiones que tendra la ventana
variable_hora_actual = tk.StringVar(root, value=obtener_tiempo_transcurrido_formateado()) #le damos valor al cronometro, con esto llenaremos el valor del label cuando activemos la funcion
caracter = tk.Entry(root, width=20) #declaramos y colocamos las cajas de texto y sus botones desde aqui
caracter.place(anchor=tk.N, x=100)
numero = tk.Entry(root, width=20)
numero.place(anchor=tk.N, x=900)
caja = tk.Text(root, height=30, width=110)
caja.place(anchor=tk.CENTER, y=270, x=500)
caja.tag_config(root, justify=tk.CENTER)
imprimir = tk.Button(root, text="Impirmir", command= lambda: piramide(int(numero.get()),caracter.get()))
imprimir.place(anchor=tk.S, x=100, y=550)
limpiar = tk.Button(root, text="Limpiar", command= lambda: borrar())
limpiar.place(anchor=tk.S, x=900, y=550)
root.tiempo = tk.Label(root, textvariable=variable_hora_actual, font=f"Consolas 20")
root.tiempo.place(anchor=tk.S, x=500, y=550) #hasta aqui
app = tk.Frame() #declaramos un frame para el funcionamiento del cronometro
refrescar_tiempo_transcurrido() #esta linea activara el cronometro siempre y cuando op sea igual a 1
app.pack() #esta linea nos permitira actualizar la interfaz para visualizar los cambios del cronometro

root.mainloop() #iniciamos el bucle principal de la aplicacion