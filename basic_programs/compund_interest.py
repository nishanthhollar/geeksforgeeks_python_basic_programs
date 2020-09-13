"""Formula to calculate compound interest annually is given by:

Compound Interest = P(1 + R/100)to the power r
Where,
P is principle amount
R is the rate and
T is the time span"""


"""Compound interest is the addition of interest to the principal sum of a
 loan or deposit, or in other words, interest on interest.
  It is the result of reinvesting interest,
  rather than paying it out, so that interest in the next period
  is then earned on the principal sum plus previously-accumulated interest.
  Compound interest is standard in finance and economics."""


 #program1
#input
principle = int(input("Enter the amount: "))
rate = input("Enter the rate of interest: ")
time = int(input("Enter the time: "))


#operation
compound_interest = principle* ( ( 1+ float(rate)/100 )**time)
print("The compound interest is: {0}".format(compound_interest))

# #program2
# # Python3 program to find compound
# # interest for given values.
# def compound_interest(principle, rate, time):
#     CI = principle*(pow(1+rate/100, time))
#     print("The compound interest is: {0}".format(CI))
#
# #driver code
# compound_interest(10000, 10.25, 5)
