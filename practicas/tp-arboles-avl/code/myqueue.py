from linkedlist import *

def enqueue(Q,element):
  #Agrega un elemento al comienzo
  add(Q,element)
def dequeue(Q):
  #extrae el último elemento de la cola
  cont=length(Q)
  current=Q.head
  if cont!=0 and cont!=1:
    for i in range(0,cont):
      if i==cont-2:
        element=current.nextNode.value
        current.nextNode=None
        return element
      current=current.nextNode
  elif cont==1: #un elemento en la lista
    element=Q.head.value
    Q.head=None
    return element
  else:
    return None

