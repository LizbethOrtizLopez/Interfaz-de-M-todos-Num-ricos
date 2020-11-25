
from tkinter import *


def siguiente():
    top = Toplevel()
    top.title("Ayuda")
    top.resizable(False,False)
    top.geometry("800x600")
    
    top.config(bg="deepskyblue4")
    
    label = Label(top,text="Integración numérica")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=20)
    
    label = Label(top,text="Estos métodos te darán el resultado del área bajo la curva de n cantidad de puntos, es")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=40)
    
    label = Label(top,text="decir, el resultado de una integral basado solamente en los puntos que conforman la")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=60)
    
    label = Label(top,text="gráfica.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=80)
     
    label = Label(top,text="Solución de Ecuaciones Diferenciales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=110)
    
    label = Label(top,text="Estos métodos te regresarán una serie de puntos (almacenados en un archivo .txt) que se ajusten a")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=130)
    
    label = Label(top,text="los puntos dados de una ecuación diferencial ordinaria. Dependiendo las características")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=150)
    
    label = Label(top,text="del métodos, deberás ingresar otros factores, como el intervalo x en el que se")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=170)
    
    label = Label(top,text="encuentran los puntos, evaluaciones de f(x), así como parámetros de seguimiento ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=190)
    
    label = Label(top,text="y ajuste.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=210)
    
    label = Label(top,text="CLARIFICACIONES")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",14)) #tipo de letra
    label.place(x=10,y=250)
    
    label = Label(top,text="Newton-Raphson, Secante y Secante Modificada")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=10,y=280)
    
    label = Label(top,text="El maxitermino es el número de iteraciones a realizar")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=300)
    
    label = Label(top,text="Descomposición LU")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=10,y=330)
    
    label = Label(top,text="Se crearán dos archivos para las matrices L y U")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=350)
    
    label = Label(top,text="Integración numérica")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=10,y=380)
    
    label = Label(top,text="Cada método tiene situciones y aplicaciones diferentes. Verifica bien tu información.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=410)
    
    label = Label(top,text="Existen métodos en los cuales podrás guardar archivos con la información del resultado.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=435)
    
    label = Label(top,text="Estos archivos se guardarán en la misma carpeta que se encuentra este ejecutable.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=455)
    
    label = Label(top,text="Siempre verifica tus datos antes de ejecutar los métodos para evitar errores.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=480)
    
    label = Label(top,text="¡DISFRUTALO!")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",14)) #tipo de letra
    label.place(x=10,y=510)
    
    label = Label(top,text="Autores: Lizbeth Ortiz, Marlene Rodríguez, Erick Montan")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=150,y=510)
    
    destroy=Button(top,text="Volver", width=7, command=top.destroy)
    destroy.place(x=350, y=550)

 
def inicio():
    
    global raiz
    raiz = Toplevel()
    raiz.title("Ayuda")
    raiz.resizable(False,False)
    raiz.geometry("800x600")
    
    raiz.config(bg="deepskyblue4")
    
    label = Label(raiz,text="Bienvenido al menú de métodos numéricos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",24)) #tipo de letra
    label.place(x=20,y=15)
    
    label = Label(raiz,text="Los métodos numéricos presentados a continuación te servirán para resolver diferentes")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=70)
   
    label = Label(raiz,text="problemas. Cada método está categorizado según el problema que está supuesto a resolver.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",10)) #tipo de letra
    label.place(x=10,y=90)
    
    label = Label(raiz,text="Métodos para encontrar raíces de funciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=130)
    
    
    label = Label(raiz,text="Con estos métodos podrás conoces las raices (puntos de x donde f(x) = 0) con ingresar")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=150)

    label = Label(raiz,text="la función que quieras evaluar (y otros parámetros propios del método).")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=170)

    label = Label(raiz,text="Sistemas de ecuaciones lineales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=200)
    
    label = Label(raiz,text="Con estos métodos encontrarás los valores de las variables de un sistema de ")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=220)
    
    label = Label(raiz,text="ecuaciones. Todos ellos se manejan a través del uso de matrices. Es muy importante")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=240)
    
    label = Label(raiz,text="conozcas de antemano como se manejan matrices con coeficientes de sistemas de")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=260)
    
    label = Label(raiz,text="ecuaciones lineales, así como el uso de vectores con valores independientes para")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=280)
    
    label = Label(raiz,text="algunos casos.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=300)
    
    label = Label(raiz,text="Ajuste de curvas por regresión")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=330)
    
    label = Label(raiz,text="Si tienes un conjunto de puntos con cierto comportamiento, los métodos de ajuste de")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=350)
    
    label = Label(raiz,text="curvas te mostrarán el modelo y/o regresión que mejor se ajuste a los puntos dados.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=370)
    
    label = Label(raiz,text="Para estos métodos deberás manejar archivos .txt con valores de las variables según sea")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=390)
    
    label = Label(raiz,text="el caso. Podrás visualizar en pantalla la regresión ofrecida.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=410)
    
    label = Label(raiz,text="Ajuste de curvas por interpolación")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue3", #fondo para todas la GUI
                 font=("Courier",13)) #tipo de letra
    label.place(x=10,y=440)
    
    label = Label(raiz,text="Este método te regresará un polinomio que se ajuste mejor a la serie de puntos (x,y)")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=470)
    
    label = Label(raiz,text="al igual que una representación gráfica de la función regresada.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=10,y=490)
    
    destroy=Button(raiz,text="Volver", width=7, command=raiz.destroy)
    destroy.place(x=300, y=530)
    
    destroy=Button(raiz,text="Siguiente", width=10, command=siguiente)
    destroy.place(x=400, y=530)
    

if __name__ == "__main__":
    
    inicio()

  
    
    

