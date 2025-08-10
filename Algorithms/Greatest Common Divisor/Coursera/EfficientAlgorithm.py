def EuclideGCD(a: int, b: int):
    # fall back 
    if b == 0:
        return a
    else:
        return EuclideGCD(b, a % b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(EuclideGCD(a, b))
