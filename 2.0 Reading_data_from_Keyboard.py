# Prg to read data from keyboard & multiply them
print("Enter two values")
a= input()
b= input()
print(a,b)
x=float(a)
y=float(b)
z = x*y
print("value of a: {}",format(x))
print("value of b: {}",format(y))
print("value of mult: {}",format(z))

#Program for accepting two values & multiplying them

print("-" * 40)
print("Enter two Integer values")
a= int(input())
b= int(input())
print("-" * 40)
print("Value after Multiplication is :{} * {} = {}".format(a,b,a*b))


#Program for finding simple interest

print("-"*40)
print("Enter Principal Amount : ")
P= float(input())
print("Enter rate of Interest : ")
R =float(input())
if (R<=100) :
    print("Enter Time Period in Year: ")
    T = float(input())
    s1 = (P*R*T)/100
    s2 = P + s1
    print("Amount Payable after {} year of time is {}".format(T,s2))

else:
    print("Pls Provide Valid ROI")



