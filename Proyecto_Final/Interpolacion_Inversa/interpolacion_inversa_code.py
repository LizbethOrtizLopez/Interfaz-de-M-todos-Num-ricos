
from tkinter import *
from Interpolacion_Inversa import bairstow
from Interpolacion_Inversa import lagrange
import tkinter.filedialog as tkabrir
import tkinter
from tkinter import messagebox
import os
import math

global n
global integer_n
global mat


def imprimir_poli(respuesta):
    funci = "(" + str(round(respuesta[0],4)) + ")"      
    for i in range (1,len(respuesta)):
        funci = funci + "+(" + str(round(respuesta[i],4)) + "*(x**" + str(i) + ")"
         
    textito = "El polinomio resultante es: " + funci
    messagebox.showinfo("Respuesta",textito)
    
def interpolacion_inversa(puntos):
    
    coef = lagrange.LAGRANGE(puntos)
    coef[len(coef)-1] -= (0.001)
    arr = []
    for i in range(len(coef)-1, -1, -1):
        arr.append(coef[i]) 
    
    imprimir_poli(arr)
    
    raices = bairstow.inicio(arr,(len(arr)-1))
    
    return raices

def cargar_matriz():
    try:
        global mat
        global integer_n
        global n
        integer_n = int(n.get())
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        file = tkinter.filedialog.askopenfilename()
        f = open(file, "r")
        # Vamos a leer la matriz
        mat = []
        for i in range(integer_n):
            mat.append([])
            row = f.readline().split()
            for j in range(2):
                mat[i].append(float(row[j]))
        f.close()
        return mat
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto o es incorrecto. Verifica tus datos."), e

def boton():
    try:
         global n
         global integer_n
         global mat
         integer_n = int(n.get())
         
         if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        
         raices = interpolacion_inversa(mat)
         textito = "Las raices de la función son: " + str(raices)
         messagebox.showinfo("Respuesta",textito)
         
    except:
        messagebox.showinfo("ERROR FATAL","Hay un error con los datos"), 

def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("450x300")
    
    top.config(bg="deepskyblue4")
    
    label = Label(top,text="Instrucciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",20)) #tipo de letra
    label.place(x=130,y=15)
    
    label = Label(top,text="Para el uso de este método deberás ingresar una")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="matriz con los valores de los puntos en X y Y" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="respectivamente en un archivo .txt. Los puntos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="(xi,yi) deben estar ordenados por fila. Ejemplo: ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="12 -34")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=135)
    
    label = Label(top,text="23 90")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=155)
    
    label = Label(top,text="40 62   ---> Donde cada fila es un")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=175)
    
    label = Label(top,text="             conjunto (x,y)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=230)

def inter_inversa():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Interpolación Inversa")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Interpolación Inversa")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",26)) #tipo de letra
    label.place(x=20,y=15)
    
    label = Label(raiz,text="Métodos para ajustar curvas")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=100,y=70)
   
    label = Label(raiz,text="Recomendamos se lean las intrucciones de uso")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=70,y=100)
    
    instruccion=Button(raiz,text="Instrucciones", width=10, command=instrucciones)
    instruccion.place(x=200, y=130)
    
    label = Label(raiz,text="Ingrese cantidad de conjuntos de puntos:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=49,y=170)
    
    global n
    n=Entry(raiz)
    n.place(x=49,y=200)
    
    label = Label(raiz,text="Selecciona el archivo con los puntos:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=49,y=240)
    
    matriz=Button(raiz,text="Abrir", width=17, command=cargar_matriz)
    matriz.place(x=49, y=280)
    
    label = Label(raiz,text="Tu polinomio y raices se calcularán con un error del 0.001%")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=10,y=320)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=150, y=360)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=360)
    
if __name__ == "__main__":
    
    inter_inversa()

  
    
    



