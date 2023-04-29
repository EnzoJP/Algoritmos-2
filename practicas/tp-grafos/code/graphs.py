"""-----------Graphs--------------"""
#Part 1------->

"""Ejercicio 1"""

def createGraph(listV, listA):
    #operación crear grafo
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
    #cantidad de componentes conexas
    arist=[] #lista de aristas 
    for each in Grafo:
        for i in range(0,len(each)):
            if i != 0:
                if (each[0],each[i]) not in arist and (each[i],each[0]) not in arist:
                    arist.append((each[0],each[i]))
    L=make_set(Grafo)#coloco cada vertice en una lista propia
    for i in range(0,len(arist)):#comparo y realizo la coleccion de conjuntos uniendolos cuando una arista los une 
        n1=arist[i][0]
        n2=arist[i][1]
        flag=False
        for x in range(0,len(L)):
            for j in range(0,len(L[x])):
                if n1==L[x][j]:
                    index1=x
                    flag=True
                if n2==L[x][j]:
                    index2=x
                    aux=L[index2]
                    flag=True
        if index1!=index2 and flag is True:
            L[index1].append(aux)
            if aux in L:
                L.remove(aux)
    print(L)
    return len(L)
    
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







