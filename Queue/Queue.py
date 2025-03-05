from typing import Any 

class Queue: 
    # Define Node 
    class Node:
        def __init__(self,data : Any):
            self.data = data 
            self.next = None 
    
    def __init__(self):
        self.head = None 
        self.tail = None 

    def empty(self) -> bool: 
        """
            Return true if queue is empty  
        """
        return (self.head == None) and (self.tail == None) 
    
    def push(self,data : Any) -> None:
        """
            Push data into queue 
            Args :
                data (Any) : data to push queue
        """

        # create node for data 
        temp = self.Node(data) 
        if(temp == None):
            raise MemoryError("Queue is full can not push data into queue") 
        
        # Insert data into queue 
        if(self.empty()):
            self.head = self.tail = temp 
        else: 
            self.tail.next = temp 
            self.tail = temp 
    
    def pop(self) -> None: 
        """
            Pop data from queue
        """
        # check queue is empty or not 
        if(self.empty()):
            raise MemoryError("Queue is empty can  not pop the data from queue")
        
        # Pop data from queue 
        temp = self.head 
        if(self.head ==  self.tail):
            self.head = self.tail = None 
        else: 
            self.head =  self.head.next 
        
        del temp 
    
    def front(self) -> Any: 
        """
            Return front of the queue
        """
        #Check queue is empty or not 
        if(self.empty()):
            raise MemoryError("Queue is empty can not return front data from queue")
        
        return self.head.data   
    

if(__name__ == "__main__"):
    q =  Queue() 
    arr : list = [1,2,3,4,5,6,7,8,9,10]
    # Push all data from arr into queue 
    for x in arr: 
        q.push(x) 
    # Print all data from queue 
    while(not q.empty()):
        print(q.front(),end = ",")
        q.pop()