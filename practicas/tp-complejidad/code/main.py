from math import trunc

#Ejercicio 5
def ContieneSuma (A,n):
    """recibe una lista de enteros A y un entero n y devuelve True
     si existen en A un par de elementos que sumados den n."""
    #comparo cada elemento con los demas y sumo
    success=False
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            suma=0
            if success==False:
                if i is not j :
                    suma=A[i]+A[j]
                if suma==n:
                    success=True
    return success

#Ejercicio 4
def OrdListaMenores(L):
    """ordena una lista donde siempre el elemento del medio contiene antes que él
    la mitad de los elementos menores que él."""
    if len(L)<=2:
        #si la lista es menor a 2 elementos no hay nada de que hacer
        return L
    else:
        #creo dos listas aux
        ListaResult=[]
        ListaAux=[]
        #defino los casos para listas de tamaño impar y par
        if len(L)%2==0:#si es par
            Pmedio=trunc(len(L)/2)-1 
        else:#si es impar
            Pmedio=trunc(len(L)/2)
        Nmedio=L[Pmedio]
        Nmenores=cantidadDeMenores(L,Nmedio)

        #a continuacion dos casos especiales
        if Nmenores is 0:
            #si no tiene menores por ejemplo en una lista con un 0
            return L
        MitadMenores=round(Nmenores/2)
        if MitadMenores is 0:
            #en este caso la variable al redondear queda en 0 pero no significa que no tenga menores asiq pongo 1
            MitadMenores=1
        
        #en este bloque voy a insertar en otra lista los elemtos correspondientes
        contador=0
        #en este pongo el numero de menores que corresponda
        #primero la mitad de los menores en una lista y los demas sin el del medio en otra
        for i in range(0,len(L)):
            if L[i]<Nmedio:
                contador+=1
                if contador<=(MitadMenores):
                    ListaResult.append(L[i])
                else:
                    ListaAux.append(L[i])
            elif L[i]>Nmedio:
                ListaAux.append(L[i])
        #luego relleno la primera con los mayores 
        contador=0
        for i in range(0,len(L)):
            if L[i]>Nmedio:
                contador+=1
                if contador<=(MitadMenores):
                    ListaResult.append(L[i])
                    ListaAux.remove(L[i])
        #inserto el del medio y junto las listas
        ListaResult.insert(Pmedio,Nmedio)
        ListaResult=ListaResult+ListaAux
    return ListaResult                 


def cantidadDeMenores(L,Num):
    #da la cantidad de menores que el numero en la lista
    menores=0
    for i in range (0,len(L)):
        if L[i]<Num:
            menores+=1
    return menores


    

#Ejercicio 5

entero=8
Lista1=[7,3,2,8,5,4,1,6,10,9]
Lista2=[7,6,10,9,5,3,2,1,4,8]


print("Lista de enteros ",Lista1)
print("Numero entero: ",entero)
Cond=ContieneSuma (Lista1,entero)
print(Cond)

#Ejercicio 4

aux=OrdListaMenores(Lista1)
print(aux)