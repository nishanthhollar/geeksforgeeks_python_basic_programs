"""Python Program for How to check if a given number is Fibonacci number?
Given a number \’n\’, how to check if n is a Fibonacci number.
 First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ..

Examples :
Input : 8
Output : Yes

Input : 34
Output : Yes

Input : 41
Output : No
Following is an interesting property about Fibonacci numbers
that can also be used to check if a given number is Fibonacci or not.
A number is Fibonacci if and only if one or both of (5*n2 + 4)
or (5*n2 – 4) is a perfect square (Source: Wiki)."""


#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square


# #program1
# import math
#
#
# #function that returns true if x is a perfect isPerfectSquare
# def isPerfectSquare(x):
#     s = int(math.sqrt(x))
#     return (s*s==x)
#
# #returns true if n is Fibonacci else false
# def isFibonacci(n):
#      # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
#     # is a perferct square
#     return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
#
# #a utility function to check the above functions
# for i in range(1,11):
#     if(isFibonacci(i) == True):
#         print(i, " is a fibonacci number")
#     else:
#         print(i, "is not a fibonacci number")


# #program2 to find squuare root of a number
# import math
#
# def isPerfectSquare(x):
#     s = int(math.sqrt(x))
#     return (s*s == x)
# print(isPerfectSquare(20))




#program3 desired program  
import math
n = int(input("Check if the number is fibonacci or not: "))
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return (s*s == x)

def isFibonacci(n):
    return isPerfectSquare(5*n*n - 4) or isPerfectSquare(5*n*n +4)
if (isFibonacci(n) == True):
    print("Yes")
else:
    print("No")
