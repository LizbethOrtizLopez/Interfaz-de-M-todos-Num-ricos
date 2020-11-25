
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import os
import math

global n
global integer_n
global mat
global vec

def formar_archivo():
    try:
        global integer_n
        global final
        f = open('gauss_resultado.txt','w')
        for i in range (integer_n):
            f.write(str(final[i])+" ")
        f.close
        messagebox.showinfo("Archivo","Archivo generado con éxito")
    except:
        messagebox.showinfo("ERROR FATAL","Ocurrió un error al generar el archivo.")

def g(a,b,n,tol):
    
    global final
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
        final = substitute(aa,bb,n)
    return final

def eliminate(a, b, s, n, tol):
    for k in range(n - 1):
        (a, b, s) = pivot(a, b, s, n, k)
        if math.fabs(a[k][k] / s[k]) < tol:
            messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo")
            return a,b,True #error
        
        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] -= (factor * a[k][j])
            b[i] -= factor * b[k]

    if math.fabs(a[n - 1][n - 1] / s[n - 1]) < tol:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo")
        return a,b,True #error
    return a, b, False

def pivot(a, b, s, n, k):
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


def substitute(a,b,n):
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

def cargar_matriz():
    
    try:
        global mat
        global integer_n
        global n
        integer_n = int(n.get())
        file = tkinter.filedialog.askopenfilename()
        f = open(file, "r")
        # Vamos a leer la matriz
        mat = []
        for i in range(integer_n):
            mat.append([])
            row = f.readline().split()
            for j in range(integer_n):
                mat[i].append(float(row[j]))
        f.close()
        return mat
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","La matriz está incompleta. Verifica tus datos."), e
      
def cargar_vector():
    try:
        global vec
        global n
        global integer_n
        aux = n.get()
        integer_n = int(aux)
        file = tkinter.filedialog.askopenfilename()
        f = open(file, "r")
        vec = []
        row = f.readline().split()
        for i in range(integer_n):
            vec.append(float(row[i]))
        # Cerramos el archivo.
        f.close()
        return vec
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El vector está incompleto. Verifica tus datos."), e
    
def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("450x450")
    
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
    
    label = Label(top,text="matriz y un vector con los valores independien-" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="tes de la matriz. Deberán ser dos archivos .txt")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="que contenga los valores de los elementos.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="Ejemplo de matriz: ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=135)
    
    label = Label(top,text="5 16 -10")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=155)
    
    label = Label(top,text="2 5 8")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=175)
    
    label = Label(top,text="6 7 9")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    label = Label(top,text="Ejemplo de vector:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    label = Label(top,text="2 9 7    ---> Donde el primer elemento es la ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=235)
    
    label = Label(top,text="              variable independiente de la")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=255)
    
    label = Label(top,text="              primera fila de la matriz")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=275)
    
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=330)

def boton():
    try:
        global n
        global integer_n
        global mat
        global vec
        aux = n.get()
        integer_n = int(aux)
        
        if (integer_n<=0):
            messagebox.showinfo("ERROR FATAL","Tamaño de matriz incorrecto")
            raise Exception("Error. Tamaño de matriz incorrecto.")
        
        textito = "Los valores resultantes son " + str(g(mat,vec,integer_n,0.01))
        messagebox.showinfo("Resultado",textito)
        
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste el campo vacío"), e
    except:
        messagebox.showinfo("ERROR FATAL","No cargaste alguno de los archivos")
        
def gauss():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Eliminación de Gauss")
    raiz.resizable(False,False)
    raiz.geometry("500x500")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Eliminación de Gauss")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=10,y=15)
    
    label = Label(raiz,text=" Método para sistemas de ecuaciones lineales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=25,y=70)
   
    label = Label(raiz,text="Recomendamos se lean las intrucciones de uso")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=70,y=100)
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=instrucciones)
    instruccion.place(x=200, y=130)
    
    label = Label(raiz,text="Ingrese tamaño de la matriz:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=49,y=170)
    global n
    n=Entry(raiz)
    n.place(x=350,y=173)
    
    label = Label(raiz,text="Selecciona matriz a evaluar:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=49,y=210)
    
    matriz=Button(raiz,text="Abrir", width=17, command=cargar_matriz)
    matriz.place(x=350, y=210)
    
    label = Label(raiz,text="Carga vector:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=213,y=250)
    
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector)
    calcular.place(x=350, y=250)
    
    label = Label(raiz,text="Tus resultados tendrán un error del 0.01%")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=50,y=290)
    
    label = Label(raiz,text="¡Recuerda verificar tus datos!")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=100,y=320)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=100, y=360)
    
    gene=Button(raiz,text="Guardar resultado", width=15, command=formar_archivo)
    gene.place(x=200, y=360)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=360)
    
if __name__ == "__main__":
    
    gauss()

  
    
    



