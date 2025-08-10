def fibonacci_last_digit(n):
    # pisano period for %10, that it reapeats every 60 rounds
    n = n % 60
    
    #Problem: getting the last digit of large fibonaci number
    if n <= 1:
        return n
    
    previous = 0
    current  = 1
    ## iterating directly and calculating fibonacci number without saving the values in a list, only last number will be returned
    for _ in range(n - 1):
        # as we are interested in the last digit, will directly get it in each iteration with module 10.
        previous, current = current, (previous + current)%10

    return current


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
