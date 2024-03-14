
#-----------------P.DINAMICA---------------------------

def darCambioDP(cambio, monedas):
    dp = [float('inf')] * (cambio + 1)
    dp[0] = 0

    for i in range(1, cambio + 1):
        for moneda in monedas:
            if moneda <= i:
                dp[i] = min(dp[i], dp[i - moneda] + 1)

    return dp[cambio]
"""
def caminoEnMat(Tabla):
    #eqR=min(abajo y derecha) si son posibles
    #caso base cuando casilla n,n
    res=[]
    i=0
    j=0
    while i!= len(Tabla) or j != len(Tabla):
        if i+1 <= len(Tabla[i])-1 and j+1 <= len(Tabla[j])-1:
            aux=min(Tabla[i+1][j],Tabla[i][j+1])
            if Tabla[i+1][j] <= Tabla[i][j+1]:
                i=i+1
            else:
                j=j+1
            res.append(aux)
        elif i+1 <= len(Tabla)-1:
            aux=Tabla[i+1][j]
            i=i+1
            res.append(aux)
        elif j+1 <= len(Tabla)-1:
            aux=Tabla[i][j+1]
            res.append(aux)
    return res
 """      
def caminoEnMat(Tabla):
    filas = len(Tabla)
    columnas = len(Tabla[0])

    # Inicializar la tabla auxiliar dp
    dp = [[0] * columnas for _ in range(filas)]

    # Llenar la primera fila y columna de dp con sumas acumulativas
    for j in range(columnas):
        dp[0][j] = dp[0][j - 1] + Tabla[0][j] if j > 0 else Tabla[0][j]

    for i in range(1, filas):
        dp[i][0] = dp[i - 1][0] + Tabla[i][0]

    # Calcular las sumas acumulativas mínimas
    for i in range(1, filas):
        for j in range(1, columnas):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + Tabla[i][j]

    # Construir el camino óptimo
    camino_optimo = []
    i, j = filas - 1, columnas - 1

    while i > 0 or j > 0:
        camino_optimo.append(Tabla[i][j])

        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    camino_optimo.append(Tabla[0][0])
    camino_optimo.reverse()

    return camino_optimo

#-----------------BACKTRACKING------------------------- 

def darCambioBacktracking(cambio, monedas):
    def backtrack(cambio_actual, index):
        nonlocal min_monedas

        if cambio_actual == 0:
            min_monedas = min(min_monedas, len(current_solution))
            return

        for i in range(index, len(monedas)):
            if monedas[i] <= cambio_actual:
                current_solution.append(monedas[i])
                backtrack(cambio_actual - monedas[i], i)
                current_solution.pop()

    min_monedas = float('inf')
    current_solution = []
    backtrack(cambio, 0)
    return min_monedas

def mochila(PesoMax, latas):
    def mochilaR(PesoMax, latas, currSol, latasmax):
        if PesoMax == 0:
            latasmax.append(currSol.copy())
            return

        for i in range(len(latas)):
            if latas[i] <= PesoMax:
                currSol.append(latas[i])
                mochilaR(PesoMax - latas[i], latas[i+1:], currSol, latasmax)
                currSol.pop()

    latasmax = []
    mochilaR(PesoMax, latas, [], latasmax)
    return latasmax

#-----------------GREEDY-------------------------------

def adminActividades(tareas, inicio, fin):
    n = len(tareas)

    # Ordenar las tareas por tiempo de finalización
    tareas_ordenadas = sorted(zip(tareas, inicio, fin), key=lambda x: x[2])

    # Inicializar la lista de tareas seleccionadas
    seleccionadas = []

    # La primera tarea siempre se selecciona
    seleccionadas.append(tareas_ordenadas[0][0])

    # Iterar sobre las tareas restantes
    tarea_previa = tareas_ordenadas[0]
    for i in range(1, n):
        tarea_actual = tareas_ordenadas[i]
        # Si el inicio de la tarea actual es posterior al final de la tarea previa, la seleccionamos
        if tarea_actual[1] >= tarea_previa[2]:
            seleccionadas.append(tarea_actual[0])
            tarea_previa = tarea_actual

    return seleccionadas

def buscaPares(vector):
    #tomamos los pares consecutivos
    i=0
    pares=[]
    while i < len(vector):
        aux=vector[i]+vector[i+1]
        pares.append(aux)
        i+=2
    return max(pares)

#-----------------Divide y Vencerás--------------------

def busquedaKesimo(lista, k):
    if k > 0 and k <= len(lista):
        return quickselect(lista, 0, len(lista) - 1, k)
    else:
        return None

def quickselect(lista, inicio, fin, k):
    if inicio == fin:
        return lista[inicio]

    pivot_index = particion(lista, inicio, fin)

    if k - 1 == pivot_index:
        return lista[pivot_index]
    elif k - 1 < pivot_index:
        return quickselect(lista, inicio, pivot_index - 1, k)
    else:
        return quickselect(lista, pivot_index + 1, fin, k)

def particion(lista, inicio, fin):
    pivot = lista[fin]
    i = inicio

    for j in range(inicio, fin):
        if lista[j] <= pivot:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    lista[i], lista[fin] = lista[fin], lista[i]
    return i

def subsecuenciaCreciente(numeros):
    def Srec(numeros,ind,res,head):
        Lmen=[]
        Lmay=[]
        if len(numeros)==0:
            return res
        for i in range(0,len(numeros)):
            if numeros[i]<= head:
                Lmen.append(numeros[i])
            else:
                Lmay.append(numeros[i])
        res.append(head)
        if len(Lmay) > 0:
            head=Lmay[0]
        return Srec(Lmay,ind+1,res,head)
    head=numeros[0]
    return Srec(numeros,1,[],head)

        



monedas1 = [1, 2, 6, 8, 10]
cambio1 = 14
print("Programación Dinámica", darCambioDP(cambio1, monedas1))

monedas1 = [1, 2, 6, 8, 10]
cambio1 = 14
print("Backtracking ", darCambioBacktracking(cambio1, monedas1))

print("peso max ", mochila(10,[1,2,3,4,5]))

tareas = ["T1", "T2", "T3", "T4", "T5", "T6"]
inicio = [1, 3, 0, 5, 8, 5]
fin = [2, 4, 6, 7, 9, 9]

resultado = adminActividades(tareas, inicio, fin)
print("Tareas seleccionadas:", resultado)

print("maxima suma par ",buscaPares([5,8,1,4,7,9]))

print("secuencia m ",subsecuenciaCreciente([1,2,3,5,4,8,6,9]))

