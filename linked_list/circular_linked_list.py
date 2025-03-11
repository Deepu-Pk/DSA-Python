"""
    Circular linked list data structure 
"""
from typing import Any

class circularLinkedList:
    # Node structure
    class Node: 
        def __init__(self,data : Any):
            self.data = data 
            self.next = None
            
    def __init__(self):
        self.__head = None 
        self.__tail = None 
        self.__count = 0

    def empty(self) -> bool: 
        """
            Return True if circular linked list empty
        """
        return self.__head == None and self.__tail == None 

    def addNode(self,data : Any,index = -1) -> None: 
        """
            Add new node into circular linked list
        
        """



        # Create new node 
        new_node = self.Node(data) 
        if(new_node is None):
            raise MemoryError("Can not crate new node beacause memory is full")
        # Add new node into empty circular linked list
        if(self.empty()):
            new_node.next = new_node 
            self.__head = self.__tail = new_node
        # Add new node into at tail of the circular linked list 
        elif(index == -1):
            self.__tail.next = new_node 
            self.__tail = new_node
            self.__tail.next = self.__head
        # Add new node into at head of the circular linked list
        elif(index == 0): 
            new_node.next = self.__head 
            self.__head =  new_node 
            self.__tail = self.__head
        else: 
            prev_node = self.__head 
            curr_node = self.__head.next
            count = 1 
            while((curr_node != self.__head) and (count < index)):
                prev_node = curr_node 
                curr_node = curr_node.next 
                count += 1 
            if(curr_node != self.__head):
                prev_node.next = new_node 
                new_node.next = curr_node

        self.__count += 1

    def removeNode(self,data : Any) -> None:
        """
            Remove node for single linked list
        """ 
        if(self.empty()):
            raise NotImplementedError("Circular linked list is empty can not remove any node")
        
        # If node is head node
        if(self.__head.data == data):
            # If circular linkd list have only node 
            if(self.__head == self.__tail):
                node = self.__head 
                self.__head = self.__tail = None 
            else:
                node = self.__head 
                self.__head = self.__head.next 
                self.__tail.next = self.__head 
            del node
        
        else: 
            prev_node = self.__head 
            curr_node = self.__head.next 
            while(curr_node != self.__head):
                if(curr_node.data == data): 
                    prev_node.next = curr_node.next
                    if(curr_node == self.__tail):
                        self.__tail = prev_node 
                    del curr_node
                    break
                prev_node = curr_node
                curr_node = curr_node.next
        self.__count = self.__count - 1

    def search(self,data : Any) -> Node:
        # Check data is head node 
        curr_node = self.__head
        idx = 0 
        while(idx < self.__count):
            if(curr_node.data == data):
                return curr_node 
            curr_node = curr_node.next 
            idx += 1
        return None


    def __iter__(self):
        
        node = self.__head
        idx = 0 
        while idx < self.__count: 
            yield node 
            node = node.next
            idx += 1



if(__name__ == "__main__"):
    o1 = circularLinkedList()
    arr : list = [1,2,3,4,5]
    for x in arr:
        o1.addNode(x)
    
    print(f"Circular linked list : {[node.data for node in o1]}")
    data  = int(input("data to insert circular linked list : "))
    idx = int(input("Index position of data : "))
    o1.addNode(data,idx)
    print(f"Circular linked list addinf new data {data} at postion  {idx} : {[node.data for node in o1]}")
    data = int(input("Enter the data to delete "))
    o1.removeNode(data)
    print(f"Circular linked list after delete a node : {[node.data for node in o1]}")
    data = int(input("Enter the data to search : "))
    node = o1.search(data)
    print(f"Node address of data : {node}")