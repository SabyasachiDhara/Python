import xlrd
import openpyxl

check={'admin'}

wb = xlrd.open_workbook(r'database.xlsx')
xfile = openpyxl.load_workbook(r'database.xlsx')

sheet1 = xfile['Sheet1']
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(sheet.nrows):
    imp=sheet.cell_value(i,0)
    check.add(imp)

l = len(check)
p='A'+str(l)
e={'exit','Exit'}
name = input('\nWhat is your name :: ')

def welcome(n):
    if n in check:
        print ('\nWelcome Home..')
    else:
        print ('\n\n!!!!...Invalid user...!!!!')
        print ('\nPlease Sign in First, Then Try..')
        sign=input("\nAre you want to Sign In(Yes/No) :: ")
        if sign in ('no','No','NO'):
            print("\nThanks!! Come Again.")
        elif sign in  ('yes','Yes','YES'):
            newname=input("\nEnter your name (If you don't want then enter exit) :: ")
            if newname in e:
                print ('\nThanks..You Always Welcome ')
            elif newname in check:
                print ('\nHey, You already Here !!\n###Enter Again###')
            else:
                conform=input('Are you sure to save (Yes/No):: ')
                if conform in ('no','No'):
                    print ('\nThanks, please start again')
                elif conform in ('Yes','yes'):
                    sheet1[p] = newname
                    xfile.save(r'C:\Users\sabya\Documents\database.xlsx')
                    print('\nEntry Successfull !!!! \n\n....Please Restart....')
                else:
                    print ('###ERROR###')
        else:
            print ('Invalid Entry !!\n####Try Again####')

welcome(name)
