"""
    Implementation of binary search tree
"""



# Node 
class Node:
    def __init__(self,data : int): 
        self.left = None 
        self.data = data 
        self.right = None 

def findMin(root : Node) -> Node: 
    while(root.left is not None):
        root = root.left 
    return root

def buildBST(root : Node,data : int) -> Node:
    """
        Building binary search tree
    """ 
    if(root is None):
        return Node(data)

    elif(data < root.data):
        root.left  = buildBST(root.left,data) 
    else:
        root.right = buildBST(root.right,data) 
    
    return root 


def searchNode(root : Node,data : int) -> Node: 
    """
        Search a node from BST
    """
    if(root is None):
        return None 
    
    elif(data < root.data):
        return searchNode(root.left,data)
    elif(data > root.data):
        return searchNode(root.right,data) 
    
    return root

def removeNode(root : Node,data :int ): 
    """
        Remove node form BST
    """
    if(root is None): 
        return None
    elif(data < root.data):
        root.left =  removeNode(root.left,data)
    elif(data > root.data):
        root.right =  removeNode(root.right,data) 
    else:
        # leaf node 
        if(root.left is None and root.right is None):
            del root 
            root = None 
        # only left subtree 
        elif(root.right is None):
            node = root 
            root = root.left 
            del node
        # Only right subtree 
        elif(root.left is None):
            node = root 
            root = root.right
            del node
        else: 
            node = findMin(root.right)
            root.data = node.data
            root.right = removeNode(root.right,root.data) 
    
    return root 


def  inorderTraversal(root : Node) -> None:
    if(root is None):
        return 
    inorderTraversal(root.left) 
    print(root.data,end = " ")
    inorderTraversal(root.right) 


if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,2,8,1,9,10] # Arrayof integers
    root = None # Intialization of root node 
    for x in arr: # Inser all array elements into BST
        root = buildBST(root,x) 

    # Inorder traversal of BST 
    print(f"Inorder traversal : ",end = " ")
    inorderTraversal(root) 
    print()

    data = int(input("Insert new node : "))
    root = buildBST(root,data) 

    print(f"Inorder traversal : ",end = " ")
    inorderTraversal(root) 
    print()


    data = int(input("Enter the data to search : "))
    node = searchNode(root,data)
    if(node is not None):
        print(f"{node.data} is found at {node}") 
    else: 
        print(f"{data} is not found at BST")

    data = int(input("Entre the data to delete : "))
    root = removeNode(root,data) 
    print(f"Inorder traversal of BST : ",end = " ")
    inorderTraversal(root)
    print()

 