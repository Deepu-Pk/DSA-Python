"""
    Stack data structure using linked list
"""

from typing import Any

class Stack:
    # Node definition 
    class Node:
        def __init__(self,data : Any):
            self.data = data 
            self.next = None 
    
    def __init__(self):
        self.head = None 
    
    def empty(self) -> bool: 
        """
            Return true if stack is empty
        """
        return self.head == None 
    
    def push(self,data : Any) -> None: 
        """
            Push data into stack 
            Args :
                data (Any) : data to push into stack
        """
        # Create temporary node 
        temp = self.Node(data) 
        # push into stack 
        temp.next = self.head 
        self.head = temp 
    
    def pop(self) -> None: 
        """
            Pop data from stack 
        """
        #check stack is empty or not 
        if(self.empty()):
            raise Exception("Stack is empty can pop data from stack") 

        # Pop data from top of the stack 
        temp = self.head 
        self.head = self.head.next 
        del temp 

    def top(self) -> Any: 
        """
            Return top data from stack
        """ 
        # Check stack is empty or not 
        if(self.empty()):
            raise Exception("Stack is empty")
    
        # Return top data 
        return self.head.data


if(__name__ == "__main__"):
    s = Stack() 
    arr : list = [1,2,3,4,5,6,7,8,9,10]
    # Push all data from arr into stack
    for x in arr:
        s.push(x)
    
    # Displaty all elements from stack 
    while(not s.empty()):
        print(s.top(),end = ",")
        s.pop()