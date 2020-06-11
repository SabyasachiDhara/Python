num1=int(input ("Enter the number who's Table you want :: "))
num2=int(input ("From where you want :: "))
num3=int(input ("How many want :: "))

for i in range (num2,num3+1,1):
    result = num1*i
    print(num1,end=" ")
    print( i,end=" ")
    print( result,end="\n")
