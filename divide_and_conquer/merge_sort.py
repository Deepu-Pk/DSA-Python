"""
    Implementation of merge sort algorithm
"""
from typing import List


def merge(arr: List,s : int,e : int) -> None:
    """
        Merge to two sorted array
    """
    mid = (s + e) // 2 
    temp_arr : list = []
    i = s 
    j = mid + 1 
    while((i <= mid) and (j <= e)):
        if(arr[i] < arr[j]):
            temp_arr.append(arr[i])
            i = i +1 
        else:
            temp_arr.append(arr[j])
            j = j + 1

    for k in range(i,mid+1):
        temp_arr.append(arr[k]) 
    for k in range(j,e+1):
        temp_arr.append(arr[k])
    

    k = 0
    for i in range(s,e+1):
        arr[i] = temp_arr[k] 
        k = k + 1

def mergeSort(arr : List,s :int, e : int) -> None:
    if(s >= e):
        return 
    
    mid = (s + e) // 2 
    mergeSort(arr,s,mid) 
    mergeSort(arr,mid+1,e)
    merge(arr,s,e)

if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,3,8,2,9,1,10]
    print(f"Array before sort : {arr}")
    s = 0 
    e = len(arr) - 1
    mergeSort(arr,s,e)
    print(f"Arrat after sort : {arr}")