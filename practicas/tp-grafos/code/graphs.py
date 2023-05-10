"""-----------Graphs--------------"""
#Part 1------->

"""Ejercicio 1"""

def createGraph(listV, listA):
    #operación crear grafo Lista de adyacencia
    #ListV-listaNumeros, ListA-ListaTuplas
    graph=[]
    #creo la lista de adyacencia con los vertices
    for i in range(0,len(listV)):
        L=[]
        graph.append(L)
        graph[i].append(listV[i])
    #comparo y relleno
    for i in range(0,len(graph)):
        aux=graph[i][0]
        for j in range(0,len(listA)):
            #como no es dirijido inserto en ambos sentidos
            if listA[j][0]==aux: 
                graph[i].append(listA[j][1])
            if listA[j][1]==aux:
                graph[i].append(listA[j][0])

    return graph

"""Ejercicio 2"""

def existPath(Grafo, v1, v2):
    #un camino entre los vértices v1 y v2
    Lis_bfs=BFS(Grafo,v1)

    #como la funcion de bfs asume que el grafo es conexo
    # si no esta el v2 en la lista significa que no hay camino

    for current in Lis_bfs:
        if current is v2:
            return True
    return False         

"""Ejercicio 3"""

def isConnected(Grafo):
    #Implementa la operación es conexo
    Lis_bfs=BFS(Grafo,Grafo[0][0])
    verts=[]
    for current in Grafo:
        #los primeros elementos de la lista de ady son los vertices
        verts.append(current[0])
        
    #la funcion de bfs asume que el grafo es conexo asi que solo comparo
    for vert in verts:
        find=False
        for each in Lis_bfs:
            if each == vert:
                find=True
        if find is False:
            return False
    return True

"""Ejercicio 4"""

def isTree(graph):
    #Implementa la operación es árbol
    #que sea conexo
    if  isConnected(graph) is False:
        return False
    #que no tenga ciclos
    if Aristas(graph)==len(graph)-1: return True
    else: return False
    
"""Ejercicio 5"""

def isComplete(Grafo):
    #Implementa la operación es completo
    index=0
    L_verts=[]
    for each in Grafo:
        L_verts.append(Grafo[0][0])
    for i in range(0,len(Grafo)):
        #comparo las longuitudes de las listas de adyacencia
        if len(Grafo[i])!=len(L_verts):
            return False
        else:
            #chequeo que todos los elementos sean los de la lista de vertices
            cond=False
            for j in range(0,len(L_verts)):
                if Grafo[i][j]==L_verts[i]:
                    cond=True
            if cond is False:
                return True
    return True

"""Ejercicio 6"""
def convertTree(Grafo):
    #dado un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol
    Aux=[]#cuento las aristas
    for each in Grafo:
        for i in range(0,len(each)):
            if i != 0:
                if (each[0],each[i]) not in Aux and (each[i],each[0]) not in Aux:
                    Aux.append((each[0],each[i]))
    visted=[]
    elimA=[]
    cont=0 #si ambas estan entonces esa arista tiene que eliminarse
    while cont<len(Aux):
        flag=True
        if Aux[cont][0] not in visted or Aux[cont][1] not in visted:
            if Aux[cont][0] not in visted: visted.append(Aux[cont][0])
            if Aux[cont][1] not in visted: visted.append(Aux[cont][1])
            cont=cont+1
        else:
            elimA.append(Aux[cont])
            Aux.remove(Aux[cont])
    print (Aux)
    return elimA
    

"""Extras"""

def P_List_AD(graph):
    #imprime la lista de adyacencia
    for each in graph:
        print("[",each[0],"]","--->",end="")
        print(each[1:])
        print("----")

def SearchVert(V,G):
    #busca un vertice y devuelve el indice
    for i in range(0,len(G)):
        if G[i][0]==V:
            return i

def search(l,value):
    #devuelve el value o None en caso contario
    for i in range(0,len(l)):
        if value==l[i]:
            return value
    return None    

def BFS (graph,V):
    #return a list bfs Of Graph
    #coloco en la queue el vertice
    queue=[]
    queue.append(V)
    #creo las listas de recorridos y pendientes
    grayList=[]
    blackList=[]
    #marco el primer nodo como gris
    grayList.append(V)

    while len(queue)>0:
        #saco el elemento para luego ponerlo en la lista negra
        posc=SearchVert(queue[0],graph)
        aux=queue.pop(0)
        #me ubico en la lista de el elemto que estoy visitando
        L=graph[posc]
        #si no estan sus elementos en la lista gris los agrega 
        for current in L:
            if search(grayList,current)==None:
                grayList.append(current)
                queue.append(current)
        blackList.append(aux)
    
    return blackList

