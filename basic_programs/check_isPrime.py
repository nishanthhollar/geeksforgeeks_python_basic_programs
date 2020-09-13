'''Python program to check whether a number is Prime or not
Given a positive integer N.
The task is to write a Python program
to check if the number is prime or not.
Definition: A prime number is a natural number
 greater than 1 that has no positive divisors other than 1 and itself.
  The first few prime numbers are {2, 3, 5, 7, 11, ….}.'''

#   #program1
#   #input
# num = int(input("Enter the number to check if the number is prime or not: "))
# if(num>1):
#         for i in range(2, num):
#             if(num%i == 0):
#                 break
#         else:
#                 print("True")



#program2
'''The idea to solve this problem is to iterate through
all the numbers starting from 2 to (N/2) using
a for loop and for every number check if it divides N.
If we find any number that divides, we return false.
 If we did not find any number between 2 and N/2
 which divides N then it means that N is prime and we will return True.'''

number = int(input("Enter the number to check if it is Prime or Not: "))
def checkIsPrime(number):
    if (number>1):
        for num in range(2, number//2):
            if(number%num == 0):
                print("It is not a prime number",number)
                break
        else:
                print("It is a prime number", number)
    else:
        print("It is neither prime not composite")

isPrime = checkIsPrime(number)
