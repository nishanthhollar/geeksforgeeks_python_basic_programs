'''Given a number x,
determine whether the given number is Armstrong number or not.
 A positive integer of n digits is called
 an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... '''

# #program1 incomplete program tryout
# #input
# num = input("Enter the armstrong number: ")
#
# def check_armstrong(num):
#     for ch in num:
#         ch = int(ch)
#         sh = pow(ch,3)
#         print(ch)
#         print(sh)
#
# check_armstrong(num)
#
# digit = input("Enter the digits: ")
# def power(a, n):
#     res = pow(a,n)
#     print(res)
#     if (a == res):
#         print("Yes it is armstrong number")
#     else:
#         print("It is not armstrong")
# power(1,3)



#program2
# #input
# num = int(input("Enter a Armstrong number:"))
# temp = num
# sum = 0
#
# #operation
# while temp>0:
#     digit = temp%10
#     sum+= pow(digit, 3)
#     temp//=10
# if (num==sum):
#     print("{0}".format(sum))
#     print("Yes, it is an armstrong number")
# else:
#     print("{0}".format(sum))
#     print("NO, it is not an armstrong number")




program3
num = int(input("Enter the armstrong number: "))
temp = num
sum = 0
while temp>0:
    digit = temp%10
    sum+= pow(digit, 3)
    temp//=10
if(num==sum):
    print("{0}".format(sum))
    print("Yes, it is an Armstrong number")
else:
    print("{0}".format(sum))
    print("No, it is not armstrong number")
