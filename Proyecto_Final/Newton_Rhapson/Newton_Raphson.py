
from tkinter import *
from tkinter import messagebox
import math
global tex_func
global tex_der
global raiz

def result(x0, maxiter, ed):
    xold = x0
    ea = 101
    ite = 0
    while ite < maxiter and ea > ed:
        xnew = xold - ((eval_func_normal(xold))/(eval_func_derivada(xold)))
        if math.fabs(xnew) > 0.0:
            ea = math.fabs((xnew-xold)/xnew) * 100
        xold = xnew
        ite += 1
    return xold

def eval_func_normal(x):
    try:
        global tex_func
        return eval(tex_func)
    except:
        print("Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
        messagebox.showinfo("ERROR FATAL","Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
    
def eval_func_derivada(y):
    try:
        global tex_der
        return eval(tex_der)
    except:
        print("Error. La derivada fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
        messagebox.showinfo("ERROR FATAL","Error. La derivada fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")

def boton():
    
    try:
        global cuadroLimit1
        global cuadroLimit2
    
        x0 = float(cuadroLimit1.get())
        maxi = int(cuadroLimit2.get())
    
        global textoFuncion
        global tex_func
        tex_func = textoFuncion.get(1.0,END)
    
        global textoDerivada
        global tex_der
        tex_der = textoDerivada.get(1.0,END)
    
        textito = "Las raices de tu función son: " + str(result(x0,maxi,0.001))
        messagebox.showinfo("Resultado",textito)
        
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido o dejaste un campo vacío"), e
    
    
def instrucciones_boton():
    
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
    
    label = Label(top,text="función y derivada. Para ello, debe escribirse")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="con el formato de paréntesis. Ejemplo: (x+y) + 2")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=95)
    
    label = Label(top,text="En caso de usar potencias, estas deberán estar")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=125)
    
    label = Label(top,text="expresadas por doble asterisco (**). Ejemplo ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=145)
    
    label = Label(top,text="Para x cuadrada: (x**2). Para x cúbica: (x**3)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=165)
    
    label = Label(top,text="Las funciones trigonométricas deberán estar")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=200)
    
    label = Label(top,text="acompañadas de la palabra 'math.'")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=220)
    
    label = Label(top,text="Ejemplo: math.sin(x), math.cos(x), math.atan(x)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=240)
    
    label = Label(top,text="Las multiplicaciones deben expresarse por")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=270)
    
    label = Label(top,text="asteriscos. Ejemplo: (5*2), (3*x), (10*2*3)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=290)
    
    label = Label(top,text="Al final, podrías tener un ejemplo como:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=320)
    
    label = Label(top,text="math.sin(x) + (x**2) + (2*x)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=340)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=200, y=390)
    
def newton_raphson():
    
    global raiz
    raiz = Toplevel()
    raiz.title("BNewton-Raphson")
    raiz.resizable(False,False)
    raiz.geometry("600x550")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Método de Newton-Raphson")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=10,y=15)
    
    label = Label(raiz,text=" Método para encontrar raíces de funciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=80,y=70)
   
    label = Label(raiz,text="Recomendamos leer las instrucciones primero antes de ejecutar:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=45,y=100)
    
    calcular=Button(raiz,text="Instrucciones", width=15, command=instrucciones_boton)
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
    
    label = Label(raiz,text="Ingresa derivada de la función:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=273)
    
    global textoDerivada
    textoDerivada=Text(raiz, width=70, height=3)
    textoDerivada.place(x=10, y=310)
    
    label = Label(raiz,text="Ingresa valor de x0:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=375)
    global cuadroLimit1
    cuadroLimit1=Entry(raiz)
    cuadroLimit1.place(x=370,y=377)
     
    label = Label(raiz,text="Ingresa maxitermino:")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=405)
    global cuadroLimit2
    cuadroLimit2=Entry(raiz)
    cuadroLimit2.place(x=370,y=407)
   
    label = Label(raiz,text="Tu raices se calcularán con un error aproximado del 0.001%")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=50,y=440)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=200, y=480)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=480)
    

if __name__ == "__main__":
    
    newton_raphson()

  
    
    

