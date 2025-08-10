def fibonacci_list(n):
    # Creating an array with initialized 0,1 as these are always the same value
    fib_array = [0,1]
    # Iterating from 2 because the first two Fibonacci numbers (0 and 1) are already initialized
    for i in range(2, n+1):
        fib_array.append((fib_array[i-1] + fib_array[i-2]))
    # Returning the nth Fibonacci number
    return fib_array[n]

## For testing and assignment in coursera
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_list(input_n))
