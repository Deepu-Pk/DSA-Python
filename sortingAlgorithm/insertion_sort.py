"""
    Implementation of insertion sort algorithm
"""


def insertionSort(arr : list) -> None:
    total = len(arr) 
    for i in range(1,total):
        item = arr[i] 
        idx = i - 1 
        while((idx >= 0) and (arr[idx]) > item):
            arr[idx + 1]  = arr[idx] 
            idx = idx - 1 
        arr[idx+1] = item 


if(__name__ == "__main__"):
    arr : list = [5,4,6,3,7,2,8,1,9,10]
    print(f"Array before sorting : {arr}")
    insertionSort(arr)
    print(f"Array after sorting : {arr}")