def decimalToBinary(n : int) -> int: 
    """
        Return binary number of given decimal number 
    """
    # Base codition
    if(n == 0): 
        return 0
    #Recursive codition 
    return (n % 2) + (10 * decimalToBinary(n // 2)) 


n = int(input("Enter the number : ")) 
print(f"Binary number of {n} is {decimalToBinary(n)}")