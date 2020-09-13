n = int(input('Enter the age: '))
voting_age  = 18

if(n>=voting_age):
    print("Person is eligible to vote")
else:
    temp = 0
    years_to_wait =  voting_age - n
    print("The number of years the person has to still  wait {0}".format(years_to_wait))
