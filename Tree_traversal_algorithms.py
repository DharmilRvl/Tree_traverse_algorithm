#creating a node class
class Node:
    def __init__(self,val):
        self.childleft= None
        self.childright= None
        self.nodedata= val

# creating an instance to construct tree
root = Node(1)
root.childleft= Node(2)
root.childright= Node(3)
root.childleft.childleft= Node(4)
root.childleft.childright= Node(5)
""" This is the tree for reference
             1
         2       3
       4   5       """
def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)
InOrd(root)

def Preord(root):
    if root:
        print (root.nodedata)
        Preord(root.childleft)
        Preord(root.childright)
Preord(root)

def Postord(root):
    if root:
        Postord(root.childright)
        print(root.nodedata)
        Postord(root.childleft)
Postord(root)
        



        
