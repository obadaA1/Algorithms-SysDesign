def EuclideGCD(a: int, b: int):
    # fall back 
    if b == 0:
        return a
    else:
        return EuclideGCD(b, a % b)
