import matplotlib.pyplot as plt

class poly:
    def __init__(self, n, coefs):
        self.n = n
        self.coefs = [0] * (n +1) 
        for i in range(len(coefs)):  
                self.coefs[i] = coefs[i]  


    def get_expression(self):
        #Devuelve el polinomio en forma de polinomio dado en lista 
        vacio = ""
        for i, c in enumerate(self.coefs):
            if c != 0:
                signo = "-" if c < 0 else "+" if i != 0 else ""
                c = abs(c)
                grado = f"x^{i}" if i > 1 else "x" if i == 1 else ""
                if c == 1 and i != 0:
                    terminado = f"{signo}{grado}"
                elif c == -1 and i == 0:
                    terminado = "-x"
                else:
                    terminado = f"{signo}{c}{grado}" if i != 0 else f"{signo}{c}"
                vacio += terminado
        return( vacio.lstrip("+ ") )
    
        
    def __call__ (self, x):
        #Busca el valor de Y en el polinomio con X en valor de "x"
        y = 0
        for i in range(self.n):
            y += self.coefs[i] * (x ** i)
        return y
    
    def poly_plt(self, a, b, **kwargs):
        #Hace un plot desde la libreria matplotlib de el polinomio
        valores_x = []
        valores_y = []
        n_points = kwargs.get("n_points", 50)

        delta = (b - a) / (n_points)
        
        for i in range(n_points):
            x = a + i * delta
            valores_x.append(x)

   
        for x in valores_x:
            valores_y.append(self(x))

        plt.plot(valores_x, valores_y, **kwargs)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(self.get_expression())
        plt.show()
        
    def __add__ (self, suma):
        #Suma polinomio + suma
        if isinstance (suma, list):
            if len(suma) > len(self.coefs) or len(suma) == len(self.coefs):
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(suma), len(self.coefs))
                
                for i in range(len(self.coefs)):  
                        nuevo_coefs[i] = suma[i] + self.coefs[i]
                        
                for a in range(len(self.coefs) , len(suma)):
                   nuevo_coefs[a] = suma[a]
                
            else:
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(suma), len(self.coefs))
                
                for i in range(len(suma)):  
                        nuevo_coefs[i] = self.coefs[i] + suma[i]
                        
                for a in range(len(suma) , len(self.coefs)):
                   nuevo_coefs[a] = self.coefs[a]
           
        elif isinstance(suma, int or float):
            sumav2 = []
            sumav2.append(suma)
            nuevo_coefs = self.coefs.copy()
            nuevo_coefs[0] += sumav2[0]
        
        return(nuevo_coefs)
    
    def __sub__ (self, resta):
        # La funcion resta tomando el polinomio - resta
        if isinstance (resta, list):
            if len(resta) > len(self.coefs) or len(resta) == len(self.coefs):
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(resta), len(self.coefs))
                
                for i in range(len(self.coefs)):  
                        nuevo_coefs[i] = resta[i] - self.coefs[i]
                        
                for a in range(len(self.coefs) , len(resta)):
                   nuevo_coefs[a] = resta[a]
                
            else:
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(resta), len(self.coefs))
                
                for i in range(len(resta)):  
                        nuevo_coefs[i] = self.coefs[i] - resta[i]
                        
                for a in range(len(resta) , len(self.coefs)):
                   nuevo_coefs[a] = self.coefs[a]
           
        elif isinstance(resta, int or float):
            restav2 = []
            restav2.append(resta)
            nuevo_coefs = self.coefs.copy()
            nuevo_coefs[0] -= restav2[0]
        
        return(nuevo_coefs)
    
    def __mul__(self, multi):
        #Multiplica polinomio * div
        if isinstance (multi, list):
            if len(multi) > len(self.coefs) or len(multi) == len(self.coefs):
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(multi), len(self.coefs))
                
                for i in range(len(self.coefs)):  
                        nuevo_coefs[i] = multi[i] * self.coefs[i]
                        
                for a in range(len(self.coefs) , len(multi)):
                   nuevo_coefs[a] = multi[a]
                
            else:
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(multi), len(self.coefs))
                
                for i in range(len(multi)):  
                        nuevo_coefs[i] = self.coefs[i] * multi[i]
                        
                for a in range(len(multi) , len(self.coefs)):
                   nuevo_coefs[a] = self.coefs[a]
           
        elif isinstance(multi, int or float):
            multiv2 = []
            multiv2.append(multi)
            nuevo_coefs = self.coefs.copy()
            nuevo_coefs[0] *= multiv2[0]
        
        return(nuevo_coefs)
    
    def __floordiv__(self, div):
        # Divide el polinomio / div
        if isinstance (div, list):
            if len(div) > len(self.coefs) or len(div) == len(self.coefs):
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(div), len(self.coefs))
                
                for i in range(len(self.coefs)):  
                        nuevo_coefs[i] = self.coefs[i] / div[i]
                        
                for a in range(len(self.coefs) , len(div)):
                   nuevo_coefs[a] = 0
                
            else:
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(div), len(self.coefs))
                
                for i in range(len(div)):  
                        nuevo_coefs[i] = self.coefs[i] / div[i]
                        
                for a in range(len(div) , len(self.coefs)):
                   nuevo_coefs[a] = self.coefs[a]
           
        elif isinstance(div, int or float):
            divv2 = []
            divv2.append(div)
            nuevo_coefs = self.coefs.copy()
            nuevo_coefs[0] /= divv2[0]
        
        return(nuevo_coefs)
    def __mod__ (self, resto):
        #Saca el resto de la division entre polinomio y "resto"
        if isinstance (resto, list):
            if len(resto) > len(self.coefs) or len(resto) == len(self.coefs):
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(resto), len(self.coefs))
                
                for i in range(len(self.coefs)):  
                        nuevo_coefs[i] = self.coefs[i] % resto[i]
                        
                for a in range(len(self.coefs) , len(resto)):
                   nuevo_coefs[a] = 0
                
            else:
                nuevo_coefs = []
                nuevo_coefs = [0] * max(len(resto), len(self.coefs))
                
                for i in range(len(resto)):  
                        nuevo_coefs[i] = self.coefs[i] % resto[i]
                        
                for a in range(len(resto) , len(self.coefs)):
                   nuevo_coefs[a] = self.coefs[a]
           
        elif isinstance(resto, int or float):
            restov2 = []
            restov2.append(resto)
            nuevo_coefs = self.coefs.copy()
            nuevo_coefs[0] %= restov2[0]
        return(nuevo_coefs)
       

        
if __name__ == "__main__":
    polinomio = poly(2, [8,2,1])
    expresion = polinomio.get_expression()
    
    valor = polinomio(3)
    grafico = polinomio.poly_plt(-20, 20, color = "red")
    
    sumatoria = polinomio + 3
    sub = polinomio - [1,1]
    mult = polinomio * 2
    divi = polinomio // [2,1]
    restos = polinomio % [2,1,3,2]