def DFS(graph):
    #return a list dfs Of Graph
    grayList=[]
    blackList=[]
    whitelist=[]
    #coloco todos en blanco
    for each in graph:
        whitelist.append(each[0])
    for each in graph:
        vertex=each[0]
        #busco los nodos que son blancos
        if search(whitelist,vertex)!=None:
            DFS_Visit(graph,vertex,grayList,whitelist,blackList)
    blackList.reverse()
    return blackList

def DFS_Visit(G,V,grayList,whitelist,blackList):
    #saco de los blancos y los pongo en gris
    whitelist.remove(V)
    grayList.append(V)
    posc=SearchVert(V,G)
    #busco en cada sublista blancos
    for each in G[posc]:
        if search(whitelist,each)!=None:
            DFS_Visit(G,each,grayList,whitelist,blackList)
    blackList.append(V)

def Aristas(Graph):
    #cuenta las aristas
    A_count=0
    for each in Graph:
        A_count+=len(each)-1
    return round(A_count/2)
        
def Cicles_DFS(graph):
    #detecta ciclos con dfs
    grayList=[]
    blackList=[]
    whitelist=[]
    cond=False
    #coloco todos en blanco
    for each in graph:
        whitelist.append(each[0])
    for each in graph:
        vertex=each[0]
        #busco los nodos que son blancos
        if search(whitelist,vertex)!=None:
            cond=DFS_Visit2(graph,vertex,grayList,whitelist,blackList)
            if cond is True:
                return cond
    return cond

def DFS_Visit2(G,V,grayList,whitelist,blackList):
    #saco de los blancos y los pongo en gris
    whitelist.remove(V)
    grayList.append(V)
    posc=SearchVert(V,G)
    #busco en cada sublista blancos
    for each in G[posc]:
        if search(whitelist,each)!=None:
            DFS_Visit(G,each,grayList,whitelist,blackList)
        else:
            if each is not V:
                return True
    blackList.append(V)

#Part 2-------> 
"""Ejercicio 7"""

def countConnections(Grafo):
    #Implementa la operación cantidad de componentes conexas
    verts=[]
    #cantidad de componentes conexas
    arist=[] #lista de aristas 
    for each in Grafo:
        verts.append(each[0])
    #veo los vertices
    visited=[]
    components=[]
    #bfs asume que no son conexos lo que me sirve para ver los que estan conectados
    for each in verts:
        if each not in visited:
            L=BFS(Grafo,each)
            for each in L:
                visited.append(each)
            components.append(L)
    print(components)
    return len(components)
    
"""Ejercicio 8"""

def convertToBFSTree(Grafo, v):
    #Convierte un grafo en un árbol BFS
    Aristas=[]
    if isConnected(Grafo) is True:
        #la op de bfs asume que es conexo
        #coloco en la queue el vertice
        queue=[]
        queue.append(v)
        #creo las listas de recorridos y pendientes
        grayList=[]
        blackList=[]
        #marco el primer nodo como gris
        grayList.append(v)

        while len(queue)>0:
            #saco el elemento para luego ponerlo en la lista negra
            posc=SearchVert(queue[0],Grafo)
            aux=queue.pop(0)
            #me ubico en la lista de el elemto que estoy visitando
            L=Grafo[posc]
            #si no estan sus elementos en la lista gris los agrega 
            for current in L:
                if search(grayList,current)==None:
                    grayList.append(current)
                    queue.append(current)
                    Aristas.append((aux,current))
            blackList.append(aux)
    print(blackList)
    print(Aristas)   
    return createGraph(blackList,Aristas)

"""Ejercicio 9"""

def convertToDFSTree(Grafo):
    #convierte un grafo en un árbol DFS
    grayList=[]
    blackList=[]
    whitelist=[]
    Aristas=[]
    #coloco todos en blanco
    for each in Grafo:
        whitelist.append(each[0])
    for each in Grafo:
        vertex=each[0]
        #busco los nodos que son blancos
        if search(whitelist,vertex)!=None:
            DFS_Visit_TREE(Grafo,vertex,grayList,whitelist,blackList,Aristas)
    blackList.reverse()
    print(blackList)
    print(Aristas)
    return createGraph(blackList,Aristas)
   
