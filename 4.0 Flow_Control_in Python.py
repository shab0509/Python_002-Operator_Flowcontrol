In Python Programming, we have 3 types of flow control statements:

1. Conditional/Selection Statement (IF / IF ELIF)
2. Looping Statement (WHILE / FOR )
3. Misc Flow Control Statement (break / continue)

# Inorder to deal with any looping statement, we must use 3 points:
# Intialisation / Condition / Increment

#Conditional Statement
##############################################


#Find the Greatest of three number

n1= int(input("Enter First Number : "))
n2 =int(input("Enter Second Number : "))
n3 =int(input("Enter Third number : "))
if((n1==n2==n3)):
    print("All are Equal")
else:
    if((n1>=n2) and (n1>=n3)):
print("{} is the Greatest".format(n1))
else:
if((n2>=n1) and (n2>=n3)):
    print("{} is the Greatest".format(n2))
else:
    print("{} is the Greatest".format(n3))


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
x = int(input("Enter Any Number :"))
def fact(i):
    f=1
    while(i>=1):
        f=f*i
        i=i-1
    return f

if(x<=0):
    print("Enter Number greater than 0")
else:
    print("_"*20)
    y= fact(x)
    print("Factorial of {} is {}".format(x,y))
    print("_"*20)

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
#Pos-Neg List

n1 = input("Enter list of values seprated by space :")
n2 = list(map(int, n1.split( )))
print(n2,type(n2))
P1,N1 = [],[]

length =len(n2)
print("Length of list is :{}".format(length))
i=0
while(i <= length-1):
    if(n2[i]>0):
        P1.append(n2[i])
        i=i+1
    else:
        N1.append(n2[i])
        i=i+1
print(P1)
print(N1)

#Reverse
n=int(input("Enter Any Number : "))
if(n<=0):
    print("Enter valid Numbers")
else:
    x=n
    i=0
    s=0
    while(n>0):
        i= n%10
        s = s*10 + i
        n=n//10
    print("Reverse of {} is {}".format(x,s))


#sumavg
n= int(input("Enter how many element you want in the list : "))
print("# of element in the list : {}".format(n))

L =list()
print(L)
i=1
while(i<=n):
    val =int(input("Enter number to be entered : "))
    L.append(val)
    i=i+1

print(L)

print("min is :{}".format(min(L)))
print("max is :{}".format(max(L)))
print("sum is :{}".format(sum(L)))
print("len is :{}".format(len(L)))
print("avg is :{}".format(sum(L)/len(L)))

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


