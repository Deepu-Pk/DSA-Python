"""
    Build min heap data structure 
"""


class minHeap:
    def __init__(self):
        self.__heap = [1] 


    def __heapify(self,idx : int ) -> None:
        """
            Heapify algorithm
        """
        left_idx = idx * 2 
        right_idx = left_idx + 1
        min_idx = idx 
        last_idx = len(self.__heap) - 1 
        if((left_idx <= last_idx) and (self.__heap[left_idx] < self.__heap[idx])):
            min_idx = left_idx 
        if((right_idx <= last_idx) and (self.__heap[right_idx] < self.__heap[min_idx])):
            min_idx = right_idx 

        if(idx != min_idx): 
            self.__heap[min_idx],self.__heap[idx] = self.__heap[idx],self.__heap[min_idx]
            self.__heapify(min_idx)


    def  empty(self) -> bool:
        """
            Return true if min_heap is empty
        """
        return len(self.__heap) == 1
    
    def push(self,data : int) -> None: 
        """
            Insert new data into min heap
        """
        self.__heap.append(data)
        idx = len(self.__heap) - 1 
        parent_idx = idx // 2 
        while((idx > 1) and (self.__heap[parent_idx] > self.__heap[idx])):
            self.__heap[parent_idx],self.__heap[idx] = self.__heap[idx],self.__heap[parent_idx]
            idx = parent_idx 
            parent_idx = idx // 2 


    def pop(self) -> None: 
        """
            Remove node from min heap
        """ 
        # Swap first and last element in min heap 
        self.__heap[1] = self.__heap[-1] 
        # Pop last element from min heap 
        self.__heap.pop() 
        # Apply heapify algorithm for making min heap 
        self.__heapify(1) 


    def min(self) -> int:
        """
            Return minimum data from min heap
        """ 
        return self.__heap[1]
    

    
if(__name__ == "__main__"):
    # Object for min heap
    o1 = minHeap() 
    arr : list = [6,5,7,8,9,4,3,10]
    #Insert all elements from arr into min heap 
    for x in arr: 
        o1.push(x) 

    # Print all minimum elements from heap and pop it 
    while(not o1.empty()):
        print(o1.min(),end = " ") 
        o1.pop()
