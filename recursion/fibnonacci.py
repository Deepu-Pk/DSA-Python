

def fibonacci(n : int) -> int: 
    """
        Return fibonacci  number of given position 
        Args :
            n (int) : position of number 
        Return :
            Fibonacci number in nth position  
    """
    # Base codition
    if((n == 0) or (n == 1)): 
        return n
    # recursive 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 


n = int(input("Enter the number : "))
print(f"Fibonacci number : {fibonacci(n)}")