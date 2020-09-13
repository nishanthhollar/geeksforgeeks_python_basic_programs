'''Python program to print all Prime numbers in an Interval
Given two positive integer start and end.
The task is to write a Python program toprint all Prime numbers in an Interval.

Definition: A prime number is a natural number greater than 1
 that has no positive divisors other than 1 and itself.
 The first few prime numbers are {2, 3, 5, 7, 11, ….}.
The idea to solve this problem is to iterate the val from start to end using
a for loop and for every number, if it is greater than 1,
 check if it divides n. If we find any other number which divides,
 print that value.'''

# #program1
# #input
# start = int(input("Enter the lower interval: "))
# end = int(input("Enter the upper interval: "))
# def calculate_interval(start, end):
#     for val in range(start, end+1):
#             if(val>1):
#                 for number in range(2, val):
#                     if(val%number == 0):
#                         break
#                 else:
#                     print(val)
# #Driver code
# interval = calculate_interval(start, end)



#program2
lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))

def calculate_interval(lower,upper):
    for num in range(lower, upper+1):
        if(num>1):
            for number in range(2, num//2):
                if(num%number == 0):
                    break

            else:

                print(num)
calsi = calculate_interval(lower, upper)
