"""Python Program for Sum of squares of first n natural numbers
Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55"""


#
# #program1
# #Method 1: O(N) The idea is to run a loop from 1 to n and for each i, 1 <= i <= n, find i2 to sum.
#
#
# def SumOfSquares(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum = sum + (i*i)
#
#     return sum
#
# n = int(input("Enter the numbers to find the sum of squares: "))
# print(SumOfSquares(n))





# #program2 to find the square of first n natural numbers
#
#
# n = int(input("Enter the number to find out the sum: "))
# def SquareOfSums(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum+ (i*i)
#     return sum
# print(SquareOfSums(n))



#program3
"""Method 2: O(1)
Sum of Squares of first N natural Number = (N*(N+1)*(2*N+1))/6
For example,
For N=4, Sum = (4*(4+1)*(2*N+1))/6
             =(4*5*9)/6
             = 180/6
             =30

For N=5, Sum = (5*(5+1)*(2*N+1))/6
             = (5*6*11)/6
             = 55

Proof:

We know,
(k + 1)3 = k3 + 3 * k2 + 3 * k + 1
We can write the above identity for k from 1 to n:
23 = 13 + 3 * 12 + 3 * 1 + 1 ......... (1)
33 = 23 + 3 * 22 + 3 * 2 + 1 ......... (2)
43 = 33 + 3 * 32 + 3 * 3 + 1 ......... (3)
53 = 43 + 3 * 42 + 3 * 4 + 1 ......... (4)
...
n3 = (n - 1)3 + 3 * (n - 1)2 + 3 * (n - 1) + 1 ......... (n - 1)
(n + 1)3 = n3 + 3 * n2 + 3 * n + 1 ......... (n)

Putting equation (n - 1) in equation n,
(n + 1)3 = (n - 1)3 + 3 * (n - 1)2 + 3 * (n - 1) + 1 + 3 * n2 + 3 * n + 1
         = (n - 1)3 + 3 * (n2 + (n - 1)2) + 3 * ( n + (n - 1) ) + 1 + 1

By putting all equation, we get
(n + 1)3 = 13 + 3 * Σ k2 + 3 * Σ k + Σ 1
n3 + 3 * n2 + 3 * n + 1 = 1 + 3 * Σ k2 + 3 * (n * (n + 1))/2 + n
n3 + 3 * n2 + 3 * n = 3 * Σ k2 + 3 * (n * (n + 1))/2 + n
n3 + 3 * n2 + 2 * n - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n2 + 3 * n + 2) - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n + 1) * (n + 2) - 3 * (n * (n + 1))/2 = 3 * Σ k2
n * (n + 1) * (n + 2 - 3/2) = 3 * Σ k2
n * (n + 1) * (2 * n + 1)/2  = 3 * Σ k2
n * (n + 1) * (2 * n + 1)/6  = Σ k2




#MEthod O(1)
Avoiding early overflow:
For large n,
 the value of (n * (n + 1) * (2 * n + 1)) would overflow.
We can avoid overflow up to some extent using the fact that n*(n+1) must be divisible by 2.
"""
n = int(input("Enter the Number to find the squares of the number: "))
def MyMethod(n):
    return (n*(n+1)*(2*n+1))//6) #function or the formula to find the squares of the numbers

print(MyMethod(n))
