
import math
import cmath
from tkinter import messagebox

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
       messagebox.showinfo("ERROR FATAL","No puedo encontrar una solución porque uno de los datos es erróneo."), e 

def quadratic (c, b, a):
    
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

def inicio(p,size):
    return bairstrow(p, 0.001, 1, 1, 1000, size)
    
        
        
    