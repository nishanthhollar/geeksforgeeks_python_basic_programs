# '''Factorial of a non-negative integer, is multiplication of all integers smaller
#  than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.'''
#
 #calculate the factorial of a number
# def factorial(n):
#
#
#      #single line to find the factorial
#      return 1 if (n==1 or n ==0) else n *factorial(n-1);
# #Driver code
# num = 5
# print("Factorial of a",num,"is",factorial(num))



# #calculate the  factorial of a number
# def factorial(n):
#
#
#     #single line to find the factorial
#     return 1 if (n==1 or n == 0) else n*factorial(n-1)
# #driver code
# num = int(input("Enter the number to find the factorial: "))
# print("Factorial of the {0} is: ".format(num),factorial(num))





# #alternate approach or iterative
# def factorial(n):
#     if n<0:
#         return 0
#     elif n == 0 or n ==1:
#         return 1
#     else:
#         fact = 1
#         while(n>1):
#             fact*= n
#             n -=1
#         return fact
#
# #Driver code
# num = int(input("Enter the number:"))
# print("Factorial of {0}: ".format(num),factorial(num))



# def fact(n):
#     return 1 if (n==0 or n==1) else n*fact(n-1)
#
# print(fact(10))


#iterative approach
def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while n>1:
            fact = fact*n #code is used to multiply fact and n
            n = n-1 #code is used to decrease the counter for while loop
        return fact
n = int(input("enter the number:"))
print(fact(n))
