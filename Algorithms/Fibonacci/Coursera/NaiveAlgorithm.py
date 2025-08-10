# This is the naive algorithm to compute fibonacci(straight forward)
# super slow
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
## For testing and assignment in coursera
if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci(input_n))
