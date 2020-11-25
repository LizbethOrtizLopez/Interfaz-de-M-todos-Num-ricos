
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import math

global n
global integer_n
global mat

def mostrar_resultado(funci,mat):
    
    global maxi
    global mini
    
    x =[]
    y =[]
    
    for i in range (integer_n):
        x.append(mat[i][0])
        y.append(mat[i][1])

    plt.scatter(x,y)
    mov = (maxi - mini)/10
    mini = mini - mov
    plt.plot(np.arange(mini,maxi,mov),[eval_func(i) for i in np.arange(mini,maxi,mov)],color='red')
    plt.ylabel("Eje y")
    plt.show()

def eval_func(x):
    global funci
    return eval(funci)

def gauss(a,b,n,tol):
    s = []
    for i in range(0,n):
        s.append(0)
    for i in range(0,n):
        s[i] = math.fabs(a[i][0])
        for j in range(1,n):
            test = math.fabs(a[i][j])
            if test>s[i]:
                s[i] = test
    aa,bb,error = eliminate(a,b,s,n,tol)
    if(error == False):
        x = substitute(aa,bb,n)
    return x

def eliminate(a, b, s, n, tol):
    try:
        for k in range(n - 1):
            (a, b, s) = pivot(a, b, s, n, k)
            if math.fabs(a[k][k] / s[k]) < tol:
                messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo.")
                raise Exception("Error. No puedo encontrar una solución porque uno de los datos es erróneo.")
                return a,b,True #error
            for i in range(k + 1, n):
                factor = a[i][k] / a[k][k]
                for j in range(k + 1, n):
                    a[i][j] -= (factor * a[k][j])
                b[i] -= factor * b[k]

        if math.fabs(a[n - 1][n - 1] / s[n - 1]) < tol:
            messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo.")
            raise Exception("Error. No puedo encontrar una solución porque uno de los datos es erróneo.")
            return a,b,True #error
        
        return a, b, False
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

def pivot(a, b, s, n, k):
    try:
        p = k
        big = math.fabs((a[k][k] / s[k]))
        for i in range(k + 1, n):
            dummy = math.fabs(a[i][k] / s[i])
            if dummy > big:
                big = dummy
                p = i
        if p != k:
            for j in range(k, n):
                dummy = a[p][j]
                a[p][j] = a[k][j]
                a[k][j] = dummy
            dummy = b[p]
            b[p] = b[k]
            b[k] = dummy
            dummy = s[p]
            s[p] = s[k]
            s[k] = dummy
        return a, b, s
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

def substitute(a,b,n):
    try:
        x=[]
        for i in range(0,n):
            x.append(0)
        x[n-1] = b[n-1]/a[n-1][n-1]
        for i in range(n-2,-1,-1):
            sum = 0
            for j in range(i+1,n):
                sum = sum + a[i][j]*x[j]
            x[i] = (b[i] - sum)/a[i][i]
        return x
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

def coefficients(points, n, degree):
    m = degree + 1
    mat=[[]]
    vec=[]
    for i in range (m):
        vec.append(0)
    mat = [[0 for i in range(m)] for j in range (m)]
    for i in range (m):
        for j in range (i+1):
            k = i + j
            sum = 0;
            for l in range(n):
                sum = sum + (points[l][0])**k
            mat[i][j] = sum
            mat[j][i] = sum
        sum = 0
        for l in range (n):
            sum = sum + points[l][1] * ((points[l][0])**i)
        vec[i] = sum
    return mat, vec

def pol_reg(points,n,degree):
    mat, vec = coefficients(points, n, degree)
    x = gauss(mat, vec, degree + 1, 0.0001)
    return x


def cargar_matriz():
    try:
        global mat
        global integer_n
        global n
        
        global mini
        global maxi
        
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
        
        mini = mat[0][0]
        maxi = mat[0][0]
        
        for i in range (1,integer_n):
            if (mat[i][0]<mini):
                mini = mat[i][0]
            if (mat[i][0]>maxi):
                maxi = mat[i][0]
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
        grado = int(g.get())
         
        if (integer_n < (grado+1)):
            messagebox.showinfo("ERROR FATAL","Error. El número de puntos no puede ser menor al grado")
            raise Exception("Error. El número de puntos no puede ser menor al grado")
        
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        
        poli = pol_reg(mat,integer_n,grado)
        
        global funci
        
        #funci = ""
        
        '''
        factor = grado
        for i in range (grado):
            funci = funci + "(" + str(poli[i]) + "*(x**" + str(factor) + "))+"
            factor = factor - 1
        
        funci = funci + "(" + str(poli[grado]) + ")"
        '''
        
        funci = "(" + str(poli[0]) + ")"
        for i in range (1,grado+1):
            funci = funci + "+(" + str(poli[i]) + "*(x**" + str(i) + "))"
        
        textito = "El modelo que mejor se ajusta es:  " + funci
        messagebox.showinfo("Resultado",(textito))
        mostrar_resultado(funci,mat)
         
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
 
def regresion_poli():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Regresión polinomial")
    raiz.resizable(False,False)
    raiz.geometry("500x500")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Regresion Polinomial")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",25)) #tipo de letra
    label.place(x=45,y=15)
    
    label = Label(raiz,text="Métodos para ajustar curvas por regresion")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=50,y=70)
   
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
    
    label = Label(raiz,text="Ingrese grado del polinomio:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=49,y=320)
    
    global g
    g=Entry(raiz)
    g.place(x=320,y=322)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=150, y=350)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=350)
    
if __name__ == "__main__":
    
    regresion_poli()

  
    
    