"""Ejercicio 10"""

def bestRoad(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return

#otra implementacion es asignarle a cada nodo un parent en bfs y luego ver el camino de uno a otro 
# en el arbol bfs

"""Extras"""

def make_set(graph):
    L=[]
    for i in range(0,len(graph)):
        L.append([])
        L[i].append(graph[i][0])
    return L

def DFS_Visit_TREE(G,V,grayList,whitelist,blackList,Aristas):
    #saco de los blancos y los pongo en gris
    whitelist.remove(V)
    grayList.append(V)
    posc=SearchVert(V,G)
    #busco en cada sublista blancos
    for each in G[posc]:
        if search(whitelist,each)!=None:
            Aristas.append((each,V))
            DFS_Visit_TREE(G,each,grayList,whitelist,blackList,Aristas)
    blackList.append(V)


#Part 3------->


def createGraph_Mat(vertices, aristas):
    #crea la matriz de adyacencia pero SIN los bordes
    vertices.sort()
    n = len(vertices)
    # crear matriz de adyacencia inicializada con ceros
    matriz = [[0] * n for x in range(n)]
    # llenar matriz con unos donde haya aristas
    for u, v,weight in aristas:
        i = vertices.index(u)
        j = vertices.index(v)
        matriz[i][j] = matriz[j][i] = weight   
    return matriz

def createGraph_Mat_with_edges(vertices, aristas):
    #crea la matriz de adyacencia pero CON los bordes
    #agrego los bordes
    vertices.sort()
    n = len(vertices)
    # crear matriz de adyacencia inicializada con ceros
    matriz = [[0] * n for x in range(n)]
    # llenar matriz con unos donde haya aristas
    for u, v,weight in aristas:
        i = vertices.index(u)
        j = vertices.index(v)
        matriz[i][j] = matriz[j][i] = weight
    for i in range(0,len(matriz)):
        matriz[i].insert(0,vertices[i])
    matriz.insert(0,["V"])
    for each in vertices:
        matriz[0].append(each)
 
    return matriz

def printMat2(mat):
    #imprime una matriz hecha con listas que SI tiene los bordes
    for each in mat:
        print(each)

def printMat(mat,vertices):
    #imprime una matriz hecha con listas que NO tiene los bordes
    print("V",vertices)
    cont=0
    for each in mat:
        cont+=1
        if cont==len(mat):
            print(vertices[cont-1],each,"]")
        else:
            print(vertices[cont-1],each)



def PRIM(G):
    #algoritmo de prim para AACM
    # Numero de vertices
    N = len(G)
    selected_node = [0]*N
    U = 0
    selected_node[0] = True

    ListV=[]
    ListA=[]

    while (U < N - 1): #(O|V|)
        vert=search_minimun_edge(N,selected_node,G,ListA)
        selected_node[vert] = True
        U += 1
        ListV.append(vert)

    return createGraph(ListV,ListA)

def search_minimun_edge(N,selected_node,G,ListA):
    minimum = 999999
    a = 0
    b = 0
    for i in range(N):
            if selected_node[i] is True:
                for j in range(N):
                    if selected_node[j] is not True and G[i][j]!=0:  
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            a = i
                            b = j
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    aux=(a,b,G[a][b])
    ListA.append(aux)
    return b



def KRUSKAL(Grafo):
    #algoritmo de Kruskal para AACM
    Arists=[]
    verts=[]
    Makeset=[]
    #veo las aristas, los vertices y la implementacion de make set
    for i in range(0,len(Grafo)):
        if i!=0:
            verts.append(Grafo[0][i])
            Makeset.append([Grafo[0][i]])
            for j in range(0,len(Grafo)):
                if j!=0:
                    a=Grafo[0][i]
                    b=Grafo[j][0]
                    c=Grafo[a+1][b+1]
                    if c!=0 and (((a,b,c) not in Arists) and ((b,a,c) not in Arists)) :
                        Arists.append((a,b,c))
    #ordeno los pesos
    AS=sort_by_weight(Arists)
    New_arist=[]
    for each in AS:
        a=find_set(each[0],Makeset)
        b=find_set(each[1],Makeset)
        if a is not b:
            New_arist.append(each)
            Union(a,b,Makeset)
    print(New_arist)
    return createGraph(verts,New_arist)

def sort_by_weight(L):
    #ordena por el peso de la arista
    weights=[]
    ArSort=[]
    for each in L:
        weights.append(each[2])
    weights.sort()
    for i in range(0,len(weights)):
        for j in range(0,len(L)):
            if weights[i]==L[j][2]:
                if L[j] not in ArSort: 
                    ArSort.append(L[j])
    return ArSort

def find_set(V,Makeset):
    #busca el conjunto conexo de un vertice dado
    for each in Makeset:
        if V in each:
            return each

def Union(l1,l2,L):
    #une los conjuntos conexos
    i=0
    for each in L:
        if l1==each:
            aux=l1
        elif l2==each:
            index=i
        i+=1
    for each in aux:
        L[index].append(each)
    L.remove(l1)

#--------------------------


def createDirected_G_Mat_with_edges(vertices, aristas):
    #crea la matriz de adyacencia pero CON los bordes (Grafo Dirijido)
    #agrego los bordes
    #crea la matriz de adyacencia pero SIN los bordes
    vertices.sort()
    n = len(vertices)
    # crear matriz de adyacencia inicializada con ceros
    matriz = [[0] * n for x in range(n)]
    # llenar matriz con unos donde haya aristas
    for u, v,weight in aristas:
        i = vertices.index(u)
        j = vertices.index(v)
        matriz[i][j] = weight
    for i in range(0,len(matriz)):
        matriz[i].insert(0,vertices[i])
    matriz.insert(0,["V"])
    for each in vertices:
        matriz[0].append(each)
 
    return matriz


class Vertex:
    distance=None
    parent=None
    key=None
        


def shortestPath(Grafo, s, v):
    #determina el algoritmo de 
    verts=initRelax(Grafo,s)
    visited=[]
    queue=minqueue(verts)#ordeno por dist
    while len(queue)>0:
        u=queue.pop(0)
        visited.append(u)
        for each in adjunt(u.key,Grafo,verts):# lista de adjuntos
            if each not in visited:
                relax(u,each,Grafo)
        queue=minqueue(queue)
    #bloque para ver S
    a=None
    b=None
    for each in verts:
        if each.key==s:
            a=each
        elif each.key==v:
            b=each
    S_Path=parent_path(b,a)
    return  S_Path




def initRelax(G,s):
    #veo los vertices
    verts=[]
    Nodes=[]
    for i in range(0,len(G)):
        if i!=0:
            verts.append(G[0][i])
    #Relax inicial
    for ve in verts:
        if ve==s:
            newNode=Vertex()
            newNode.key=ve
            newNode.parent=None
            newNode.distance=0
            Nodes.append(newNode)
        else:
            newNode=Vertex()
            newNode.key=ve
            newNode.parent=None
            newNode.distance=9999#inf
            Nodes.append(newNode)
    return Nodes

def minqueue(V):
    #devulve una queue con los nodos ordenados por distancia
    q=[0]*len(V)
    d=[]
    for each in V:
        d.append(each.distance)
    d.sort()
    for i in range(0,len(V)):
        for each in V:
            if d[i]==each.distance and each not in q:
                q[i]=each
    return q

def adjunt(v,G,verts):
    #da una lista de vertices adjuntos a el
    adj=[]
    aux=[]
    for i in range(len(G)):
        if i!=0:
            if G[i][0]==v:
                for j in range(0,len(G[i])):
                    if G[i][j]!=0 and j!=0:
                        aux.append(G[0][j])
    for each in verts:
        if each.key in aux:
            adj.append(each)
    return adj

def relax(u,v,G):
    #relaja el vertice actualizando su parent y su distancia
    if v.distance > (u.distance + calculeweight(u.key,v.key,G)):
        v.distance = u.distance + calculeweight(u.key,v.key,G)
        v.parent= u


def calculeweight(u,v,G):
    #calcula el peso de una arista
    a=G[0].index(v)
    a=a
    for i in range(0,len(G)):
        if i!=0 and G[i][0]==u:
            return G[i][a]

def parent_path(v,s):
    #calcula el camino mas corto mirando los parent
    L=[]
    L.insert(0,v.key)
    aux=True
    while aux!=False:
        if v.parent is not None:
            v=v.parent
            if v.key==s.key:
                aux=False
        else:
            return None
        L.append(v.key)
        #L.reverse()
    return L




