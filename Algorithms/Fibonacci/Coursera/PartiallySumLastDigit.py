def partial_sum_last_digit(m:int,n:int):
    # Problem: getting the last digit of partial sum Fibonacci number
    
    # pisano period for %10, that it repeats every 60 rounds
    m = m % 60
    n = n % 60
    if n <= 1:
        return n
    if n < m:
        n += 60  # handle wrap-around due to modulo
    fib_list = [0,1]
    #creating a list of the last digits of the fibonacci
    for i in range(2,n + 1):
        fib_list.append((fib_list[i-1] + fib_list[i-2]) % 10)

    return sum(fib_list[m:n+1])%10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(partial_sum_last_digit(m, n))
