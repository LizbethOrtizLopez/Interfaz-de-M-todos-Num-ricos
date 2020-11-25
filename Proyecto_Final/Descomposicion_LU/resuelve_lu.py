#Lizbeth Ortiz López  A00227346
#Marlene Rodríguez Harms A00227347
#Erick Alfonso Montan Lopez A01379766
#Programa resuelve_lu

import os
import math
import tkinter.filedialog
from tkinter import messagebox

def leerArchivoA(file,n):
    try:
        f = open(file, "r")
        a = []
        for i in range(n):
            a.append([])
            row = f.readline().split()
            for j in range(n):
                a[i].append(float(row[j]))
        f.close()
        return a
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto. Verifica tus datos."), e
            
def leerArchivoO(file,n):
    try:
        f = open(file, "r")
        o = []
        row = f.readline().split()
        for i in range(n):
            o.append(int(row[i]))
        # Cerramos el archivo.
        f.close()
        return o
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto. Verifica tus datos."), e

def leerArchivoB(file,n):
    try:
        f = open(file, "r")
        b = []
        row = f.readline().split()
        for i in range(n):
            b.append(float(row[i]))
        # Cerramos el archivo.
        f.close()
        return b
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto. Verifica tus datos."), e

def SOLVE(a,o,m,b) :
    try:
        n = int(m)
        x = []
        for i in range (n):
            x.append(0)
        for i in range (1,n):
            accumulator = (b[o[i]])
            for j in range (i):
                accumulator = accumulator - a[o[i]][j] * b[o[j]]
            b[o[i]] = accumulator
        x[n-1] = b[o[n-1]] / a[o[n-1]][n-1]
        for i in range (n-1 , -1, -1):
            accumulator = 0
            for j in range (i+1,n):
                accumulator = accumulator + a[o[i]][j] * x[j]
            x[i] = (b[o[i]] - accumulator) / a[o[i]][i]
        return x
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo"),e
        
   
