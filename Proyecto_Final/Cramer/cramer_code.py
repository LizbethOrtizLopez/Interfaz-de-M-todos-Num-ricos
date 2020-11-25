
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import os
import math

global n
global integer_n
global matriz

def formar_archivo():
    try:
        global integer_n
        global res
        f = open('cramer_resultado.txt','w')
        for i in range (integer_n):
            f.write(str(res[i])+" ")
        f.close
        messagebox.showinfo("Archivo","Archivo generado con éxito")
    except:
        messagebox.showinfo("ERROR FATAL","Ocurrió un error al generar el archivo.")
        
def sarrus3x3(mat):
    val = ((mat[0][0 ] *mat[1][1 ] *mat[2][2]) +
           (mat[0][1 ] *mat[1][2 ] *mat[2][0]) +
           (mat[0][2 ] *mat[1][0 ] *mat[2][1])) - \
          ((mat[2][0 ] *mat[1][1 ] *mat[0][2]) +
           (mat[2][1 ] *mat[1][2 ] *mat[0][0]) +
           (mat[2][2 ] *mat[1][0 ] *mat[0][1]))
    return val

def sarrus2x2(mat):
    val = ((mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0]))
    return val

def cramer_result(mat):
    n = len(mat)
    if n == 3:
        global res
        res = [0.0, 0.0, 0.0]
        mat_x = [[mat[0][3], mat[0][1], mat[0][2]],
                 [mat[1][3], mat[1][1], mat[1][2]],
                 [mat[2][3], mat[2][1], mat[2][2]]]
        mat_y = [[mat[0][0], mat[0][3], mat[0][2]],
                 [mat[1][0], mat[1][3], mat[1][2]],
                 [mat[2][0], mat[2][3], mat[2][2]]]
        mat_z = [[mat[0][0], mat[0][1], mat[0][3]],
                 [mat[1][0], mat[1][1], mat[1][3]],
                 [mat[2][0], mat[2][1], mat[2][3]]]
        det_mat = sarrus3x3(mat)
        if det_mat == 0:
            messagebox.showinfo("ERROR FATAL","El determinante de la matriz es 0. No hay solución")
        else:
            det_matx = sarrus3x3(mat_x)
            det_maty = sarrus3x3(mat_y)
            det_matz = sarrus3x3(mat_z)
            res[0] = det_matx / det_mat
            res[1] = det_maty / det_mat
            res[2] = det_matz / det_mat
    else:
        res = [0.0, 0.0]
        mat_x = [[mat[0][2], mat[0][1]],
                 [mat[1][2], mat[1][1]]]
        mat_y = [[mat[0][2], mat[0][0]],
                 [mat[1][2], mat[1][0]]]
        det_mat = sarrus2x2(mat)
        if det_mat == 0:
            messagebox.showinfo("ERROR FATAL","El determinante de la matriz es 0. No hay solución")
        else:
            det_matx = sarrus2x2(mat_x)
            det_maty = sarrus2x2(mat_y)
            res[0] = det_matx/det_mat
            res[1] = det_maty/det_mat
    return res

def cargar_matriz():
    try:
        global matriz
        global integer_n
        global n
        integer_n = int(n.get())
        file = tkinter.filedialog.askopenfilename()
        f = open(file, "r")
        # Vamos a leer la matriz
        matriz = []
        for i in range(integer_n):
            matriz.append([])
            row = f.readline().split()
            for j in range(integer_n+1):
                matriz[i].append(float(row[j]))
        f.close()
        return matriz
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","La matriz está incompleta. Verifica tus datos."), e
    
def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("450x370")
    
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
    
    label = Label(top,text="matriz a evaluar. Esta matriz deberá estar" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="en formato .txt que contenga los valores de los")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="elementos (incluyendo valores independientes).")
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
    
    label = Label(top,text="6 7 9  ---> Donde los primeros 2x2 elementos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    label = Label(top,text="            son los valores de la matriz, y")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    label = Label(top,text="            el resto son valores independientes")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=235)
    
    label = Label(top,text="En tamaño de la matriz debes ingresarlo en")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=255)
    
    label = Label(top,text="función de las variables. (Para el ejemplo")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=275)
    
    label = Label(top,text="anterior el tamaño sería 2).")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=295)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=330)

def boton():
    try:
        global n
        global integer_n
        global matriz
        integer_n = int(n.get())
        
        if (integer_n<=1 or integer_n>=4):
            messagebox.showinfo("ERROR FATAL","Tamaño de matriz incorrecto")
            raise Exception("Error. Tamaño de matriz incorrecto.")
        
        textito = "Los valores resultantes son " + str(cramer_result(matriz))
        messagebox.showinfo("Resultado",textito)
        
    except:
        messagebox.showinfo("ERROR FATAL","No cargaste alguno de los archivos")
        
def cramer_main():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Regla de Cramer")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Regla de cramer")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=60,y=15)
    
    label = Label(raiz,text="Método para sistemas de ecuaciones lineales")
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
    
    label = Label(raiz,text="¡Recuerda verificar tus datos!")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=100,y=260)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=100, y=330)
    
    gene=Button(raiz,text="Guardar resultado", width=15, command=formar_archivo)
    gene.place(x=200, y=330)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=330)
    
if __name__ == "__main__":
    
    cramer_main()

  
    
    




