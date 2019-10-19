import math

a=input("enter length")
b=input("enter base")
c=input("enter hypotenuse")
a=float(a)
b=float(b)
c=float(c)

if a==0 or b==0 or c==0:
    print("invalid input")
elif a+b>c and b+c>a and a+c>b:
    perimeter=a+b+c
    s=perimeter/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    # print("the area and perimeter of your triangle is {} and {}".format(area,perimeter))
    print("the area and perimeter of your triangle is %f and %f" %(area,perimeter))
else:
    print("invalid triangle")


