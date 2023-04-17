from dictionary import *

"""Ejercicio 4"""

def IsPermutation(S1,S2):
    #cuidado que mayusculas sera otra cadena distinta
    #dado dos cadenas vemos si una es permutacion de la otra
    if S1 == S2 or len(S1) != len(S2): return False #no pueden ser permutaciones
    else:
        D=CreateHashTable(len(S1))
        for letter in S1:
            Hindex=ord(letter)-ord("A")#Func hash uno a uno
            insert(D,Hindex,letter)
        printHashTable(D)
        for letter in S2:
            Hindex=ord(letter)-ord("A")#Func hash uno a uno 
            Cond=search(D,Hindex)
            if Cond==None: return False
    return True


"""Ejercicio 5"""

def Isunique(List):
    #verifica que los elementos de la lista son unicos
    D=CreateHashTable(len(List))
    for i in range(0,len(List)):
        #busco la key y veo si su value esta y coincide
        HashIndex=F_hash_Div(List[i],len(D))
        Aux=search(D,HashIndex)
        insert(D,HashIndex,List[i])
        if Aux is not None and Aux==List[i]:
            return False
    return True



"""Ejercicio 6"""

def C_PostalesHash(key,M):
    #una funcion de hash para los codigos cddddccc c=carc d=int
    return ((ord(key[0])*10**8+ord(key[1])*10**7+ord(key[2])*10**6+ord(key[3])*10**5+ord(key[4])*10**4+ord(key[5])*10**3+ord(key[6])*10**2+ord(key[7])*10) % M)


"""Ejercicio 7"""

def CompressedString(string):
    #comprime cadenas con el numero de veces del caracter repetido
    #no es necesario un hash table
    cont=1
    Sresult=""
    #recorro y cuando el sig es otro reinicio el contador
    for i in range(0,len(string)):
        #final de cadena
        if i+1 is len(string):
            Sresult+=string[i]
            Sresult+=str(cont)
            return Sresult
        if string[i+1] is not string[i]:
            Sresult+=string[i]
            Sresult+=str(cont)
            cont=1
        else:
            cont+=1


"""Ejercicio 8"""

def FirstOccurrence(S,P):
    #muestra el indice de la primera ocurrencia de p en s
    if S==P: return 0
    if len(S)<len(P): return False
    for i in range(0,len(S)):
        print(S[i:i+len(P)])
        if S[i:i+len(P)]==P:
            return True
    return False

        



"""Ejercicio 9"""

def subset(S,T):
    #verifica si S es subconjunto de T
    #insertar y luego en otro bucle poner search y no es o de n^2 porque no recorres toda la lista
    D=CreateHashTable(len(T))
    for each in T:
        insert(D,each,each)
    printHashTable(D)
    for each in S:
        if search(D,each) is None:
            return False
    return True
