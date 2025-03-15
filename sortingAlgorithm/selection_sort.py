"""
    Implementation of selection sort algorithm
"""


from typing import List

def selectionSort(arr : List): 
    total = len(arr)
    for i in range(total):
        min_idx = i
        for j in range(i,total):
            if(arr[j] < arr[min_idx]):
                min_idx = j 
        if(min_idx != i):
            arr[min_idx],arr[i] = arr[i],arr[min_idx]


if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,2,8,1,9,10] 
    print(f"Array before sort : {arr}")
    selectionSort(arr) 
    print(f"Array after sort : {arr}")