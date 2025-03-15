"""
    Implementation of binary search algorithm
"""

from typing import List

def binarySearch(arr : List,item : int) -> int:
    """
        Return +ve index of arr if item in found otherwise return -1
    """
    size = len(arr) 
    s = 0 
    e = size - 1
    while(s <= e):
        mid = (s + e) // 2 
        if(arr[mid] == item):
            return mid 
        elif(item < arr[mid]):
            e = mid - 1
        else:
            s = mid + 1
    return -1 

if(__name__ == "__main__"): 
    arr : list = [1,2,13,18,21,24,4,56,79]
    print(f"Array : {arr}")
    item = int(input("Enter the array to search : "))
    idx = binarySearch(arr,item)
    if(idx != -1):
        print(f"{item} is found at {idx} ")
    else:
        print(f"{item} is found at arr")