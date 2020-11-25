from tkinter import messagebox
class PolinomioClass:
    
    def __init__(self,coeficientes=[0]):
        self.coef = coeficientes
        self.grado = len(coeficientes) - 1
    
    def getGrado(self):
        return self.grado
    
    def getCoeficientes(self):
        return self.coef
    
    def getCoeficiente(self,idx):
        return self.coef[idx]
    
    def multiplicaConstante(self,constante):
        #warning: modificando campo fuera de constructor o set.
        return PolinomioClass([x * constante for x in self.coef])
        
    def aumentaCoeficiente(self,final):
        if final:
            self.coef.append(0)
        else:
            self.coef.insert(0,0)
        self.grado = self.grado + 1
    
    def sumaPolinomio(self,pol2):
        arr=[]
        for i in range (self.getGrado()+1):
            arr.append(self.coef[i]+pol2.coef[i])
        return PolinomioClass(arr);
    
    def multiplicaLineal(self,pol_lineal):
        nuevo_grado = self.getGrado() + 1
        factor = pol_lineal.getCoeficiente(0)
        op1 = self.multiplicaConstante(factor)
        op1.aumentaCoeficiente(True)
        factor = pol_lineal.getCoeficiente(1)
        op2 = self.multiplicaConstante(factor)
        op2.aumentaCoeficiente(False)
        suma = op1.sumaPolinomio(op2)
        self.coef = suma.getCoeficientes()
        self.grado = nuevo_grado
        return self
        
def GET_LINEAL(n):
    return PolinomioClass([1,-n])

def GET_LI(puntos,i):
    try:
        n = len(puntos)
        xi= puntos[i][0]
        li = PolinomioClass([1])  
        for j in range (0,i):
            xj = puntos[j][0]
            lineal = GET_LINEAL(xj)
            factor = 1 / (xi - xj)
            lineal = lineal.multiplicaConstante(factor)
            li = li.multiplicaLineal(lineal)
        for j in range (i+1,n):
            xj = puntos[j][0]
            lineal = GET_LINEAL(xj)
            factor = 1 / (xi - xj)
            lineal = lineal.multiplicaConstante(factor)
            li = li.multiplicaLineal(lineal)
        return li
    except ZeroDivisionError as e:
        messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e

def LAGRANGE(puntos):
    n = len(puntos)
    print(n);
    results = []
    for i in range (n):
        results.append(0.0)
        
    res = PolinomioClass(results)

    for i in range (n):
        results.append(0.0)

    for i in range (n):
        pol = GET_LI(puntos,i)
        pol = pol.multiplicaConstante(puntos[i][1])
        res = res.sumaPolinomio(pol)
    
    final = []
    for i in range (n):
        final.append(res.getCoeficiente(i))
    
    return final

