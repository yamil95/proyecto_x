import functools
from typing import Any

class exception_custom (Exception):
    
    def __init__ (self,*valores):
        
        self.nombre = valores[0][0]
        self.hora = valores[0][1]
    
    def mostrar_valores (self) -> str:
        return (f"se produjo la exception con nombre {self.nombre} a la hora: {self.hora}")

class decorador:
    
    def __init__ (self , *valores,**diccionario):
        self.parametro = valores
        self.diccionarios = diccionario
        self.datos = 0
    
    def __call__(self, func) -> Any:
        
        functools.update_wrapper(self,func)
        def wrapper (*args, **kwargs):
            print (*args)
            print (*kwargs)
            print ("el nombre de la funcion  es :", func.__name__, "va ser decorada con  :", self.parametro)
            return func(*args, **kwargs) + self.parametro
        return wrapper
 
        
            
        
diccionario ={"valor":1,"valor_2":2}   
lista = [1,2,3]
diccionario_2 ={"valor":4,"valor_2":6 }
lista_2= [10,20,30]

@decorador(lista_2,diccionario_2)
def suma (lista,diccionario):
     
    return (lista[0]*diccionario["valor_2"])
    



if __name__ == '__main__':
   
   try:
       if lista[0] ==0:
           print ( suma (lista,diccionario))
        
       else:
           raise exception_custom(["exception_valor_1","21:30"])

   except exception_custom as e:
       
       print (e.mostrar_valores())