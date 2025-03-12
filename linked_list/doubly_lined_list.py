"""
    Doubly linkde list
"""

from typing import Any
class doubluLInkedList:
    # Define the node
    class Node:
        def __init__(self,data : Any):  
            self.left = None 
            self.data = data 
            self.right = None 

    def __init__(self):
        self.__head = None 
        self.__tail = None 
    
    def empty(self) -> bool:
        """
            Return true if doubly linked list is empty
        """
        return self.__head == None and self.__tail == None 
    
    def addNode(self,data,index = -1):
        """
            Add new node into doubly linked list 
        """
        # Create new node 
        new_node = self.Node(data)
        if(new_node is None):
            raise MemoryError("Memory is full can not new node into doubly linked list") 
        # Add node into doubly linked list 
        if(self.empty()):
            self.__head = self.__tail = new_node
        # Add new node at head of the list
        elif(index == 0):
            new_node.right = self.__head 
            self.__head.left = new_node 
            self.__head = new_node 
        # Add node of the tail of the list
        elif(index == -1):
            self.__tail.right = new_node
            new_node.left = self.__tail 
            self.__tail = new_node
        # Add node at perticular location
        else:
            idx = 1
            cur_node = self.__head.right
            prev_node = self.__head 
            while((cur_node is not None) and (idx < index)): 
                idx += 1
                prev_node = cur_node 
                cur_node = cur_node.right
            
            
            if(cur_node is not None): 
                new_node.right = cur_node 
                cur_node.left = new_node 
                new_node.left = prev_node
                prev_node.right = new_node
            else: 
                raise IndexError("Out of the index") 



        
    def removeNode(self,data : Any) -> None:
        """
            Remove node from doubly linked list
        """

        # data in head of the doubly linked list 
        if(self.__head.data == data):
            node = self.__head
            # Only one node in list 
            if(self.__head == self.__tail):
                self.__head = self.__tail = None 
            
            else:
                self.__head = self.head.right 
            del node 
        
        else: 
            prev_node = self.__head 
            curr_node = self.__head.right 
            while((curr_node is not None) and (curr_node.data != data)): 
                prev_node = curr_node
                curr_node = curr_node.right 
            if(curr_node is not None):
                if(curr_node.right is not None): 
                    prev_node.right = curr_node.right 
                    curr_node.right.left = prev_node
                else:
                    prev_node.right = None  
                del curr_node 
            else: 
                print(f"[INFO] {data} is not found in doubly linked list") 
    

    def clear(self) -> None: 
        """
            Remove all nodes form doubly linkde list 
        """
        node = self.__head 
        while(node is not None): 
            temp = node 
            node = node.right 
            del temp 

        self.__head = self.__tail = None 
    
    def forwardTraversal(self) -> None: 
        """
            Traverse doubly linked list from left to right
        """
        node = self.__head 
        while(node is not None): 
            print(node.data,end = ",")
            node = node.right 
        
    def bachwardTravesal(self) -> None: 
        """
            Traverse doubly linked list from right to left
        """
        node = self.__tail 
        while node is not None: 
            print(node.data,end = ",")
            node = node.left



def traversal(ob : doubluLInkedList):
    print(f"Forward traversal : ",end = " ")
    o1.forwardTraversal()
    print() 
    print(f"Backward traversal : ",end = " ")
    o1.bachwardTravesal()
    print()



if(__name__ == "__main__"): 
    o1 = doubluLInkedList() 
    arr : list = [1,2,3,4,5,6,7,8,9,10] 
    for x in arr: 
        o1.addNode(x)
    traversal(o1)

    # Insert new node
    data = int(input("Enter the data : "))
    idx = int(input("Enter the index to insert  : "))
    o1.addNode(data,idx)
    traversal(o1)

    # get data from user to delete foir removing node 
    data = int(input("Enter the data to remove : "))
    o1.removeNode(data)
    traversal(o1)


