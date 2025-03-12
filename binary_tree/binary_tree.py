
from typing import Any 
from queue import Queue

class Node: 
    def __init__(self,data : Any):
        self.left = None 
        self.right = None 
        self.data =  data




def buildTree() -> Node:
    """
        Buildinfd the tree
    """
    data = int(input("Enter the data : "))
    if(data == -1): 
        return None 
    new_node = Node(data) 
    new_node.left = buildTree() 
    new_node.right = buildTree() 
    return new_node



def preorderTraversal(root : None) -> None:
    if(root is None):
        return 
    
    print(root.data,end = ",")
    preorderTraversal(root.left)
    preorderTraversal(root.right) 

def postorderTraversal(root : Node) -> None: 
    if(root is None):
        return  
    postorderTraversal(root.left) 
    postorderTraversal(root.right) 
    print(root.data,end = ",") 

def inorderTraversal(root : Node) -> None: 
    if(root is None):
        return 

    inorderTraversal(root.left) 
    print(root.data,end = ",")
    inorderTraversal(root.right) 


def levelorderTraversal(root : Node) -> None:
    if(root is None):
        return  
    q =  Queue()
    q.put(root) 
    while(not q.empty()):
        temp_node = q.get() 
        if(temp_node.left is not None):
            q.put(temp_node.left) 
        if(temp_node.right is not None):
            q.put(temp_node.right) 
        print(temp_node.data,end=",") 


def height(root : Node) -> int: 
    if(root is None):
        return 0 
    
    h1 : int = height(root.left) 
    h2 : int = height(root.right) 
    return 1 + max(h1,h2)


if(__name__ == "__main__"):
    root = buildTree()
    print(f"Preorder traversal : ",end = " ")
    preorderTraversal(root)
    print() 
    print(f"Postorder traversal : ",end = " ")
    postorderTraversal(root) 
    print()
    print(f"Inorder traversal : ",end = " ")
    inorderTraversal(root) 
    print()
    print(f"Level order traversal : ",end = " ")
    levelorderTraversal(root) 
    print()
    print(f"Height of the binary tree : {height(root)}",end = " ")
    
    