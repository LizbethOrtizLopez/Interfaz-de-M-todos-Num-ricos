
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tkabrir
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import math

global n

import math

def mostrar_resultado(a0,a1):
    
    global maxi
    global mini
    
    textito = "El modelo que mejor se ajusta es: " + str(a1) + "x +" + str(a0)
    messagebox.showinfo("Resultado",textito) 
    print(maxi)
    print(mini)
    
    plt.scatter(x,y)
    mov = (maxi - mini)/10
    mini = 0
    fun = lambda x: (a1 * x) + a0
    plt.plot(np.arange(mini,maxi,mov),[fun(i) for i in np.arange(mini,maxi,mov)],color='pink')
    plt.ylabel("Eje y")
    plt.show()
    
def regresion_lineal(x,y,n):
    try:
        sumx = sumy = st = sumxy =sumx2 = sr = 0
        for i in range (n):
            sumx = sumx + x[i]
            sumy = sumy + y[i]
            sumxy = sumxy + x[i] * y[i]
            sumx2 = sumx2 + x[i] * x[i]
        xm = sumx / n
        ym = sumy / n
        a1 = (n * sumxy - sumx * sumy)/(n * sumx2 - sumx*sumx)
        a0 = ym - a1 * xm
        
        for i in range (n):
            st = st + ((y[i] - ym)**2) 
            sr = sr + ((y[i] - (a1*x[i]) -a0)**2)
        syx = math.sqrt((sr/(n-2)))
        r = math.sqrt((st-sr)/st)
        
        return a0, a1, r, syx
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

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
        messagebox.showinfo("ERROR FATAL","El vector está incompleto o no corresponde a la entrada del tamaño. Verifica tus datos."), e 

def cargar_vector1():
    try:
        global x
        global n
        global mini
        global maxi
        
        integer_n = int(n.get())
        
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        
        file = tkinter.filedialog.askopenfilename()
        x = leerArchivo(file,integer_n)
        
        mini = x[0]
        maxi = x[0]
        for i in range (1,len(x)):
            if (x[i]<mini):
                mini = x[i]
            if (x[i]>maxi):
                maxi = x[i]
    except:
        messagebox.showinfo("ERROR FATAL","No pude abrir el archivo. Intenta de nuevo"), e  
    
def cargar_vector2():
    try:
        global y
        global n
        
        integer_n = int(n.get())
        
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        
        file = tkinter.filedialog.askopenfilename()
        y = leerArchivo(file,integer_n)
        
    except:
        messagebox.showinfo("ERROR FATAL","No pude abrir el archivo. Intenta de nuevo"), e
        
def boton():
    
    global n
    integer_n = int(n.get())
    
    if (integer_n == 0):
        messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
        raise Exception("Error. No pueden haber 0 conjuntos")
    
    funcion = regresion_lineal(x,y,integer_n)
    
    mostrar_resultado(funcion[0],funcion[1])

def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("450x350")
    
    top.config(bg="deepskyblue4")
    
    label = Label(top,text="Instrucciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",20)) #tipo de letra
    label.place(x=130,y=15)
    
    label = Label(top,text="Para el uso de este método deberás ingresar dos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="vectores con los valores de los puntos en X y Y" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="respectivamente en archivos .txt. Los puntos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="(x,y) deben estar en la misma posicion en sus")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="respectivos archivos (uno para x y otro para y).")
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
    
    label = Label(top,text="de conjuntos (x,y) que tienes en total. ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=260)
    
def re_l():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Regresion lineal")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Regresión lineal por mínimos cuadrados")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",15)) #tipo de letra
    label.place(x=15,y=15)
    
    label = Label(raiz,text="Ajuste de curvas por regresión")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=85,y=50)
   
    label = Label(raiz,text="Recomendamos se lean las intrucciones de uso")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=65,y=80)
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=instrucciones)
    instruccion.place(x=200, y=110)
    
    label = Label(raiz,text="Ingrese cantidad de puntos a evaluar:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=10,y=170)
    
    global n
    n=Entry(raiz)
    n.place(x=350,y=173)
      
    label = Label(raiz,text="Carga vector con puntos x:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=210)
    
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector1)
    calcular.place(x=350, y=210)
    
    
    label = Label(raiz,text="Carga vector con puntos y:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=240)
    
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector2)
    calcular.place(x=350, y=240)
          
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=100, y=320)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=320)
    
if __name__ == "__main__":
    
    re_l()

  
    
    





