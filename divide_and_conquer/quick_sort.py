"""
    Implemen tation of quick sort algorithm
"""

from typing import List

def partition(arr : List,s : int, e : int) -> int:
    j = s - 1  
    p = e 
    for i in range(s,e):
        if(arr[i] < arr[p]):
            j = j + 1 
            arr[i],arr[j] = arr[j],arr[i] 
    
    j = j + 1 
    arr[p],arr[j] = arr[j],arr[p]
    return j
    

def quickSort(arr : List,s : int,e : int) -> None:
    if(s > e):
        return 
    p = partition(arr,s,e)
    quickSort(arr,s,p-1) 
    quickSort(arr,p+1,e)

if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,2,8,1,9,10]
    print(f"Array before sort : {arr}")
    s = 0 
    e = len(arr) - 1
    quickSort(arr,s,e)
    print(f"Array after sort : {arr}")