def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    a<9
    if 99>=a>=10 and a%2==1:
        f="two-digit odd number "
    if 99>=a>=10 and a%2==0:
        f="two-digit even number "
    if 999>=a>=100 and a%2==1:
        f="three digit odd number "
    if 999>=a>=100 and a%2==0:
        f="three digit even number "
    
        

    return f
a=int(input("sonni kirit "))
print(main(a))