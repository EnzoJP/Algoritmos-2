import binarytree
import linkedlist
from myqueue import *
class AVLTree:
	root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None
  height=None


"""Ejercicio 1"""

def rotateLeft(Tree,avlnode): 
  #realiza una rotacion hacia la izquierda en un AVl
  Nroot=avlnode.rightnode
  avlnode.rightnode=Nroot.leftnode
  if Nroot.leftnode is not None:
     Nroot.leftnode.parent=avlnode 
  Nroot.parent=avlnode.parent
  if avlnode.parent is None:
     Tree.root=Nroot
  else:
     if avlnode.parent.leftnode is avlnode:
        avlnode.parent.leftnode=Nroot
     else:
        avlnode.parent.rightnode=Nroot
  Nroot.leftnode=avlnode
  avlnode.parent=Nroot
  return Nroot

def rotateRight(Tree,avlnode):
  #realiza una rotacion hacia la derecha en un AVl
  Nroot=avlnode.leftnode
  avlnode.leftnode=Nroot.rightnode
  if Nroot.rightnode is not None:
     Nroot.rightnode.parent=avlnode 
  Nroot.parent=avlnode.parent
  if avlnode.parent is None:
     Tree.root=Nroot
  else:
     if avlnode.parent.rightnode is avlnode:
        avlnode.parent.rightnode=Nroot
     else:
        avlnode.parent.leftnode=Nroot
  Nroot.rightnode=avlnode
  avlnode.parent=Nroot
  return Nroot

"""Ejercicio 2"""

def calculateBalance(AVLTree):
  #Calcula el balance para cada nodo.
  #calculo la altura.
  Current=AVLTree.root
  CalculateHeight(AVLTree,Current)
  #calculo el balance factor
  Current=AVLTree.root
  CalculateBalanceR(AVLTree,Current)
  return AVLTree

def CalculateBalanceR(AVLTree,Current):
  if Current is not None:
      if Current.leftnode is not None and Current.rightnode is not None:
        #calculo el balance que es hoja con dos hijos
        Current.bf=((Current.leftnode.height)-(Current.rightnode.height))
      elif Current.leftnode is not None and Current.rightnode is None:
         #Nodo con un hijo caso #1
         Current.bf=((Current.height)-0)
      elif Current.rightnode is not None and Current.leftnode is None:
         #Nodo con un hijo caso #2
         Current.bf=(0-(Current.height))
      else:
         #balance de una  hoja es 0
         Current.bf=0
  if Current is not None:
      CalculateBalanceR(AVLTree,Current.leftnode)
      CalculateBalanceR(AVLTree,Current.rightnode)
  
def CalculateHeight(AVLTree,Current):
   #calcula la altura de cada nodo.
   if Current is not None:
      Current.height=maxalt(Current)-1
   if Current is not None:
      CalculateHeight(AVLTree,Current.leftnode)
      CalculateHeight(AVLTree,Current.rightnode)

def maxalt(current):
	#ve la altura maxima
   if current == None:
      return 0
   else:
      lalt = maxalt(current.leftnode)
      ralt = maxalt(current.rightnode)
      if (lalt > ralt):
         return lalt+1
      else:
         return ralt+1


"""Ejercicio 3"""

def reBalance(AVLTree):
  #Balancea un arbol para que este resulte un AVL
  #calculo los Bf de el arbol
  calculateBalance(AVLTree)
  Current=AVLTree.root
  reBalanceRecursive(AVLTree,Current)
  return AVLTree

def reBalanceRecursive(AVLTree,Current):
  #recorre los nodos en busca de hojas y busca los padres para ir balanceando
  if Current is not None:
    if Current.rightnode is None and Current.leftnode is None:
      #hoja
      CurrentAux=Current#aux para padres
      while CurrentAux is not None:
        if CurrentAux.bf > 1 or CurrentAux.bf < -1:
          #ahora necesitamos que este no sea una hoja
          if CurrentAux.rightnode is not None or CurrentAux.leftnode is not None:
            BalanceNode(AVLTree,CurrentAux)
        CurrentAux=CurrentAux.parent
  if Current is not None:
    reBalanceRecursive(AVLTree,Current.leftnode)
    reBalanceRecursive(AVLTree,Current.rightnode)
    
