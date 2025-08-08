# Greatest Common Divisor -summary

## Problem
- finding the highest number that divide 2 numbers a,b

## Approaches

### Brute-force / Naive
- scamming through all numbers from 1 to sum of numbers and checking if the number divides

### Euclidean Algorithm (recursive)
- Example
- Let's say a = 26, b = 12: -> remineder will be 2 means a` is 2 >> 
- according to the algorithm we can reduce the number : gcd(a,b) = gcd(a`,b) = gcd(b,a^prime)
can do so by directly finding the reminder of a/b, and putting it in the formula again and again(reduce number) till reminder is 0
last reminder before 0 is the gcd.
