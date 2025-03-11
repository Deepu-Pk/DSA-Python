"""
    Single linked data structure 
"""

from typing import Any

class SingleLinkedList: 
    class Node: 
        def __init__(self, data  : Any):
            self.data = data 
            self.next = None 

    def __init__(self):
        self.__head = None
        self.__tail = None 
        self.__count = 0
        
    def empty(self) -> bool: 
        """
            Return true if linked list is empty otherwise false 
        """
        return self.__head == None and self.__tail == None
    
    def addNode(self,data : Any,index : int = -1) -> None:
        # Verification location 
        if(index > self.__count):
            raise IndexError("Index is out of boundry") 
        # Create new node 
        temp = self.Node(data) 
        # check temo is None 
        if(temp is None):
            raise MemoryError("Memory is full can not create new node")
        

        # if list is empty  
        if(self.empty()):
            self.__head = self.__tail = temp 
        elif(index == 0): # Add node in head of the linked list
            temp.next = self.__head 
            self.__head = temp 
        elif(index == -1): # Add  node in tail of the linked list
            self.__tail.next = temp 
            self.__tail = temp 
        else: 
            loc = 0 
            curr_node = self.__head 
            prev_node = None 
            while(loc < index):
                prev_node = curr_node
                curr_node = curr_node.next 
                loc += 1 
            prev_node.next = temp 
            temp.next = curr_node 
        self.__count += 1 
    
    def removeNode(self,data : Any) -> None: 
        """
            Remove node from linked list
        """
        # Check data is first node
        if(self.__head == data):
            temp = self.__head 
            if(self.__head == self.__tail):
                self.__head = self.__tail = None 
            else:
                self.__head = self.__head.next  
            del temp 
        
        else: 
            prev_node = self.__head 
            curr_node = self.__head.next 
            while(curr_node is not None):
                if(curr_node.data == data): 
                    prev_node.next = curr_node.next 
                    del curr_node 
                    break 
                prev_node = curr_node 
                curr_node= curr_node.next
    
    def __iter__(self):
        """
            Linked list iteration
        """
        node = self.__head 
        while node: 
            yield node 
            node = node.next  


                        

if(__name__ == "__main__"):
    arr : list = [1,2,3,4,5,6,7]
    o1 = SingleLinkedList() 
    # Push all the data into single linked list 
    for x in arr: 
        o1.addNode(x) 
    # Print all nodes in linked list 
    print(f"Linked list : {[node.data for node in o1]}")

    data = int(input("Enter new node to list : "))
    index = int(input("Enter the index position to insert : "))
    o1.addNode(data,index)
    print(f"SIngle linked list : {[node.data for node in o1]}")