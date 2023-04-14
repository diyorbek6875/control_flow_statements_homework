def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    b=a%10
    c=a//10
    d=b*10+c
    
    if d<a:
        e=True
    if d>a:
        e=False
    
    return e
a=int(input("sonni kiriting "))

print(main(a))