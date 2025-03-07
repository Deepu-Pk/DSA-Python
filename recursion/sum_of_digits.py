

def sumOfDigitsHelper(sum : int,n : int) -> int:
    """
        calculate the sum of digits in recursive manner
    """
    # Base condition
    if(n <= 0 ): 
        return sum
    # calculate reminder of given n 
    rem = n % 10 
    # Add reminider in total sum
    sum += rem 
    # Remove last digit from n 
    n //= 10 
    # Recursive call 
    return sumOfDigitsHelper(sum,n)


def sumOfDigits(n : int) -> int: 
    """
        Return sum of all digits of given number 
        Args : 
            n (int) :  input number to calculate the sum of digits
    """

    # Define intial sum
    sum : int = 0 
    # Helper funtion for calculating the sum of digits in recursive version
    return sumOfDigitsHelper(sum,n) 

n = int(input("Enter the number : "))
print(f"sum of digits : {sumOfDigits(n)}")
