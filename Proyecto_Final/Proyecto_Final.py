
from tkinter import *
from Biseccion import biseccion
from Falsa_Pos import falsa_posicion
from Newton_Rhapson import Newton_Raphson
from Secante import secante
from Secante_Modificada import secante_modificada
from Bairstow import bairstow_code

from Cramer import cramer_code
from Gauss import gauss_code
from Gauss_Jordan import gauss_jordan_code
from Gauss_Seidel import gauss_seidel_code
from Descomposicion_LU import LU
from Descomposicion_LU import resuelve_lu

from Regresion_Lineal import regre_lineal
from Linearizacion_ln import linearizacion_ln_code
from Linearizacion_base10 import linearizacion_base_10
from Regresion_polinomial import regresion_polinomial_code

from Interpolacion_Newton import interpolacion_newton_code
from Interpolacion_Lagrange import interpolacion_lagrange_code
from Interpolacion_Inversa import interpolacion_inversa_code
from Interpolacion_Inversa import bairstow
from Interpolacion_Inversa import lagrange

from Integracion_desigual import integracion_desigual_code
from Integracion_iguales import integracion_iguales_code

from Euler import Euler
from RK_2 import runge_kutta2
from RK_4 import runge_kutta4

import conocer

def biseccion_button():  
    biseccion.biseccion()
    
def falsa_pos_button():  
    falsa_posicion.falsa_pos()
    
def newton_raphson_button(): 
    Newton_Raphson.newton_raphson()

def secante_button():
    secante.secante_main()

def secante_modificada_button():
    secante_modificada.sec_m()
    
def bairstrow_button():
    bairstow_code.bair_main()
    
def cramer_button():
    cramer_code.cramer_main()
  
def gauss_button():  
    gauss_code.gauss()

def gauss_jordan_button():  
    gauss_jordan_code.gauss_J()

def gauss_seidel_button():  
    gauss_seidel_code.seidel()
    
def LU_button():
    LU.L_U()
    
def minimo_cuadrado_button():  
    regre_lineal.re_l()
    
def linearizacion_ln_button():  
    linearizacion_ln_code.re_ln()
    
def linearizacion_log_button():  
    linearizacion_base_10.re_log10()
    
def regresion_polinomial_button():  
    regresion_polinomial_code.regresion_poli()
    
def regresion_varias_button():  
    #biseccion.biseccion()
     return True;
    
def interpolacion_newton_button():  
    interpolacion_newton_code.inter_newton()
    
def interpolacion_lagrange_button():  
    interpolacion_lagrange_code.inter_lagrange()
    
def interpolacion_inversa_button():  
    interpolacion_inversa_code.inter_inversa()
    
def integracion_iguales_button():  
    integracion_iguales_code.integra_igual()
    
def integracion_desiguales_button():  
    integracion_desigual_code.integra_des()
    
def euler_button():
    Euler.euler_main()
    
def rk2_button():  
    runge_kutta2.rk2_main()

def rk4_button():  
    runge_kutta4.rk4_main()
    
def conoce():
    conocer.inicio()
    

