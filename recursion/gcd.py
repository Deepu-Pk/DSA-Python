
def gcd(a : int, b : int) -> int: 
    """
        Return greated common divisor a and b 
    """
    # Base condition
    if(b == 0):
        return a
      
    # Recursive condition
    return gcd(b,a % b) 



a = int(input("Enter the number : "))
b = int(input("Enter the number : ")) 

print(f"Greatest commmon divisir of {a} and {b} is {gcd(min(a,b),max(a,b))}")

