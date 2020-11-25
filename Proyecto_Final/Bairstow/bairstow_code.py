
from tkinter import *
import tkinter
import tkinter.filedialog as tkabrir
from tkinter import messagebox
import os
import math
import cmath

global n

def bairstrow (p, ed, r0, s0, maxiter, n):
    try:
        b = []
        c = []
        roots = []
        for i in range (n+1):
            b.append(0.0)
            c.append(0.0)
            roots.append(0.0 + 0j)
        itera = 0.0
        while itera < maxiter and n >= 3:
            itera = 0
            ea1 = 1
            ea2 = 1
            r = r0
            s = s0
            while itera < maxiter and (ea1 > ed or ea2 > ed):
                itera = itera + 1
                b[n] = p[n]
                b[n-1] = p[n-1] + r * b[n]
                c[n] = b[n]
                c[n-1] = b[n-1] + r + c[n]
                for i in range(n-2,-1,-1):
                    b[i] = p[i] + r * b[i+1] + s * b[i+2]
                    c[i] = b[i] + r + c[i+1] + s * c[i+2]
                det = c[2] * c[2] - c[3] * c[1]
                if math.fabs(det) > ed:
                    dr = (-b[1] * c[2] + b[0] * c[3])/det
                    ds = (-b[0] * c[2] + b[1] * c[1])/det
                    r = r + dr
                    s = s + ds
                    if math.fabs(r) > ed:
                        ea1 = math.fabs(dr/(r + dr))
                    if math.fabs(s) > ed:
                        ea2 = math.fabs(ds/(s + ds))
                else:
                    r = r + 1
                    s = s +1
                    itera = 0
            (c1,c2) = quadratic(-s, -r, 1)    
            roots[n-1] = c1
            roots[n-2] = c2
            n = n - 2
            for i in range (0,n+1):
                p[i] = b[i + 2]
        if n < 3:
            if n == 2:
                (c1,c2) = quadratic(p[0],p[1],p[2])
                roots[0] = c1
                roots[1] = c2
            else:
                roots[0] = p[0] / p[1]
        
        return roots
    
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo."),e

def quadratic (c, b, a):
    try:
        x0 = 0 + 0j
        x1 = 0 + 0j
        disc = (b**2) - 4 * a * c
        if disc >= 0:
            val = cmath.sqrt(disc)
            x0 = (-b + val)/(2 * a)+ 0j
            x1 = (-b - val)/(2 * a)+ 0j
        else:
            val = cmath.sqrt(-disc)
            x0 = complex(-b,val)/(2*a)
            x1 = complex(-b,-val)/(2*a)
        
        return (x0,x1)
    
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo."),e
        
    

def leerArchivo(file,n):
    
    try:   
        f = open(file, "r")
        v = []
        row = f.readline().split()
        for i in range(n+1):
            v.append(float(row[i]))
        # Cerramos el archivo.
        f.close()
        return v
    
    except:
        messagebox.showinfo("ERROR FATAL","Hubo un error con el archivo. Verifica se encuentre en buen estado, los coeficientes correspondan al grado del polinomio o que los datos sean correctos.")

def cargar_vector1():
    global x
    global n
    
    file = tkinter.filedialog.askopenfilename()
    x = leerArchivo(file,int(n.get()))
    
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
    
    label = Label(top,text="Para el uso de este método deberás ingresar un ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="polinomio de una sola variable. Se debe cargar")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="un archivo .txt que contenga los coeficientes")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="de los elementos del polinomio ordenados desde")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="la variable independiente hasta el coeficiente")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=135)
    
    label = Label(top,text="de la x de mayor grado. Los elementos deben")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=155)
    
    label = Label(top,text="estar separados por espacio. Ejemplo")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=175)
    
    label = Label(top,text="10 6 32 -> Donde 10 es la variable")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    label = Label(top,text="independiente, 6 el coeficiente de x, y 32 el")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    label = Label(top,text="coeficiente de x cuadrada")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=235)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=290)

def boton():
    try:  
        global n
        global x
        grado = int(n.get())
        
        if (grado<=0):
            messagebox.showinfo("ERROR FATAL","Grado incorrecto")
            raise Exception("Error. Grado incorrecto.")
        
        raices = []
        raices = bairstrow(x, 0.001, 1, 1, 50, grado)
        
        reales = "Raices reales: "
        imaginarias = "\nRaices imaginarias: "
        for i in range(grado):
            reales = reales + str(raices[i].real) + " "
            imaginarias = imaginarias + str(raices[i].imag) + " "        
        textito = reales + imaginarias 
        
        messagebox.showinfo("Resultado",textito)
    
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste un campo vacío"), e 
        
    
def bair_main():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Bairstow")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Bairstow")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=150,y=15)
    
    label = Label(raiz,text="Método para encontrar raíces de funciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=45,y=60)
   
    label = Label(raiz,text="Recomendamos se lean las intrucciones de uso")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=65,y=90)
    
    instruccion=Button(raiz,text="Intrucciones", width=10, command=instrucciones)
    instruccion.place(x=200, y=120)
    
    label = Label(raiz,text="Ingrese grado del polinomio:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=10,y=170)
    
    global n
    n=Entry(raiz)
    n.place(x=350,y=173)
      
    label = Label(raiz,text="Carga vector con coeficientes:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=210)
      
    calcular=Button(raiz,text="Cargar Vector", width=17, command=cargar_vector1)
    calcular.place(x=350, y=210)
    
    label = Label(raiz,text="Tu raices se calcularán con un error aproximado del 0.001%")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=15,y=250)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=150, y=300)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=300)
    
if __name__ == "__main__":
    
    bair_main()

  
    
    






