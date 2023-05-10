from graphs import *



ListV=[0,1,2,3,4,5,6,7]
ListA=[(0,1,3),(0,2,4),(1,2,2),(1,3,3),(1,5,1),(2,5,8),(2,6,1),(2,4,2),(3,5,5),(3,7,2),(4,6,7),(4,7,1),(5,7,2),(6,7,1),(1,0,3),(7,5,1)]


#G=createGraph(ListV, ListA)
#P_List_AD(G)
#mat1=createGraph_Mat_with_edges(ListV, ListA)
#mat=createGraph_Mat(ListV, ListA)

#printMat(mat,ListV)
#print("-----------")
#printMat2(mat1)

#PRIM(mat)

#KRUSKAL(mat1)


#ListV=["s","t","y","z","x"]
#ListA=[("s","y",5),("s","t",10),("y","z",2),("z","x",6),("x","z",4),("z","s",7),("t","x",1),("t","y",2),("y","t",3),("y","x",9)]

matD=createDirected_G_Mat_with_edges(ListV, ListA)
printMat2(matD)

print(shortestPath(matD,3,7))
