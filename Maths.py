print("To calculate the factorial of any number")
n = int(input("Enter the value of n: "))
def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)
print (factorial(n))


print("To caculate the average of two numbers")
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
def average(a,b):
    print("The average is",(a+b)/2)
average(a,b)



print("To calculate the square of any number")
a= int(input("Enter the value of a: "))
print("The square of a is",(a*a))



print("To calculate the cube of any number")
a= int(input("Enter the value of a: "))
print("The square of a is",(a*a*a))



print("To calculate total surface area of a Cone")
pai = 3.14
r = int(input("Enter the value of r: "))
h= int(input("Enter the value of h: "))
def volume(r,h):
    print("The volume of the cube is",(1/3*pai*r*r*h))
volume(r,h)
print("To caculate the average of two numbers")



print("To Find the summation of two Limits") 
L=int(input("lower_limit= "))
U=int(input("upper_limit= "))
sum = 0

for REEMA in range(L, U + 1):
  sum += REEMA
print("The sum of numbers from", L, "to", U, "is:", sum)



print("To Find the multiplicatin b/w two numbers")
L=int(input("lower_limit= "))
U=int(input("upper_limit= "))
sum = 1

for Vijay in range(L, U + 1):
  sum *= Vijay
print("The sum of numbers from", L, "to", U, "is:", sum)


