
import matplotlib
import matplotlib.pyplot as plt


def biseccion():
    #plt.plot([[-10,-40],[-9,-35],[-8,30],[-7,-25],[-6,-20]])
    #plt.plot([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0])
    #plt.plot([-40,-35,-30,-25,-20,-15,-10,-5,0,5,10])
    #x = [1,2,3,4,5,6,7,8,9,10,11]
    #y = [133,292,283,283,302,400,505,608,667,783,785]
    
    x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
    y = [-40,-35,-30,-25,-20,-15,-10,-5,0,5,10]
    
    
    
    #plt.plot([63.9636,65.718181])
    
    dibujo = plt.plot([5,10])
    dibujo = plt.scatter(x,y)
    dibujo = plt.ylabel("baba")
    dibujo = plt.show()

if __name__ == "__main__":
    
    biseccion()
