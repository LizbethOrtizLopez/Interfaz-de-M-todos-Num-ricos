
import os
import math
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tkabrir
from Descomposicion_LU import resuelve_lu
from Descomposicion_LU import descompone_lu

global n
global a
global b
global o

def formar_archivo():
    try:
        f = open('LU_resultado.txt','w')
        f.write(final)
        f.close()
        messagebox.showinfo("Archivo","Archivo generado con éxito")     
    except:
        messagebox.showinfo("ERROR FATAL","Ocurrió un error al generar el archivo.")

def cargar_archivo():
    try:
        global integer_n
        integer_n = int(n.get())
        
        if (integer_n<=0):
            messagebox.showinfo("ERROR FATAL","Tamaño de matriz incorrecto")
            raise Exception("Error. Tamaño de matriz incorrecto.")
        
        file = tkinter.filedialog.askopenfilename()
        a = descompone_lu.leerArchivo(file,integer_n)
        
        name=""
        i=len(file)-5
        while(str(file[i])!='/'):
            name+=str(file[i])
            i-=1
        nameArchivo = name[::-1]
        descompone_lu.DESCOMPOSELU(a,integer_n,0.01,nameArchivo)
        
        return 1
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto. Verifica tus datos."), e

def cargar_l():
    global a
    file = tkinter.filedialog.askopenfilename()
    a = resuelve_lu.leerArchivoA(file,int(n.get()))
      
def cargar_u():
    global o
    file = tkinter.filedialog.askopenfilename()
    o = resuelve_lu.leerArchivoO(file,int(n.get()))
    
def cargar_vector():
    global b
    file = tkinter.filedialog.askopenfilename()
    b = resuelve_lu.leerArchivoB(file,int(n.get()))
    
def intrucciones():
    return 1

def boton():
    
    try:
        global n
        global final
        global integer_n
     
        final = str(resuelve_lu.SOLVE(a,o,integer_n,b))
        textito = "Los valores resultantes son " + str(final)
        messagebox.showinfo("Resultado",textito)
         
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste el campo vacío"), e
    except:
        messagebox.showinfo("ERROR FATAL","No cargaste alguno de los archivos")
    
def L_U():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Descomposición LU")
    raiz.resizable(False,False)
    raiz.geometry("500x500")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Descomposición LU")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=40,y=15)
    
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
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=boton)
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
    
    label = Label(raiz,text="Selecciona matriz a descomponer:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=210)
    
    matriz=Button(raiz,text="Abrir", width=17, command=cargar_archivo)
    matriz.place(x=350, y=210)
    
     
    label = Label(raiz,text="Carga matriz L:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=195,y=250)
    
    calcular=Button(raiz,text="Cargar L", width=17, command=cargar_l)
    calcular.place(x=350, y=250)
    
    label = Label(raiz,text="Carga matriz U:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=195,y=290)
    
    calcular=Button(raiz,text="Cargar U", width=17, command=cargar_u)
    calcular.place(x=350, y=290)
    
    label = Label(raiz,text="Carga vector:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=213,y=330)
    
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector)
    calcular.place(x=350, y=330)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=50, y=400)
    
    gene=Button(raiz,text="Guardar resultado", width=15, command=formar_archivo)
    gene.place(x=200, y=400)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=400, y=400)
    
if __name__ == "__main__":
    
    L_U()

  
    
    


