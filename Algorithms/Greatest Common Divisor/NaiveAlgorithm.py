def naiveGCD(a: int, b: int):
    gcd = 0
    # starting from 1 so wont devide over 0, and will return the gcd
    for d in range(1, a+b):
        if a%d == 0 and b%d ==0:
            gcd = d
    return gcd