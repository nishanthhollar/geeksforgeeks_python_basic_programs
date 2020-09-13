"""Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate"""

#program1
# #input
# principle = int(input("Enter the principle: "))
# time = int(input("Enter the time: "))
# rate = int(input("enter the rate of interest: "))
#
# #operation
# simple_interest = (principle * time *rate)//100
#
# #output
# print("The simple interest is {0}".format(simple_interest))




#program2
def SI(p, t, r):
    si = (p*t*r)/100
    return si

print(SI(3000,7,1))