if __name__ == '__main__':
    
    raiz = Tk()
    raiz.title("Menú de Métodos Numéricos")
    raiz.resizable(False,False)
    raiz.geometry("950x700")
    
    raiz.config(bg="deepskyblue4")
       
    #menubar = Menu(raiz)
    #raiz.config(menu=menubar)  # Lo asignamos a la base
    
    #helpmenu = Menu(menubar)

    #menubar.add_cascade(label="Ayuda", menu=helpmenu)
    
    imagen=PhotoImage(file="fondo.gif")
    Label(raiz,image=imagen).pack()
    
    label = Label(raiz,text="Menú de métodos numéricos")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",40)) #tipo de letra
    label.place(x=75,y=15)
    
    label = Label(raiz,text="Aquí podrás encontrar una diversa cantidad de programas")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",15)) #tipo de letra
    label.place(x=135,y=75)
    
    label = Label(raiz,text=" que te permitan resolver problemas con distintas metodologías.")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",15)) #tipo de letra
    label.place(x=75,y=100)
    
    bis=Button(raiz,text="Conoce más sobre los métodos aquí", width=30, command=conoce)
    bis.place(x=75, y=135)
    
    #METODOS DE RAICES
    label = Label(raiz,text=" Métodos para encontrar raíces de funciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=430,y=170)
    value=0
    
    bis=Button(raiz,text="Bisección", width=7, command=biseccion_button)
    bis.place(x=400, y=205)
    
    f_pos=Button(raiz,text="Falsa Posición", width=10, command=falsa_pos_button)
    f_pos.place(x=470, y=205)
    
    nw_r=Button(raiz,text="Newton-Rhapson", width=13, command=newton_raphson_button)
    nw_r.place(x=560, y=205)
    
    nw_r=Button(raiz,text="Secante",width=7, command=secante_button)
    nw_r.place(x=670, y=205)
    
    bairstow=Button(raiz,text="Bairstow",width=7, command=bairstrow_button)
    bairstow.place(x=740, y=205)
    
    S_M=Button(raiz,text="Secante-modificada",width=15, command=secante_modificada_button)
    S_M.place(x=810, y=205)
    
    #METODOS DE ECUACIONES LINEALES
    label = Label(raiz,text="Sistemas de ecuaciones lineales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=500,y=240)
    
    cramer=Button(raiz,text="Cramer",width=7, command=cramer_button)
    cramer.place(x=400, y=275)
    
    gauss=Button(raiz,text="Gauss",width=7, command=gauss_button)
    gauss.place(x=470, y=275)
    
    gauss_jordan=Button(raiz,text="Gauss-Jordan",width=12, command=gauss_jordan_button)
    gauss_jordan.place(x=540, y=275)

    nw_r=Button(raiz,text="Descomposición LU",width=15, command=LU_button)
    nw_r.place(x=645, y=275)
    
    G_S=Button(raiz,text="Gauss-Seidel",width=12, command=gauss_seidel_button)
    G_S.place(x=770, y=275)
 
    #METODOS PARA AJUSTAR CURVAS POR MEDIO DE REGRESION
    label = Label(raiz,text="Ajuste de curvas por regresión")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=500,y=310)
    
    label = Label(raiz,text="Regresiones lineales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=400,y=340)
    
    mc=Button(raiz,text="Mínimos cuadrados", width=15, command=minimo_cuadrado_button )
    mc.place(x=400, y=365)
  
    vv=Button(raiz,text="Varias variables",width=12, command=regresion_varias_button)
    vv.place(x=525, y=365)
    
    label = Label(raiz,text="Regresión polinomial")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=670,y=340)

    rp=Button(raiz,text="Polinomial",width=9, command=regresion_polinomial_button)
    rp.place(x=670, y=365)

    label = Label(raiz,text="Linearizaciones")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue4", #fondo para todas la GUI
                 font=("Courier",11)) #tipo de letra
    label.place(x=400,y=395)
    
    ln=Button(raiz,text="Logaritmo natural", width=17, command=linearizacion_ln_button)
    ln.place(x=400, y=420)
     
    l10=Button(raiz,text="Logaritmo base 10", width=17, command=linearizacion_log_button)
    l10.place(x=550, y=420)
       
    #METODOS PARA AJUSTAR CURVAS POR MEDIO DE interpolación
    label = Label(raiz,text="Ajuste de curvas por interpolación")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=480,y=455)
    
    n_w=Button(raiz,text="Newton", width=7, command=interpolacion_newton_button)
    n_w.place(x=400, y=490)
    
    lagrange=Button(raiz,text="Lagrange", width=8, command=interpolacion_lagrange_button)
    lagrange.place(x=470, y=490)
    
    inversa=Button(raiz,text="Inversa",width=8, command=interpolacion_inversa_button)
    inversa.place(x=550, y=490)
    
    #METODOS PARA INTEGRACION NUMERICA
    label = Label(raiz,text="Integración numérica")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=540,y=525)
    
    n_w=Button(raiz,text="Segmentos iguales", width=15, command=integracion_iguales_button)
    n_w.place(x=400, y=560)
    
    lagrange=Button(raiz,text="Segmentos desiguales", width=20, command=integracion_desiguales_button)
    lagrange.place(x=530, y=560)
    
    #METODOS ECUACIONES DIFERENCIALES
    label = Label(raiz,text="Solución de Ecuaciones Diferenciales")
    label.pack(anchor=CENTER)
    label.config(fg="snow", #color de letra
                 bg="deepskyblue2", #fondo para todas la GUI
                 font=("Courier",12)) #tipo de letra
    label.place(x=470,y=600)
    
    euler=Button(raiz,text="Euler", width=7, command=euler_button)
    euler.place(x=400, y=635)
    
    rk2=Button(raiz,text="Runge-Kutta segundo orden", width=23, command=rk2_button)
    rk2.place(x=470, y=635)
    
    rk4=Button(raiz,text="Runge-Kutta cuarto orden", width=20, command=rk4_button)
    rk4.place(x=650, y=635)
    
    destroy=Button(raiz,text="Salir", width=7, command=raiz.destroy)
    destroy.place(x=75, y=635)
    
    raiz.mainloop()
    