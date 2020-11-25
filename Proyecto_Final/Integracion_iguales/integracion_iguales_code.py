
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import os
import math

global n

def sim38(h, f0, f1, f2, f3):
    return (3/8) * h * (f0 + (3 * f1) + (3 * f2) + f3)


def sim13mul(h, n, f):
    sum = f[0]
    for i in range(1, n-1, 2):
        sum = sum + (4 * f[i]) + (2 * f[i+1])
    sum = sum + (4 * f[n-1]) + f[n]
    return (h/3)*sum


def intsim(a, b, f):
    n = len(f)-1
    h = (b-a)/n
    sum = 0
    m = n
    odd = math.fmod(n, 2)
    if odd > 0 and n > 1:
        sum = sum + sim38(h, f[n-3], f[n-2], f[n-1], f[n])
        print("simspon 3/8: ", sum)
        m = n-3
    if m > 1:
        sum = sum + sim13mul(h, m, f)
        print("simspon 1/3: ", sum)
    return sum

def leerArchivo(file,n):
    try:
        f = open(file, "r")
        v = []
        row = f.readline().split()
        for i in range(n):
            v.append(float(row[i]))
        # Cerramos el archivo.
        f.close()
        return v
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El vector está incompleto, no corresponde a la entrada del tamaño o es un archivo incorrecto. Verifica tus datos."), e 

def cargar_vector():
    
    try:
        global puntos
        global n
        
        integer_n = int(n.get())
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        file = tkinter.filedialog.askopenfilename()
        
        puntos = leerArchivo(file,integer_n)
        
        '''
        diferencia = math.fabs(puntos[1]) - math.fabs(puntos[0])
        
        for i in range(1, len(puntos)-1):
            if ((puntos[i+1] - puntos[i]) != diferencia):
                messagebox.showinfo("ERROR FATAL","Los segmentos no son iguales")
                raise Exception("Error.Los segmentos no son iguales") 
        '''
    except:
        messagebox.showinfo("ERROR FATAL","No pude abrir el archivo. Intenta de nuevo"), e 
    
def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("480x400")
    
    top.config(bg="deepskyblue4")
    
    label = Label(top,text="Instrucciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",20)) #tipo de letra
    label.place(x=130,y=15)
    
    label = Label(top,text="Para el uso de este método deberás ingresar un")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="vector con los valores de la evaluación f(x)" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="en un archivo .txt. En el programa, deberás")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="ingresar el intervalo entre el que se")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="encuentran las evaluaciones de f(x).")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=135)
    
    label = Label(top,text="Los datos deben estar separados solo por un")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=155)
    
    label = Label(top,text="espacio, de lo contrario podría mostrar errores.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=175)
    
    label = Label(top,text="En el programa deberás ingresar la cantidad")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    label = Label(top,text="de valores f(x) que tienes en total. ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    label = Label(top,text="El uso de este método solo es para segmentos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=245)
    
    label = Label(top,text="separados por la misma distancia. Verifica")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=265)
    
    label = Label(top,text="tus datos, de lo contrario, utiliza la sección de")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=285)
    
    label = Label(top,text="Integración para segmentos desiguales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=305)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=345)

def boton():
    try:
         global n
         global x1
         global x2
         
         integer_n = n.get()
         x_i = float(x1.get())
         x_s = float(x2.get())
         
         if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
         
         respuesta = intsim(x_i,x_s,puntos)
         
         textito = "El resultado es: " + str(respuesta)
         messagebox.showinfo("Respuesta",textito)
         
    except:
        messagebox.showinfo("ERROR FATAL","Hay un error con los datos o dejaste campos vacíos") 
    
def integra_igual():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Integración segmentos desiguales")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Integración de segmentos iguales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",17)) #tipo de letra
    label.place(x=17,y=15)
    
    label = Label(raiz,text=" Método de integración numérica")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=75,y=50)
   
    label = Label(raiz,text="Recomendamos se lean las intrucciones de uso")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=65,y=80)
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=instrucciones)
    instruccion.place(x=200, y=110)
    
    label = Label(raiz,text="Ingrese número de puntos:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=78,y=170)
    
    global n
    n=Entry(raiz)
    n.place(x=350,y=173)
      
    label = Label(raiz,text="Carga vector:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=213,y=210)
    
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector)
    calcular.place(x=350, y=210)
    
    label = Label(raiz,text="Ingresa valor menor de x:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=78,y=245)
    
    global x1
    x1=Entry(raiz)
    x1.place(x=350,y=247)
    
    label = Label(raiz,text="Ingresa valor mayor de x:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=78,y=280)
    
    global x2
    x2=Entry(raiz)
    x2.place(x=350,y=282)
           
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=100, y=330)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=330)
    
if __name__ == "__main__":
    
    integra_igual()

  
    
    



