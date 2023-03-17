import random
class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None


def add(L,element):
  #agrega un nodo al principio de la lista
  head=L.head
  nodeFirst=Node()
  nodeFirst.value=element
  L.head=nodeFirst
  nodeFirst.nextNode=head

def search(L,element):
  #Busca un elemento de la lista
  current=L.head
  cont=0
  while current!=None:
    if current.value==element:
      return cont
    current=current.nextNode
    cont+=1
  return None

def insert(L,element,position):
  #Inserta un elemento en una posición de la lista
  current=L.head
  cont=0
  while current!=None:
    current=current.nextNode
    cont+=1
  if position>cont:
    return None
  else:
    if position!=0:
      nodeInsert=Node()
      nodeInsert.value=element
      current=L.head
      for i in range (0,cont):
        if i==position-1:
          nodeInsert.nextNode=current.nextNode
          current.nextNode=nodeInsert
        current=current.nextNode
      return position
    else:
      add(L,element)
      return position
      
def delete(L,element):
  #Elimina un elemento de la lista
  Encontrado=search(L,element)
  if Encontrado==0:
    L.head=L.head.nextNode
    return Encontrado
  if Encontrado != None:
    current=L.head
    for i in range(0,Encontrado):
      if i==Encontrado-1:
        current.nextNode=current.nextNode.nextNode
        return Encontrado
      current=current.nextNode
  else:
    return None  

  
def length(L):
  #Calcula el número de elementos de la lista
  current=L.head
  cont=0
  while current!=None:
    cont+=1
    current=current.nextNode
  return cont
def access(L,position):
  #Permite acceder a un elemento de la lista
  current=L.head
  cont=0
  while current!=None:
    if cont==position:
      if current.value!=None:
        return current.value
      else:
        return None  
    cont+=1
    current=current.nextNode
def update(L,element,position):
  #Permite cambiar el valor de un elemento de la lista
  current=L.head
  cont=0
  while current!=None:
    if cont==position:
      if current.value!=None:
        current.value=element
        return cont 
      else:
        return None  
    cont+=1
    current=current.nextNode
def printList(L):
  #imprime la lista
  current=L.head
  print("[",end="")
  for i in range(0,length(L)):
    print(current.value,end=" ")
    current=current.nextNode
  print("]",end="")
  print("")
  
def move(L,position_orig,position_dest):
  aux=access(L,position_orig)
  if position_orig==0:
    L.head=L.head.nextNode
    return
  if position_orig != None:
    current=L.head
    for i in range(0,position_orig):
      if i==position_orig-1:
        if current.nextNode.nextNode is not None:
          current.nextNode=current.nextNode.nextNode
        else:
          current.nextNode=None
      current=current.nextNode
  else:
    return None  
  insert(L,aux,position_dest)


def revertL(L):
  #da vuelta la lista
  newL = LinkedList()
  len = length(L)
  current = L.head

  for i in range(len):
    len -= 1
    add(newL, current.value)
    current = current.nextNode
  return newL

def listAleatoria(length, rnd_in, rnd_fin):
  #lista con numeros random
  L = LinkedList()
  for i in range(length):
    add(L, random.randint(rnd_in, rnd_fin))
  return L

def previousNode(L, position):
  #nodo previo
  count = 0
  current = L.head
  while count < position-1:
      current = current.nextNode
      count += 1
  return current


def deletePosition(L,position):
  element=access(L,position)
  current=L.head
  if (position==None):
    return None
  if (position==0):
    L.head=current.nextNode
  else:
    for i in range (0,position-1):
      current=current.nextNode
    if current.nextNode.nextNode is not None:
    	current.nextNode=current.nextNode.nextNode
    else:
      current.nextNode=None
  return element