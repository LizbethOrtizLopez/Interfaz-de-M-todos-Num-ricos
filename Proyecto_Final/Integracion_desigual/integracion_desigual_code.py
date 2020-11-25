
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tkabrir
import os
import math

global n

def regla_traprecio(h, n, f):
    return (h/2) * (f[n-1] + f[n])

def sim38(h, f0, f1, f2, f3):
    return (3/8) * h * (f0 + (3 * f1) + (3 * f2) + f3)

def sim13mul(h, n, f):
    sum = f[0]
    for i in range(1, n-1, 2):
        sum = sum + (4 * f[i]) + (2 * f[i+1])
    sum = sum + (4 * f[n-1]) + f[n]
    return (h/3)*sum

def newton_cotes_equal(x, fx):
    n = len(fx) - 1
    a = x[0] * 1.0
    b = x[n] * 1.0
    h = (b-a)/n
    sum = 0.0
    if n == 1:
        sum = regla_traprecio(h, n, fx)
        print("trapecio: ", sum)
    else:
        m = n
        odd = math.fmod(n, 2)
        if odd > 0 and n > 1:
            sum = sum + sim38(h, fx[n-3], fx[n-2], fx[n-1], fx[n])
            print("simspon 3/8: ", sum)
            m = n-3
        if m > 1:
            sum = sum + sim13mul(h, m, fx)
            print("simspon 1/3: ", sum)
    return sum


def newton_cotes_unequal(x, fx):
    n = len(x) - 1
    current_h = float (x[1] - x[0])
    ultima_procesada = 0
    pos_actual = 1
    res = 0.0
    for i in range(1, n+1):
        if i < n:
            new_h = round(x[i+1] - x[i], 4)
            if new_h == current_h:
                pos_actual += 1
            else:
                print("x0 ", x[ultima_procesada], " xi ", x[pos_actual])
                res = res + newton_cotes_equal(x[ultima_procesada:(pos_actual+1)], fx[ultima_procesada:(pos_actual+1)])
                ultima_procesada = pos_actual
                pos_actual += 1
                current_h = new_h
        else:
            print("x0 ", x[ultima_procesada], " xi ", x[pos_actual])
            res = res + newton_cotes_equal(x[ultima_procesada:(pos_actual+1)], fx[ultima_procesada:(pos_actual+1)])
    return res

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

def cargar_vector1():
    try:
        global x
        global n
        
        integer_n = int(n.get())
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")

        file = tkinter.filedialog.askopenfilename()
        x = leerArchivo(file,integer_n)
        
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
    try:
        global n
        integer_n = int(n.get())
        
        integer_n = int(n.get())
            
        if (integer_n == 0):
            messagebox.showinfo("ERROR FATAL","Error. No pueden haber 0 conjuntos")
            raise Exception("Error. No pueden haber 0 conjuntos")
        
        resultado = newton_cotes_unequal(x,y)
        
        textito = "El resultado es: " + str(resultado)
        messagebox.showinfo("Respuesta",textito)
        
        
    except:
        messagebox.showinfo("ERROR FATAL","Hay un error con los datos o dejaste campos vacíos") 

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
    
    label = Label(top,text="Para el uso de este método deberás ingresar dos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="vectores con los valores de los puntos en x y f(x)" )
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="respectivamente en archivos .txt. Las puntos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text=" (x,f(x)) deben estar en la misma posicion en sus")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=115)
    
    label = Label(top,text="respectivos archivos (uno para x y otro para f(x)).")
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
    
    label = Label(top,text="de conjuntos (x,f(x)) que tienes en total. ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=215)
    
    label = Label(top,text="El uso de este método es para segmentos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=245)
    
    label = Label(top,text="separados por diferentes distancias. Verifica")
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
    
    label = Label(top,text="Integración para segmentos iguales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=305)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=345)
    
def integra_des():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Integración segmentos desiguales")
    raiz.resizable(False,False)
    raiz.geometry("500x400")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Integración de segmentos desiguales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",17)) #tipo de letra
    label.place(x=5,y=15)
    
    label = Label(raiz,text="Métodos de Integración Numérica")
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
    
    
    label = Label(raiz,text="Carga vector con puntos f(x):")
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
    
    integra_des()

  
    
    






