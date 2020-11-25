
from tkinter import *
from tkinter import messagebox
import math
global tex_func
global raiz

def falsa_posicion(x_l, x_r, tol):
  candidate = math.fabs(eval_func(x_l)) * math.fabs(eval_func(x_r))
  while candidate > 0:
      temp = x_r - ((eval_func(x_r) * (x_r - x_l)) / (eval_func(x_r) - eval_func(x_l)))
      candidate = math.fabs(eval_func(temp))
      if candidate < tol:
          return temp
      else :
          test = eval_func(x_l) * eval_func(temp)
          if test > 0:
              x_l = temp
          else:
              x_r = temp
  return temp  

def eval_func(x):
    try:
        global tex_func
        return eval(tex_func)
    except:
        print("Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")
        messagebox.showinfo("ERROR FATAL","Error. La función fue ingresada de forma incorrecta o el campo está vacío. Intentalo de nuevo")

def boton():
    
    try:
        global cuadroLimit1
        global cuadroLimit2
        limit1 = cuadroLimit1.get()
        limit2 = cuadroLimit2.get()
    
        infe = float(limit1)
        supe = float(limit2)
    
        global textoFuncion
        global tex_func
        tex_func = textoFuncion.get(1.0,END)
    
        if (infe>supe):
            messagebox.showinfo("ERROR FATAL","Error. El límite inferior no puede ser mayor al superior")
            raise Exception("Error. El límite inferior no puede ser mayor al superior")
        
        if (infe==supe):
            messagebox.showinfo("ERROR FATAL","Error. Los intervalos no pueden ser iguales")
            raise Exception("Error.Los intervalos no pueden ser iguales")
    
        textito = "Las raices de tu función son: " + str(falsa_posicion(infe,supe,0.001))
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
    
    label = Label(top,text="función. Para ello, deberá estar escrita con el")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=75)
    
    label = Label(top,text="formato de paréntesis. Ejemplo: (x+y) + 2")
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
    
def falsa_pos():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Falsa Posición")
    raiz.resizable(False,False)
    raiz.geometry("600x450")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Falsa Posición")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",30)) #tipo de letra
    label.place(x=120,y=15)
    
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
    
    label = Label(raiz,text="Tu raices se calcularán con un error aproximado del 0.001%")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=50,y=340)
    
    calcular=Button(raiz,text="Calcular", width=7, command=boton)
    calcular.place(x=200, y=380)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=380)
    

if __name__ == "__main__":
    
    falsa_pos()

  
    
    