def BalanceNode(AVLTree,Current):
  #realiza el balance de ese subarbol que tiene a current como raiz
  if Current.bf < 0:
    if Current.rightnode.bf > 0:
      rotateRight(AVLTree,Current.rightnode)
      rotateLeft(AVLTree,Current)
    else:
      rotateLeft(AVLTree,Current)
  elif Current.bf > 0:
    if Current.leftnode.bf < 0:
      rotateLeft(AVLTree,Current.leftnode)
      rotateRight(AVLTree,Current)
    else:
      rotateRight(AVLTree,Current)
  #actualizo los Bf
  calculateBalance(AVLTree)
   

"""Ejercicio 4 y 5"""

def insert(AVLTree, element, key):
    # Inserta un elemento con una clave determinada del árbol Avl y luego rebalancea si corresponde
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    currentNode = AVLTree.root
    insertR(AVLTree, newNode, currentNode)
    #rebalanceo 
    reBalance(AVLTree)
    """no calculo de nuevo el factor de balanceo (actualizar) ya que (en mi caso)
    la funcion reBalance() calcula el Bf por si misma """


def insertR(B, newNode, currentNode):
    #funcion que inserta en un arbol binario recursivamnete tambien sirve para un AVl
    aux = False
    if B.root == None:
        B.root = newNode
        aux = True
        return newNode.key
    if aux == False:
        if currentNode.key < newNode.key:
            if currentNode.rightnode == None:
                newNode.parent = currentNode
                currentNode.rightnode = newNode
                return newNode.key
            else:
                insertR(B, newNode, currentNode.rightnode)
        else:
            if currentNode.key == newNode.key:
                return None
            if currentNode.leftnode == None:
                newNode.parent = currentNode
                currentNode.leftnode = newNode
                return newNode.key
            else:
                insertR(B, newNode, currentNode.leftnode)

def delete(AVLTree, element):
    # Elimina un elemento del TAD árbol AVL
    # Recorre un árbol binario en post-orden
    current = AVLTree.root
    Busca(current, AVLTree, element)


def Busca(current, B, element):
    if current != None:
        Busca(current.leftnode, B, element)
        Busca(current.rightnode, B, element)
        if current.value == element:
            return deleteKey(B, current.key)

def deleteKey(B, key):
    # Elimina una clave del TAD árbol AVL 
    # situaciones con la raiz
    aux = 0
    if B.root.leftnode == None and B.root.rightnode == None and B.root.key == key:
        B.root = None
        return None
    elif B.root.leftnode == None and B.root.rightnode == None and B.root.key != key:
        return None
    else:
        # otras
        current = B.root
        aux = deleteKeyR(current, key, B)
        reBalance(AVLTree)
        """no calculo de nuevo el factor de balanceo (actualizar) ya que (en mi caso)
    la funcion reBalance() calcula el Bf por si misma """
        return aux


def deleteKeyR(current, key, B):
    # busca el nodo
    aux = 0
    if current.key < key:
        if current.rightnode != None:
            aux = deleteKeyR(current.rightnode, key, B)
    elif current.key > key:
        if current.leftnode != None:
            aux = deleteKeyR(current.leftnode, key, B)
    elif current.key == key:
        # bloque de borrado
        # si encontro el nodo con la key
        if current.leftnode == None and current.rightnode == None:
            # encontro una hoja
            aux = current.key
            if current.key == current.parent.leftnode.key:
                current.parent.leftnode = None
            else:
                current.parent.rightnode = None
        else:  # nodo rama
            aux = current.key
            nodoActu = AVLNode()
            # dos hijos
            if current.leftnode != None and current.rightnode != None:
                buscarNodo(current.leftnode, B, nodoActu)
                current.key = nodoActu.key
                current.value = nodoActu.value
            else:
                # solo hijo der
                if current.leftnode == None:
                    if current.parent.leftnode.key == current.key:
                        current.parent.leftnode = current.rightnode
                    elif current.parent.rightnode.key == current.key:
                        current.parent.rightnode = current.rightnode
                else:
                    # solo hijo izq
                    if current.parent.leftnode.key == current.key:
                        current.parent.leftnode = current.leftnode
                    elif current.parent.rightnode.key == current.key:
                        current.parent.rightnode = current.leftnode
    else:
        # no lo encuentra
        return None
    return aux


