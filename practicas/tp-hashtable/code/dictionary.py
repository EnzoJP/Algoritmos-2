
def CreateHashTable(Dim):
    Hash=[]
    #crea un Hash de M posciones
    for i in range (0,Dim):
        L=[]
        Hash.append(L)
    return Hash
    
def insert(D,key, value):
    #inserta un elemento en la HashTable
    if D==None or len(D)==0:
        print("Please first create a HashTable with CreateHashTable(Dim) ")
    else:
        #busco la posc donde insertar
        HashIndex=F_hash_Div(key,len(D))
        Tupla=(key,value)
        #inserto por encadenamineto
        D[HashIndex].append(Tupla)
    return D

def search(D,key):
    #busca un key en un HashTable
    HashIndex=F_hash_Div(key,len(D))
    for each in D[HashIndex]:
        if each[0] is key:
            return each[1]
    return None

def delete(D,key):
    if search(D,key) is None:
        print("Not found")
        return None
    else:
        HashIndex=F_hash_Div(key,len(D))
        for i in range(0,len(D[HashIndex])):
            if D[HashIndex][i][0] is key:
                D[HashIndex].pop(i)
                return D
    





"""Funciones Hash"""

def F_hash_Div(K,M): return K % M

"""Extras"""

def printHashTable(D):
    count=0
    for each in D:
        print("[",count,"]","--->",end="")
        print(each)
        print("----")
        count+=1


