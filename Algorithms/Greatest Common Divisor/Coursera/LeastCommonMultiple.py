def least_common_multiple(a:int,b:int):
    #there is a relationship between gcd and lcm
    #lcm = (a*b)/gcd(a,b)
    
    return (a*b)//euclidean_gcd(a,b)
# For assignment purposes, I will not import gcd but will implement it here
def euclidean_gcd(a: int, b: int):
    # fall back 
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(least_common_multiple(a, b))

