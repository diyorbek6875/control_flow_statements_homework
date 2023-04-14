def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """

    if a>0 and a%2==0:
        d="positive even number "
    if a>0 and a%2==1:
        d="positive odd number "
    if a<0 and a%2==0:
        d="negative even number "
    if a>0 and a%2==1:
        d="negative odd number "

    return d
a=int(input("son kirit "))
print(main(a))