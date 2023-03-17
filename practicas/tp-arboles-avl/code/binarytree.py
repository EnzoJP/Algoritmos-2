import math
import linkedlist
from myqueue import *


class BinaryTree:
    root = None


class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None


# EJERCICIO 1

def search(B, element):
    # Busca un elemento en el TAD árbol binario
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
# ---------------------------------


def insert(B, element, key):
    # Inserta un elemento con una clave determinada del árbol binario
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element
    currentNode = B.root
    insertR(B, newNode, currentNode)


def insertR(B, newNode, currentNode):
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

# ---------------------------------


def delete(B, element):
    # Elimina un elemento del TAD árbol binario
    # Recorre un árbol binario en post-orden
    current = B.root
    Busca(current, B, element)


def Busca(current, B, element):
    if current != None:
        Busca(current.leftnode, B, element)
        Busca(current.rightnode, B, element)
        if current.value == element:
            return deleteKey(B, current.key)

# ---------------------------------


def deleteKey(B, key):
    # Elimina una clave del TAD árbol binario
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
            nodoActu = BinaryTreeNode()
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

# ---------------------------------


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
# ---------------------------------


def update(B, element, key):
    # Cambiar el valor de un elemento con una clave determinada
    current = B.root
    aux = None
    aux = updateR(B, key, element, current, aux)
    return aux


def updateR(B, key, element, current, aux):
    if current != None:
        aux = updateR(B, key, element, current.leftnode, aux)
        aux = updateR(B, key, element, current.rightnode, aux)
        if current.key == key:
            current.value = element
            return current.key
    return aux

# EJERCICIO 2


def traverseInOrder(B):
    # Recorre un árbol binario en orden
    L = linkedlist.LinkedList()
    current = B.root
    ordenI(current, B, L)
    return L


def ordenI(current, B, L):
    if current != None:
        ordenI(current.leftnode, B, L)
        linkedlist.insert(L, current.value, linkedlist.length(L))
        ordenI(current.rightnode, B, L)
    return L


def traverseInPostOrder(B):
    # Recorre un árbol binario en post-orden
    L = linkedlist.LinkedList()
    current = B.root
    ordenPO(current, B, L)
    return L


def ordenPO(current, B, L):
    if current != None:
        ordenPO(current.leftnode, B, L)
        ordenPO(current.rightnode, B, L)
        linkedlist.insert(L, current.value, linkedlist.length(L))
    return L


def traverseInPreOrder(B):
    # Recorre un árbol binario en pre-orden
    L = linkedlist.LinkedList()
    current = B.root
    ordenRP(current, B, L)
    return L


def ordenRP(current, B, L):
    if current != None:
        linkedlist.insert(L, current.value, linkedlist.length(L))
        ordenRP(current.leftnode, B, L)
        ordenRP(current.rightnode, B, L)
    return L


def traverseBreadFirst(B):
    # Recorre un árbol binario en modo primero anchura/amplitud
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

# OTROS


def muestraArbolBin(B):
    # muestra el arbol binario
    print(B.root.key)
    print("-----")
    print(B.root.leftnode.key)
    print(B.root.rightnode.key)
    print("-----")
    print(B.root.leftnode.leftnode.key)
    print(B.root.leftnode.rightnode.key)
    print(B.root.rightnode.rightnode.key)
    print("-----")
    print(B.root.leftnode.rightnode.leftnode.key)
    print(B.root.leftnode.rightnode.rightnode.key)
    print(B.root.rightnode.rightnode.leftnode.key)


def muestraArbolBinElemnts(B):
    # muestra el arbol binario
    print(B.root.value)
    print("-----")
    print(B.root.leftnode.value)
    print(B.root.rightnode.value)
    print("-----")
    print(B.root.leftnode.leftnode.value)
    print(B.root.leftnode.rightnode.value)
    print(B.root.rightnode.rightnode.value)
    print("-----")
    print(B.root.leftnode.rightnode.leftnode.value)
    print(B.root.leftnode.rightnode.rightnode.value)
    print(B.root.rightnode.rightnode.leftnode.value)
