
import tkinter.filedialog as tkabrir
from tkinter import *
from tkinter import messagebox
import tkinter
import os
import math

global n
global integer_n
global mat
global vec

def formar_archivo():
    try:
        global integer_n
        global x
        f = open('gauss_resultado.txt','w')
        for i in range (integer_n):
            f.write(str(x[i])+" ")
        f.close
        messagebox.showinfo("Archivo","Archivo generado con éxito")
    except:
        messagebox.showinfo("ERROR FATAL","Ocurrió un error al generar el archivo.")

def gauss_seidel(a,b,n,x_prima,imax,tol,lamda):    
    global x
    x = x_prima
    for i in range (n): 
        dummy = a[i][i]
        if math.fabs(dummy) > tol :
            for j in range (n):
                a[i][j] = a[i][j]/dummy
            
            b[i] = b[i]/dummy
        else:
            messagebox.showinfo("ERROR FATAL","Error. Hay un cero en la diagonal de la matriz")
            return "Error. Hay un cero en la diagonal"
    
    for i in range (n):
        suma = b[i]
        for j in range (n):
            if i!= j:
                suma = suma - (a[i][j] * x[j])
        
        xi = suma   
    itera = 1
    sentinel = True
    while (sentinel ==True) and (itera < imax): 
        sentinel = False
        for i in range (n):
            old = x[i]
            suma = b[i]
            for j in range (n):
                if i!=j:
                    suma = suma - (a[i][j] * x[j])
            
            x[i] = lamda * suma + (1-lamda) * old
            if (sentinel == False) and math.fabs(x[i]) > tol:
                ea = math.fabs((x[i]-old)/x[i])
                if ea > tol: #el error deseado 'ed' es la tolerancia
                    sentinel = True
        itera = itera +1
    
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
        
        integer_n = int(n.get())
        x_prima = []
         
        for i in range (integer_n):
            x_prima.append(0)
             
        if (integer_n<=0):
            messagebox.showinfo("ERROR FATAL","Tamaño de matriz incorrecto")
            raise Exception("Error. Tamaño de matriz incorrecto.")
        
        textito = "Los valores resultantes son " + str(gauss_seidel(mat,vec,integer_n,x_prima,10,0.01,1))
        messagebox.showinfo("Resultado",textito)
         
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste un campo vacío"), e
    except:
        messagebox.showinfo("ERROR FATAL","No cargaste alguno de los archivos")
    
def seidel():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Gauss-Seidel")
    raiz.resizable(False,False)
    raiz.geometry("500x500")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Guass-Seidel")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=110,y=15)
    
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
    
    label = Label(raiz,text="Este método no es efectivo para ciertos problemas")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=30,y=330)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=100, y=370)
    
    gene=Button(raiz,text="Guardar resultado", width=15, command=formar_archivo)
    gene.place(x=200, y=370)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=370)
    
if __name__ == "__main__":
    
    seidel()

  
    
    





