"""Area of a circle can simply be evaluated using following formula.
Area = pi * r2
where r is radius of circle """
#
# #program1
# pi = 3.14
# r = input("Enter the radius of a circle: ")
#
# #operation
# area = pi* pow(float(r),2)
# print("Area is %.4f" %area)

#program2
s = input("Enter the radius: ")
r = float(s)
def findArea(r):
    pi = 3.142
    return pi*(r*r)
#driver method
print("Area is %.4f" %findArea(r));
