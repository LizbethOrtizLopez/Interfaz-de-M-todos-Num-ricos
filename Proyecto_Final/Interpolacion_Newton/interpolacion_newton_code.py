
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import os
import math
import copy

global n
global integer_n
global mat


class PolinomioClass:
    
    def __init__(self,coeficientes=[0]):
        self.coef = coeficientes
        self.grado = len(coeficientes) - 1
    
    def getGrado(self):
        return self.grado
    
    def getCoeficientes(self):
        return self.coef
    
    def getCoeficiente(self,idx):
        return self.coef[idx]
    
    def multiplicaConstante(self,constante):
        #warning: modificando campo fuera de constructor o set.
        return PolinomioClass([x * constante for x in self.coef])
        
    def aumentaCoeficiente(self,final):
        if final:
            self.coef.append(0)
        else:
            self.coef.insert(0,0)
        self.grado = self.grado + 1
    
    def sumaPolinomio(self,pol2):
        arr=[]
        for i in range (self.getGrado()+1):
            arr.append(self.coef[i]+pol2.coef[i])
        return PolinomioClass(arr);
    
    def multiplicaLineal(self,pol_lineal):
        nuevo_grado = self.getGrado() + 1
        factor = pol_lineal.getCoeficiente(0)
        op1 = self.multiplicaConstante(factor)
        op1.aumentaCoeficiente(True)
        factor = pol_lineal.getCoeficiente(1)
        op2 = self.multiplicaConstante(factor)
        op2.aumentaCoeficiente(False)
        suma = op1.sumaPolinomio(op2)
        self.coef = suma.getCoeficientes()
        self.grado = nuevo_grado
        return self

def GET_LINEAL(n):
    return PolinomioClass([1,-n])
    
def GET_POLINOMIO(arr):  
    for i in range (1,len(arr)):
        arr[0] = arr[0].multiplicaLineal(arr[i])
    return arr[0]
    
def GET_B(points):
    
    try:
        n = len(points)
        mat = [[]]
        mat = [[0 for i in range(n)] for j in range (n)]
        for i in range (n):
            mat[i][0] = points[i][1]
        for j in range (1,n):
            for i in range(n-j):
                right = mat[i][j - 1]
                left =  mat [i + 1][j - 1]
                dist = points[i + j][0] - points[i][0]
                mat[i][j] = (left - right)/dist
        return mat[0]
    
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

def POLINOMIO(points,b):
    n = len(points)
    lins = []
    obj1 = PolinomioClass(points)
    for i in range(n):
        lins.append(0)
    for i in range (n-1):
        lins[i] = GET_LINEAL(points[i][0])
    pol = []
    for i in range(n):
        pol.append(0)
    pol[0] = b[0]
    for i in range(1,n):
        x = b[i]
        listlin = []
        for j in range(i):
            listlin.append(copy.copy(lins[j]))
        p = GET_POLINOMIO(listlin)
        p = p.multiplicaConstante(x)
        m = p.getGrado()+1
        for j in range(m):
            pol[j] = pol[j] + p.getCoeficiente(i-j)
    return pol

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
        
        respuesta = (POLINOMIO(mat,GET_B(mat)))
        
        global funci
        funci = "(" + str(respuesta[0]) + ")"
        for i in range (1,len(respuesta)):
            funci = funci + "+(" + str(respuesta[i]) + "*(x**" + str(i) + ")"
         
        textito = "El polinomio resultante es: " + funci
        messagebox.showinfo("Respuesta",textito)
        
    except:
        messagebox.showinfo("ERROR FATAL","Hay un error con los datos") 
 
 
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

def inter_newton():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Interpolación de Newton")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Interpolación de Newton")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",25)) #tipo de letra
    label.place(x=10,y=15)
    
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
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=instrucciones)
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
       
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=150, y=340)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=340)
    
if __name__ == "__main__":
    
    inter_newton()

  
    
    

