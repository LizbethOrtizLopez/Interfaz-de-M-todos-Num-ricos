#Lizbeth Ortiz López  A00227346
#Marlene Rodríguez Harms A00227347
#Erick Alfonso Montan Lopez A01379766
#Programa resuelve_lu

import os
import math
import tkinter.filedialog
from tkinter import messagebox
from Descomposicion_LU import resuelve_lu

def DESCOMPOSELU(a,n,tol,name):
    a,o,error = DESCOMPOSE(a,n,tol)
    if error == False :
        f = open(name+'.l.txt','w')
        for i in range (n):
            for j in range (n):
                f.write(str(a[i][j])+" ")
            f.write("\n")
        f.close
        
        f1 = open(name+'.u.txt','w')
        for i in range (n):
            f1.write(str(o[i])+" ")
        f1.close
        
        messagebox.showinfo("Descomposición","Matriz descompuesta con éxito")
        
    else :
        messagebox.showinfo("ERROR FATAL","No se puede descomponer la matriz")
        raise Exception("No se puede descomponer la matriz")

def DESCOMPOSE(a,n,tol):
    try:
        o = []
        s = []
        for i in range (n):
            o.append(i)
            s.append(0)
        for i in range (n):
            s[i] = math.fabs(a[i][0])
            for j in range (1,n):
                dummy = math.fabs(a[i][j])
                if dummy > s[i] :
                    s[i] = dummy
        for k in range (n-1):
            o,s = PIVOT(a,o,s,n,k)
            if math.fabs(a[o[k]][k] / s[o[k]]) < tol :
                return a,o,True
            for i in range (k+1 , n):
                factor = a[o[i]][k] / a[o[k]][k]
                a[o[i]][k] = factor
                for j in range(k+1,n):
                    a[o[i]][j] = a[o[i]][j] - factor * a[o[k]][j]

        if math.fabs(a[o[k]][k] / s[o[k]]) < tol :
            return a,o,True
        return a,o,False
    
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo"),e
            
def PIVOT(a,o,s,n,k):
    
    try:
        p = k
        big = math.fabs(a[o[k]][k] / s[o[k]])
        for i in range (k + 1 ,n):
            dummy = math.fabs(a[o[i]][k] / s[o[i]])
            if dummy > big :
                big = dummy
                p = i
        dummy = o[p]
        o[p] = o[k]
        o[k] = dummy
        
        return o,s       
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque alguno de los datos es erroneo"),e
    
def leerArchivo(file,size):
    try:
        f = open(file, "r")
        matrix = []
        for i in range(size):
            matrix.append([])
            row = f.readline().split()
            for j in range(size):
                matrix[i].append(float(row[j]))
        f.close()
        return matrix 
    
    except ValueError as e:
        messagebox.showinfo("ERROR FATAL","Ingresaste un dato no válido, trataste de ingresar un archivo que no era de texto o dejaste vacío el campo de tamaño. Verifica tus datos"), e
    except IndexError as e:
        messagebox.showinfo("ERROR FATAL","El archivo está incompleto. Verifica tus datos."), e
  
'''
if __name__ == "__main__":
    
    #Ejemplo 1

     a =[[4,-2,-1],
         [5,1,-1],
         [1,2,-1]]
     b = [9,7,12]
     n = 3
     tol = 0.01
     
     print(DESCOMPOSELU(a,b,n,tol))

    
    print("Hola, selecciona el archivo que contenga la matriz a descomponer")
    file = tkinter.filedialog.askopenfilename()
    a, n = leerArchivo(file)
    name=""
    i=len(file)-5
    while(str(file[i])!='/'):
        name+=str(file[i])
        i-=1
    nameArchivo = name[::-1]
    DESCOMPOSELU(a,n,0.01,nameArchivo)
    
    resuelve_lu()
    
    #resuelve_lu.init(n)
''' 
   
