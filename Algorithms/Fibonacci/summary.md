# Fibonacci Number - summary

## The problem:
given an non negative integer n, compute the fibonacci number, where:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1)+F(n-2)

## Approaches (How to compute it)
### 1- Naive Algorithm 
solved straight as recursive function
### 2- Efficent Algorithm
As in hand written calculation of fibonacci, we only cared about the last 2 numbers to calcualte the nTh fibo. done that by creating a list that will have all the calculated numbers of the fibonacci stored and used to calculate the next number by just fitching the last 2.