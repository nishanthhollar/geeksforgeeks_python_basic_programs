'''Python Program for n-th Fibonacci number
In mathematical terms,
 the sequence Fn of Fibonacci numbers
  is defined by the recurrence relation
Fn = Fn-1 + Fn-2
with seed values
F0 = 0 and F1 = 1.'''

#dynamic programming means storing of sub answers
#recursive programming is not storing rather repeating the same steps again and again
#program1
n = int(input("Enter the fibonacci number: "))

def fib(n):
    a = 0
    b = 1
    if (n<0):
        print("The number is negative hence fibonacci is not possible💋")
    elif (n == 1):
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)
fib(n)







# #program2 recursive programming
# def fibonacci(n):
#     if n<0:
#         print("Incorrect Input: ")
#         #first fibonacci number is 0
#     elif n==1:
#         return 0
#         #second fibonacci number is 1
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)
#
#     #driver program
# print(fibonacci(9))


# #program3 - recursive programming
# n = int(input("Enter the fib number to find out the nth fibonacci number: "))
# def fib(n):
#     if (n==1):
#         return 0
#     elif (n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print("The",n,"th number of the fibonacci sequence",fib(n))




# #program4 - using dynamic programming
# '''Dynamic Programming is mainly an optimization over plain recursion.
# Wherever we see a recursive solution that has repeated calls for same inputs,
# we can optimize it using Dynamic Programming.
# The idea is to simply store the results of subproblems,
# so that we do not have to re-compute them when needed later.
# This simple optimization reduces time complexities from exponential to polynomial.
# For example, if we write simple recursive solution for Fibonacci Numbers,
# we get exponential time complexity and if we optimize it by storing solutions of subproblems,
# time complexity reduces to linear'''
#
#
# fibArray = [0, 1]
#
# def fibonacci(n):
#     if n<0:
#         print('Incorrect Input!!')
#     elif n<=len(fibArray):   #impt
#         return fibArray[n-1] #impt
#     else:
#         temp_fib = fibonacci(n-1)+fibonacci(n-2)  #important
#         fibArray.append(temp_fib)    #important
#         return temp_fib
#
# n = int(input("Enter the  number: "))
# print(fibonacci(n))





# #program5 -method using dynamic programming and space optimization
#
#
#
# # Function for nth fibonacci number - Space Optimisataion
# # Taking 1st two fibonacci numbers as 0 and 1
#
#
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
# # Driver Program
#
# print(fibonacci(9))
#
