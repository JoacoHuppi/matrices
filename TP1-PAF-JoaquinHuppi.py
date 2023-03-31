class matrices:
    def __init__(self, lista_elems,r,c,byrow):
        """
        La clase "matrices",con sus objetos:
                "lista_elems": Lista plana de una matriz, acepta una lista de numeros (list).
                "r": Cantidad de filas que contiene la matriz, acepta un numero (int).
                "c": Cantidad de columnas que contiene la matriz, acepta un numero (int).
                "byrow": Como se lee la lista, para crear la matriz. True o False (bool)
        ---
        Returns:
            -
        """
        self.lista_elems = lista_elems
        self.r = r
        self.c = c
        self.byrow = byrow
        
    def muestra_matriz(self):
        """
        Función que utiliza: 
            La clase "matrices", con sus objetos:
                    "lista_elems": Lista plana de una matriz, acepta una lista de numeros (list).
                    "r": Cantidad de filas que contiene la matriz, acepta un numero (int).
                    "c": Cantidad de columnas que contiene la matriz, acepta un numero (int).
                    "byrow": Como se lee la lista, para crear la matriz. True o False (bool)
        ----
        Returns: 
                Un print, en forma de matriz "real". De la matriz plana ingresada, 
                leida o por filas o por columnas.
        """
        if self.byrow == True:
            contador = 0
            for number in range(self.c):
                print(self.lista_elems[contador: contador + self.r])
                contador += self.r
                
        elif self.byrow == False:
            matriz = [self.lista_elems[i::self.c] for i in range(self.c)]
            for fila in (matriz):
                print(fila)
    
    def get_pos(self,j,k):
        """

        Parameters
        ----------
        j : Un número tipo INT
            La posición "x", de un elemento en la matriz.
        k : Un numero tipo INT
            La posición "y", de un elemento en la matriz.
            

        Returns
        -------
        Posicion: Un numero tipo INT
                  La posición de ese elemento en la matriz, en la lista.

        """
        if self.byrow == True:
           posicion = (k-1)*(self.r) + j
     
           
        elif self.byrow == False:
            posicion = (j-1)*(self.c) + k
           
        return (posicion)
    
    def get_rows(self, j):
      """
        

        Parameters
        ----------
        j : Un número tipo INT
            Una fila, que se quiera obtener de la matriz

        Returns
        -------
        Devuelve la fila pedida por "j".

        """
      self.j = j
      if self.byrow == True:
          return(self.lista_elems[(j-1)* self.r : (j-1)* self.r + self.r])
      elif self.byrow == False:
          return(self.lista_elems[(j-1) ::self.c])
    
    def get_col(self,k):
      """
        

        Parameters
        ----------
        k : Un número tipo int
            Una columna, que se quiera obtener de la raiz.

        Returns
        -------
        Devuelve la columna pedida por "k".

        """
      self.k = k
      if self.byrow == True:
          return(self.lista_elems[(k-1)::self.r])
          
      elif self.byrow == False:
          return(self.lista_elems[(k-1) * self.c: (k-1) * self.c +self.c])
      
    def switch(self):
           """
        

        Returns
        -------
        new_list : Una lista (list)
            Una lista, que si antes se leia por filas, ahora leyendolas por columnas,
            obtendría la misma matriz. Y si antes se leia por columnas, ahora por filas se
            obtendría la misma matriz.

        """
           elems = self.lista_elems
           new_list = []
           if self.byrow == True:
               for fila in range(self.r):
                   for columna in range (self.c):
                       new_list.append (elems[columna * self.r + fila])
           if self.byrow == False:
               for columna in range(self.c):
                   for fila in range (self.r):
                       new_list.append (elems[fila * self.c + columna])
           return matrices(new_list,self.r, self.c, self.byrow)
       
    def get_elems(self,ñ):
        """

        Parameters
        ----------
        ñ : Un número de tipo (bool)
            El primer número ingresado antes de la ","sería la cordenada "x".
            El segundo número después de la ",", sería la cordenada "y".
            

        Returns
        -------
        Se obtiene dadas las cordenadas "x" e "y". El elemento en cuestión de la matriz.

        """
        self.ñ = ñ
        position = matriz.get_pos(ñ[0], ñ[1])
        return(self.lista_elems[position -1])
    
    
    def del_rows(self, j):
        """
        

        Parameters
        ----------
        j : Un número de tipo (int)
            La fila a eliminar de la matriz

        Returns
        -------
        lista-nueva: Una lista tipo (list)
                     La matriz, sin la fila pedida a eliminar

        """
        self.j = j
        
        if self.byrow == True:
            lista_nueva = self.lista_elems.copy()
            del(lista_nueva[(j-1)* self.r : (j-1)* self.r + self.r])
    
        elif self.byrow == False:
            lista_nueva = self.lista_elems
            del(lista_nueva[(j-1):: self.r])
            
        return(lista_nueva)
        
    
            
    def del_cols(self, k):
        """
        

        
        Parameters
        ----------
        k : Un número de tipo (int)
            La columna a eliminar de la matriz

        Returns
        -------
        lista-nueva: Una lista tipo (list)
                     La matriz, sin la columna pedida a eliminar

        """
        self.k = k
        lista_nueva = []
        if self.byrow == True:
            lista_nueva = self.lista_elems.copy()
            del(lista_nueva[(k-1)::self.r])
        
        elif self.byrow == False:
            lista_nueva = self.lista_elems
            del(lista_nueva[self.c * (k-1): (k-1) * self.c +self.c])   
        return(lista_nueva)
    
    def swap_rows(self,q,x):
       """
        

        Parameters
        ----------
        q : Un número de tipo (int)
            La primera fila que el usuario desea cambiar por la otra
        x : Un número de tipo (int)
            La segunda fila que el usuario desea cambiar.

        Returns
        -------
        listanueva = Lista de tipo (list)
                     Devuelve una lista con la matriz y las filas cambiadas.
                     

        """
     
       listanueva = self.lista_elems.copy()
       if self.byrow == True:
           for n in range (self.c):
               listanueva[(q-1)*self.c + n] = self.lista_elems[(x-1)*self.c + n]
               listanueva[(x-1)*self.c + n] = self.lista_elems[(q-1)*self.c + n]
       if self.byrow == False: 
           for n in range (self.r):  
               listanueva[n*self.c + (q-1)] = self.lista_elems[n*self.c + (x-1)]
               listanueva[n*self.c + (x-1)] = self.lista_elems[n*self.c + (q-1)]
               
       return( listanueva )
       
    def swap_cols (self,l,m):
        """
        

        l : Un número de tipo (int)
            La primera columna que el usuario desea cambiar por la otra
        m : Un número de tipo (int)
            La segunda columna que el usuario desea cambiar.

        Returns
        -------
        listanueva = Lista de tipo (list)
                     Devuelve una lista con la matriz y las columnas cambiadas.
                     

        """
        elems = self.lista_elems
        nuevascols = self.lista_elems.copy()  
        
        if self.byrow == True:
            for n in range (self.c):
               c1 = n * self.r + (l-1)
               c2 = n * self.r + (m-1)
               nuevascols[c1] = elems[c2]
               nuevascols[c2] = elems[c1]
        if self.byrow == False:
            for n in range(self.r):
               c1 = (l-1)* self.c + n
               c2 = (m-1) * self.c + n
               nuevascols[c1], nuevascols[c2] = elems[c2], elems[c1]

        return(nuevascols)
    
    def scale_row(self, j,x):
        """
        Parameters
        ----------
        j : Un número de tipo (int)
            La fila que se desea multiplicar
        x : Un número de tipo (int)
            El número por el cual se va a multiplicar la fila

        Returns
        -------
        m2 = Una lista de tipo (list)
             La matriz, con la fila multiplicada por "x"

        """
        
        m1 = matriz.get_rows(j)
        nuevalista= []
        
        for n in m1:
            nuevalista.append(n * x)
        
        m2 = matriz.del_rows(j)
        m2.insert((j-1)*self.r,nuevalista)
    
        return(m2)
    
    
    def scale_col(self, k,y):
       """
        

       Parameters
       ----------
       k : Un número de tipo (int)
           La columna que se desea multiplicar
       y : Un número de tipo (int)
           El número por el cual se va a multiplicar la columna

       Returns
       -------
       nuevalista = Una lista de tipo (list)
            La matriz, con la fila multiplicada por "y"

        """
       elems = self.lista_elems
       nuevalista = []
       if self.byrow == True:
           for n in range (len(elems)):
               if n % self.c == k-1:
                   nuevalista.append(elems[n]*y)
               else: 
                   nuevalista.append(elems[n])
           return nuevalista
       if self.byrow == False:
           for i in range(self.r):
               for x in range(self.c):
                   pos = x*self.r + i
                   if x == k-1:
                       nuevalista.append(elems[pos] * y)
                   else:
                       nuevalista.append(elems[pos])

       return nuevalista
   
    def transpose(self):
        """
        

        Returns
        -------
        transpuesta : Una lista de tipo (list)
            Una lista con la matriz transpuesta

        """
        
        listtranspuesta = []
        if self.byrow == True:
            for x in range(self.r):
                for i in range(self.c):
                    listtranspuesta.append(self.lista_elems[i * self.r + x])
        if self.byrow == False:
            for x in range(self.c):
                for i in range(self.r):
                    listtranspuesta.append(self.lista_elems[x* self.c + i])
    
        return listtranspuesta 
    
    def flip_cols(self):
        """
        

        Returns
        -------
        flipcols : Una lista de tipo (list)
            Una lista con la matriz y todas las filas al revez

        """
        
        flipcols = []
        if self.byrow == True:
            for f in range(self.c):
                fila = self.lista_elems[f * self.r : (f+1) * self.r]
                flipcols.extend(fila[::-1])
        if self.byrow == False:
            for c in range(self.c):
                col = self.lista_elems [c::self.r]
                flipcols.extend(col[::-1])
        return flipcols
    
    def flip_rows(self):
        """
        Returns
        -------
        new_flist = Una lista de tipo (list)
                    Una lista con la matriz y todas las filas cambiadas

        """
    
        if self.byrow == True:
            first_row = self.lista_elems[:self.r]
            last_row = self.lista_elems[(self.c - 1) * self.r : self.c * self.r]
            new_flist = last_row + self.lista_elems[self.r:self.r * (self.c - 1)] + first_row
            
            return(new_flist)
        else:
            pass

        
matriz = matrices([1,2,3,4,5,6,7,8,9],3,3,False)

matriz.muestra_matriz()   

mswitch = matriz.switch()
mtraspose = matriz.transpose()
"""
mgetpos = matriz.get_pos(1,2)
mgetrow = matriz.get_rows(2)
mgetcol = matriz.get_col(3)
mgetelems = matriz.get_elems((2,3))



mswaprows = matriz.swap_rows(1,3)
mswapcol = matriz.swap_cols(1,3)   

---

mdelcols = matriz.del_cols(2)
mdelrows = matriz.del_rows(2)
-Por algun motivo si los dos dels de filas y columnas se usan a la vez, fallan ambos-

mscaelerow = matriz.scale_row(2, 2)
mscalecol = matriz.scale_col(2, 2)



mfcols = matriz.flip_cols()

mfrows = matriz.flip_rows()
"""

