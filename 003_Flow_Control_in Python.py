In Python Programming, we have 3 types of flow control statements:

1. Conditional/Selection Statement (IF / IF ELIF)
2. Looping Statement (WHILE / FOR )
3. Misc Flow Control Statement (break / continue)

#Conditional Statement
##############################################

#bigex
print("Enter First Number :")
a= int(input())
print("Enter Second Number :")
b= int(input())
print("Enter Third Number :")
c= int(input())

if(a==b==c):
    print("All are Equal")
elif(a>b and a>c):
    print("A is the greatest")
elif(b>a and b>c):
    print("B is the greatest")
else:
    print("C is the greatest")

#Prg to decide whether the number is positive or negative
a= int(input("Enter an integer value :"))
if(a == 0):
    print("Enter Integer other than Zero")
elif(a>0):
    print("A is positve")
else:
    print("A is negative")

#EvenOdd
a = int(input("Enter an integer : "))
if(a%2==0):
    print("{} is even number".format(a))
else:
    print("{} is odd number".format(a))

# Ticket
a = str(input("Do u have ticket? :"))
b = a.lower()
if(b =='yes'):
    print("Enter the Hall")
    print("Watch Movie")
    print("Leave hall")
elif(b=='no'):
    print("Go Home and enjoy the day better than movie hall")
else:
    print("pls enter valid input")

#Looping Statement
##############################################

# 1__WHILE LOOP

#MULTABLE
a= int(input("Enter an Integer : "))
if(a<=0):
        print("number is invalid")
else:
    i=1
    print("_"* 30)
    while(i<=10):
        print("{} * {} = {}".format(i,a,i*a))
        i=i+1
print("_"*30)

#sqcubesum
a= int(input("Enter an number: "))

if(a<=0):
    print("number is invalid")
else:
    i=1
    while(i<=a):
        sq= i**2
        cube=i**3
        sum = i + sq + cube
        #print("_"*30)
        print("square is {}, cube is {}, sum is {}".format(sq,cube,sum))
        i=i+1
print("_"*30)

# While example 1
n = int(input("Enter any value: "))

if (n <= 0):
    print("number  is invalid")
else:
    i = 1
    while (i <= n):
        print(i)
        i = i + 1

#While example 2
n= int(input("Enter any value: "))
if(n<=0):
    print("number  is invalid")
else:
    i=n
    while(i>=1):
        print(i)
        i=i-1

#Factorials
n = int(input("Enter any number : "))
if(n<=0):
    print("Number is invalid")
else:
    i=1
    s=1
    while(i<=n):
       s=s*i
       i=i+1
    print("Factorial of {} is {}".format(n,s))

#palindrome
n = int(input("Enter any number : "))
if(n<=0):
    print("Number is invalid")
else:
    y=n
    s=0
    while(n>0):
        x =n%10
        s= s*10 + x
        n=n//10
if(y==s):
    print("Number is palindrome")
else:
    print("Number is not an palindrome")

#Reverse
n = int(input("print any number : "))\
if(n<=0):
    print("Number is Invalid")
else:
    s=n
    q=0
    123
    while(n>0):
        p = n%10
        q = q*10 + p
        n = n//10
if(s==q):
    print("{} is reversal :{}".format(s,q))
else:
    print("{} is not reversal :{}".format(s,q))

#Miscellaneous Control Statement
#break
#break is an keyword and it is used for terminating the execution of the loop.

s='PYTHON'
for ch in s:
    if(ch == 'Y'):
        break
    else:
        print(ch)

###########################################
lst= [67,10,20,34,12,56,78,34,67]
print(lst,type(lst))
print("List : ",lst)

for val in lst:
    if(val==20):
        break
    else:
        print(val)
###########################################


#Example of "break" & "continue" statement
###########################################

s= 'PYTHON'
for val in s:
    print(val)
print("#" *10, "break Example")
for val in s:
    if(val=='H'):
        break
    print(val)
print("#" *10, "Continue Example")
for val in s:
    if(val =="T" or val =="H"):
        continue
    print(val)

#Nested Looping  Example

for i in range(1,6):
    print("Value in outer loop : ",i)
    j=1
    while(j<4):
        print("Inner loop: ",j)
        j= j+1


#Armstrong Number
n = int(input("Enter any number : "))
if(n<=0):
    print("Number is invalid")
else:
    s=0
    d=n
    while(n>0):
        p= n%10
        s= p**3 + s
        n=n//10
if(d==s):
    print("{} is an armstrong number".format(d))
else:
    print("{} is not an armstrong number".format(d))

#listPrimeNumber
n=int(input("Enter any number : "))
if(n<=1):
    print("Invalid Number")
else:
    for i in range(2,n-1):
        if(n%i == 0):
            V = False
            break
        else:
            V = True
if(V==True):
    print("{} is Prime Number".format(n))
else:
    print("{} is not an Prime Number".format(n))


