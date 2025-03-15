"""
    Implementation of bubble sort algorithm
"""
from typing import List 

def bubbleSort(arr : List): 
    total = len(arr) 
    for i in range(total):
        flag : bool = True
        for j in range(0,total-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                flag = False 
        if(flag):
            break 



if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,2,8,1,9,10]
    print(f"Array before sort : {arr}")
    bubbleSort(arr) 
    print(f"Array after sort : {arr}")
        