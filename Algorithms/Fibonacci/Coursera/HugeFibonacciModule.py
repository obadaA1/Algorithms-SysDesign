def huge_fibonacci_number(n: int, m: int):
    # Problem: returning huge fibonacci number modulo m
    pisano_period = get_pisano_period(m)
    n = n % pisano_period
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current


#I will use pisano method to solve this
def get_pisano_period(m):
    # Pisano period repeats when the sequence (0, 1) reappears
    previous,current = 0,1
    for i in range(m*m):
        previous,current = current, (previous+current)%m
        # checking sequence occurance
        if previous ==0 and current ==1 :
            return i+1
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(huge_fibonacci_number(n, m))
