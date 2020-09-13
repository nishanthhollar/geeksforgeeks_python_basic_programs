"""Python Program for Fibonacci numbers
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms,
 the sequence Fn of Fibonacci numbers
 is defined by the recurrence relation
Fn = Fn-1 + Fn-2
with seed values

   F0 = 0 and F1 = 1."""


#program1---Using Dynamic Programming
#inputs
n = int(input("Enter the number till the fibonacci should be  calculated: "))

def Fibonacci(n):
    if(n<0):
        print("Cannot find fibonaci number for such values: ")

    elif(n==1):
        print(0)
    else:
        a = 0
        b = 1
        print(a)
        print(b)

        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)
Fibonacci(n)






# #program2 --- Using Recursive programming
#
#
# n = int(input("Enter the Fibonacci numbers: "))
#
# def Fib(n):
#     if (n<0):
#         print("Incorrect input")
#     elif(n==1):
#         return 0
#     elif(n==2):
#         return 1
#     else:
#         return Fib(n-1)+ Fib(n-2)
# print(Fib(n))




# #program3 - Using DynamicProgramming with the concept of arrays
#
# # Function for nth fibonacci number - Dynamic Programing
# # Taking 1st two fibonacci nubers as 0 and 1
#
# n = int(input("Enter the numbers: "))
# FibArray = [0,1]   #using the array concept
# def Fibonacci(n):
#     if(n<0):
#         print('Incorrect input!!')
#     elif(n<=len(FibArray)):
#         return FibArray[n-1]
#     else:
#         temp_fib = Fibonacci(n-1)+Fibonacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib
#
# print(Fibonacci(n))







#program4 - Space # OPTIMIZE:
#Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
  #same code as in the 1st program of this project
