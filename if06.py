def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x = 0
    if a>0:
        x=x+1
    if b>0:
        x=x+1
    if c>0:
        x=x+1
    y=0
    if a<0:
        y=x+1
    if b<0:
        y=x+1
    if c<0:
        y=x+1

    if x>y:
        l=str("there a lot of positive numbers ")
    if x<y:
        l=str("tere are a lot of negative numbers ")
    return l
a=int(input("sonni kirit  "))
b=int(input("sonni kirit  "))
c=int(input("sonni kirit  "))
print(main(a,b,c))
