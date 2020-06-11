def middle_4_digits(i):
	s = str(abs(i))
	length = len(s)
	assert length >= 4 and length % 2 == 0 ,"Need 0 >= 4 even digits" #2nd security haha
	midl = length // 2
	return s[midl-2:midl+2]
x=int(input("Enter any even value greater than 4 :: "))
m=len(str(x))
n= m % 2
if (m<4 or n==1):
    print("Error")
else:
    print(middle_4_digits(x))
