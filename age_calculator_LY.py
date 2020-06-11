from datetime import date  # importing current date


#input from user

name=input('Hey What is your name : ')
byear=int(input('Give Your Birth Year : '))
bmonth=int(input('Give Your Birth month : '))
bday=int(input('Give Your Birth day : '))



# Calculation age

toyear = date.today().strftime('%Y')
year = int(toyear) - byear

tomonth = date.today().strftime('%m')
month = int(tomonth) - bmonth

if month <= 0:
    year = year - 1
    month = (int(tomonth) + 12) - bmonth  # in case, when value of birth month is greater than current month

today = date.today().strftime('%d')
day = int(today) - bday

#Month's day error check
if day <= 0:
    month = month - 1
    if int(tomonth) in (1,3,5,7,8,10,12) :
        day = (int(today) + 31) - bday  # after subtraction if the result come in negative, then the condition execute
    elif tomonth == 2:
        day = (int(today) + 28) - bday  # after subtraction if the result come in negative, then the condition execute
    else:
        day = (int(today) + 30) - bday  # after subtraction if the result come in negative, then the condition execute
    
    




#Leapyear
d = 0

def leapyear(num):

    return ((num % 4 == 0) and (num % 100 != 0) or (num % 400 == 0));

for i in range (byear,int(toyear) + 1, 1):
    
      d = d+1 if (leapyear(i))else d+0

day = day+d

#overflow

if day > 30:
    month += day//30
    day = day%30
if month >= 12:
    year += month//12
    month = month%12


    

print('\nHey '+name+', your are ',end='')
print(year, end=' ')
print('years', end=' ')
print(month, end=' ')
print('months', end=' ')
print(day, end=' ')
print('days', end=' ')
print('old. \n')

