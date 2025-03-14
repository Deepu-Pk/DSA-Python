"""
    Max heap data structure
"""

class maxHeap:
    def __init__(self):
        self.__heap = [1]

    def __heapify(self,idx : int) -> None: 
        left_idx = idx * 2 
        right_idx = left_idx + 1 
        max_idx = idx
        last_idx = len(self.__heap) - 1 
        if((left_idx <= last_idx) and (self.__heap[idx] < self.__heap[left_idx])):
            max_idx = left_idx 
        if((right_idx <= last_idx) and (self.__heap[max_idx] < self.__heap[right_idx])):
            max_idx = right_idx 
        if(max_idx != idx):
            self.__heap[idx],self.__heap[max_idx] = self.__heap[max_idx],self.__heap[idx]
            self.__heapify(max_idx) 
    
    def empty(self) -> bool: 
        """
            Return true if max heap is empty
        """
        return len(self.__heap) == 1 
    
    def push(self,data : int) -> None: 
        """
            Push data into max heap
        """
        self.__heap.append(data) 
        idx = len(self.__heap) - 1 
        parent_idx = idx // 2 
        while((idx > 1) and (self.__heap[parent_idx] < self.__heap[idx])):
            self.__heap[parent_idx],self.__heap[idx] = self.__heap[idx],self.__heap[parent_idx]
            idx = parent_idx 
            parent_idx = idx // 2 
    

    def pop(self) -> None: 
        """
            Pop the data from min heap
        """
        # Assign last value into first index value 
        self.__heap[1] = self.__heap[-1] 
        # Pop last element 
        self.__heap.pop() 
        # Apply heapify algorithm 
        self.__heapify(1)

    def getMax(self) -> int:
        """
            Return maximum from max heap
        """
        return self.__heap[1]
    

if(__name__ == "__main__"):
    # Object for macx heap 
    o1 = maxHeap() 
    # Array of integers 
    arr : list = [6,4,7,9,1,3,2,10,78,34,12]
    # Insert all elements from arr into max heap 
    for x in arr: 
        o1.push(x) 
    
    # Get max and element and pop it 
    while(not o1.empty()):
        print(o1.getMax(),end = " ")
        o1.pop()