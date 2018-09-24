num = int(input("enter the number of rows"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
num = int(input("enter the number of rows"))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()
a=9
for i in range(1,10,2):
    print(' '*a+i*'*')
    a=a-1
str="*"
for i in range(1,6):
    for j in range(i,i+1):
        print (str.rjust(5," "))
        str=str+"*"
for i in range(0,5):
    print(" "*(i+1)+"*"*(5-i))
a=1
for i in range(1,6):
    print(" "*(5-i)+"*"*a)
    if a<10:
        a+=2

a=7
for i in range(1,5):
    print(" "*i+"*"*a)
    a-=2
