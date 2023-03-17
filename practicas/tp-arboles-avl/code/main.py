import binarytree
import linkedlist 
from avltree import *


BA=AVLTree()
insert(BA,6,6),insert(BA,4,4),insert(BA,7,7)
insert(BA,5,5),insert(BA,3,3),insert(BA,2,2)

c=traverseBreadFirst(BA)
linkedlist.printList(c)
c=traverseBreadFirstBF(BA)
linkedlist.printList(c)

delete(BA,3)

c=traverseBreadFirst(BA)
linkedlist.printList(c)
c=traverseBreadFirstBF(BA)
linkedlist.printList(c)


