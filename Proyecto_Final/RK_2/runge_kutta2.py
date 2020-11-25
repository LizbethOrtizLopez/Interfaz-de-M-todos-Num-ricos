
from tkinter import *

import math
global tex_func
from tkinter import messagebox
import tkinter
import tkinter.filedialog as tkabrir
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def mostrar_resultado(arr_x,arr_y):
    
    plt.plot(arr_x,arr_y)
    plt.ylabel("Eje y")
    plt.show()

def formar_archivo(arr_x, arr_y):
    try:
        global integer_n
        global final
        f = open('puntos.txt','w')
        
        f.write('Puntos en x: \n')
        for i in range (len(arr_x)):
            f.write(str(arr_x[i])+" ")
        
        f.write('\nPuntos en y: \n')
        for i in range (len(arr_y)):
            f.write(str(arr_y[i])+" ")    
            
        f.close
        messagebox.showinfo("Resultado","El resultado ha sido ejecutado con éxito")
        messagebox.showinfo("Archivo","Archivo generado con éxito")
        
    except:
        messagebox.showinfo("ERROR FATAL","Ocurrió un error al generar el archivo.")


def rk2(x,y,h):
    k_1 = eval_func(x,y)
    k_2 = eval_func(x+0.75*h,y+0.75*k_1*h)
    slope = (1/3) * k_1 + (2/3) * k_2
    y_new = y + slope*h
    x_new = x + h
    return (x_new,y_new)

def eval_func(x,y):
    try:
        global tex_func
        return eval(tex_func)
    except:
        print("Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
        messagebox.showinfo("ERROR FATAL","Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
       
def rk(xl,xr,h,ini_c,output_interval):
    x = xl
    y = ini_c
    x_values = [xl]
    y_values = [ini_c]
    while x < xr:
        x_end = x + output_interval 
        if x_end > xr :
            x_end = xr
        (x,y) = fine_steps(x,y,h,x_end)
        x_values.append(x)
        y_values.append(y)
    return x_values,y_values

def fine_steps(x,y,h,x_end):
    x_new = x
    y_new = y
    while x_new < x_end:
        if x_end - x_new < h:
            h = x_end - x_new
        res = rk2(x_new,y_new,h)
        x_new = res[0]
        y_new = res[1]
    return (x_new,y_new)

def boton():
    try:
        global cuadroLimit1
        global cuadroLimit2
        global h
        global f0
        global out

        H = float(h.get())
        F0 = float(f0.get())
        OUT = float(out.get())
        
        infe = float(cuadroLimit1.get())
        supe = float(cuadroLimit2.get())
        
        if (H==0 or OUT==0):
            messagebox.showinfo("ERROR FATAL","Error. El aumento de paso y el aumento de salida no pueden ser 0")
            raise Exception("Error. El aumento de paso y el aumento de salida no pueden ser 0")
        
        if (infe>supe):
            messagebox.showinfo("ERROR FATAL","Error. El límite inferior no puede ser mayor al superior")
            raise Exception("Error. El límite inferior no puede ser mayor al superior")
            
        if (infe==supe):
            messagebox.showinfo("ERROR FATAL","Error. Los intervalos no pueden ser iguales")
            raise Exception("Error.Los intervalos no pueden ser iguales")
        
        global textoFuncion
        global tex_func
        tex_func = textoFuncion.get(1.0,END)
        
        arr_x , arr_y = rk(infe,supe,H,F0,OUT)
        formar_archivo(arr_x, arr_y)
        
        mostrar_resultado(arr_x,arr_y)
        
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste un campo vacío"), e
    
def instrucciones():
    top = Toplevel()
    top.title("Instrucciones")
    top.resizable(False,False)
    top.geometry("620x470")
    
    top.config(bg="deepskyblue4")
    
    label = Label(top,text="Instrucciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",20)) #tipo de letra
    label.place(x=180,y=15)
    
    label = Label(top,text="Para el uso de este método deberás ingresar una función. Para ello,")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=55)
    
    label = Label(top,text="deberá estar escrita con el formato de paréntesis. Ejemplo:(x+y)+2")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
     
    label = Label(top,text="En caso de usar potencias, estas deberán estar expresadas por")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=105)
    
    label = Label(top,text="doble asterisco (**). Ejemplo: Para x cuadrada: (x**2).")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=125)
    
    label = Label(top,text="Para x cúbica: (x**3)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=145)
    
    label = Label(top,text="Las funciones trigonométricas deberán estar acompañadas de la")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=175)
    
    label = Label(top,text="palabra 'math'. Ejemplo: math.sin(x), math.cos(x), math.atan(x)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=195)
    
    label = Label(top,text="Las multiplicaciones deben expresarse por asteriscos. Ejemplo:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=225)
    
    label = Label(top,text="Ejemplo: (5*2), (3*x), (10*2*3)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=245)
    
    label = Label(top,text="Al final, podrías tener un ejemplo como:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=270)
    
    label = Label(top,text="math.sin(x)+(x**2)+(2*x)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=380,y=270)
    
    label = Label(top,text="En el programa deberás ingresar los valores de:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=300)
    
    label = Label(top,text="-h = aumento de paso para x")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=320)
    
    label = Label(top,text="-La evaluación de f(0)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=340)
    
    label = Label(top,text="-Intervalo de salida (cada cuanto se mostrarán puntos)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=360)
    
    label = Label(top,text="Finalmente, se generará un archivo .txt con los puntos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=380)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=260, y=420)
    
def rk2_main():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Método de Runge Kutta de segundo orden")
    raiz.resizable(False,False)
    raiz.geometry("600x550")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Método de Runge Kutta de segundo orden")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",19)) #tipo de letra
    label.place(x=10,y=15)
    
    label = Label(raiz,text=" Método para la solución de ecuaciones diferenciales ordinarias")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=70)
   
    label = Label(raiz,text="Recomendamos leer las instrucciones primero antes de ejecutar:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=45,y=100)
    
    calcular=Button(raiz,text="Instrucciones", width=15, command=instrucciones)
    calcular.place(x=235, y=130)
    
    label = Label(raiz,text="Ingresa función a evaluar:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=170)
    
    global textoFuncion
    textoFuncion=Text(raiz, width=70, height=3)
    textoFuncion.place(x=10, y=210)
    
    label = Label(raiz,text="Ingresa número de intervalo inferior:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=270)
    global cuadroLimit1
    cuadroLimit1=Entry(raiz)
    cuadroLimit1.place(x=370,y=272)
    
    label = Label(raiz,text="Ingresa número de intervalo superior:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=300)
    global cuadroLimit2
    cuadroLimit2=Entry(raiz)
    cuadroLimit2.place(x=370,y=302)
    
    label = Label(raiz,text="Ingresa el aumento de paso:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=340)
    global h
    h=Entry(raiz)
    h.place(x=370,y=342)
    
    label = Label(raiz,text="Ingresa evaluación de f(0):")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=380)
    global f0
    f0=Entry(raiz)
    f0.place(x=370,y=382)
    
    label = Label(raiz,text="Ingresa el intervalo de salida:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=420)
    
    global out
    out=Entry(raiz)
    out.place(x=370,y=422)
    
    label = Label(raiz,text="Te recordamos este método no asegura una salida confiable")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=10,y=465)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=150, y=500)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=350, y=500)


if __name__ == "__main__":
    
    rk2_main()

  
    
    



