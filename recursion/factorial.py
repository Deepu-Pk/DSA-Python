"""
    Calculate the factorial of a number using recursion method
"""


def factorial(n : int) -> int: 
    """
        Return factorial of given number 
        Args :
            n (int) : input integer for calculating the factorial
        Return :
            Factorial of a given number 
    """

    # Base condtion
    if((n == 0) or (n == 1)): 
        return 1 
    
    # Recursive case
    return n * factorial(n-1) 


n = int(input("Enter the number : "))
print(f"Factorail of number : {factorial(n)}")