def buscarNodo(current, B, nodoActu):
    # CRITERIO: EL MAYOR DE LOS MENORES
    # dos hijos
    if current.rightnode != None:
        buscarNodo(current.rightnode, B, nodoActu)
    else:
        # Borra la hoja correspondiente
        if current.leftnode == None and current.rightnode == None:
            nodoActu.key = current.key
            nodoActu.value = current.value
            if current.parent.leftnode != None:
                if current.key == current.parent.leftnode.key:
                    current.parent.leftnode = None
            else:
                if current.key == current.parent.rightnode.key:
                    current.parent.rightnode = None
        return nodoActu


"""Extras """
def search(B, element):
    # Busca un elemento en el TAD AVl
    # Recorre un árbol binario en post-orden
    aux = None
    current = B.root
    aux = ordenR(current, B, element, aux)
    return aux
def ordenR(current, B, element, aux):
    if current != None:
        if current.value == element:
            aux = current.key
            return aux
        aux = ordenR(current.leftnode, B, element, aux)
        aux = ordenR(current.rightnode, B, element, aux)
    return aux

def accessR(key, current, aux):
    if current == None:
        return None
    elif current.key > key:
        aux = accessR(key, current.leftnode, aux)
    elif current.key < key:
        aux = accessR(key, current.rightnode, aux)
    else:
        aux = current.value
    return aux
def access(B, key):
    # Permite acceder a un elemento con una clave determinada
    aux = 0
    aux = accessR(key, B.root, aux)
    return aux

def traverseBreadFirst(B):
    # Recorre un árbol AVl en modo primero anchura/amplitud
    List = linkedlist.LinkedList()
    ListResult = linkedlist.LinkedList()
    enqueue(List, B.root)
    while List.head != None:
        current = dequeue(List)
        enqueue(ListResult, current.value)
        if current.leftnode != None:
            enqueue(List, current.leftnode)
        if current.rightnode != None:
            enqueue(List, current.rightnode)
    while ListResult.head != None:
        aux = dequeue(ListResult)
        linkedlist.insert(List, aux, linkedlist.length(List))
    return List

def traverseBreadFirstHeight(B):
  #Recorre un árbol AVl en modo primero anchura/amplitud pero con la altura
  List=linkedlist.LinkedList()
  ListResult=linkedlist.LinkedList()
  enqueue(List,B.root)
  while List.head!=None:
    current=dequeue(List)
    enqueue(ListResult,current.height)
    if current.leftnode!= None:
      enqueue(List,current.leftnode)
    if current.rightnode != None:
      enqueue(List,current.rightnode)
  while ListResult.head!=None:
    aux=dequeue(ListResult)
    linkedlist.insert(List,aux,linkedlist.length(List))
  return List

def traverseBreadFirstBF(B):
  #Recorre un árbol AVl en modo primero anchura/amplitud pero con con sus factores de balance
  List=linkedlist.LinkedList()
  ListResult=linkedlist.LinkedList()
  enqueue(List,B.root)
  while List.head!=None:
    current=dequeue(List)
    enqueue(ListResult,current.bf)
    if current.leftnode!= None:
      enqueue(List,current.leftnode)
    if current.rightnode != None:
      enqueue(List,current.rightnode)
  while ListResult.head!=None:
    aux=dequeue(ListResult)
    linkedlist.insert(List,aux,linkedlist.length(List))
  return List