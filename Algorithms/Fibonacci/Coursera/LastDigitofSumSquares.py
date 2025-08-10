def last_digit_of_sum_squares(n:int):
    # Problem: getting the last digit of partial sum Fibonacci number
    
    # pisano period for %10, that it repeats every 60 rounds
    n = n % 60
    if n <= 1:
        return n
    fib_list = [0,1]
    #creating a list of the last digits of the fibonacci
    for i in range(2,n + 1):
        fib_list.append((fib_list[i-1] + fib_list[i-2]) % 10)

    #squarring the values in the list and summing them with finding its last digit
    return sum(x*x for x in fib_list)%10


if __name__ == '__main__':
    n = int(input())
    print(last_digit_of_sum_squares(n))
