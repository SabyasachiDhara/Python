import xlrd
import openpyxl


checkname={'Admin'}
checkpassword={'abcd12@'}
path = r'zz.xlsx'


wb = xlrd.open_workbook(path)
xfile = openpyxl.load_workbook(path)
sheet1 = xfile['Sheet1']
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)



for i in range(sheet.nrows):
    imp=sheet.cell_value(i,0)
    checkname.add(imp)

for i in range(sheet.nrows):
    imp=sheet.cell_value(i,1)
    checkpassword.add(imp)




nl = len(checkname)+1
pl = len(checkpassword)+1
np='A'+str(nl)
pp='B'+str(pl)
e={'exit','Exit'}
name = input('\nName :: ')




def welcome(n):
    if n in checkname:
        password =(input('\nPassword :: '))
        if password in checkpassword:
            for row in range(sheet.nrows):              #finding Name row
                for col in range(sheet.ncols):
                    if sheet.cell_value(row, col) == name:
                        r1=row
            for row in range(sheet.nrows):              #finding password row
                for col in range(sheet.ncols):
                    if sheet.cell_value(row, col) == password:
                        r2=row
                        
            if r1==r2:
                print ('\nWelcome Home..')
            else:
                print ('\n!!!!Wrong Password!!!!')
                exit()
        else:
            print ('\n!!!!Wrong Password!!!!')
            exit()
            
    else:
        print ('\n\n!!!!...Invalid user...!!!!')
        print ('\nPlease Register First, Then Try..')
        Register=input("\nAre you want to Register (Yes/No) :: ")
        if Register in ('no','No','NO'):
            print("\nThanks!! Come Again.")
            exit()
        elif Register in  ('yes','Yes','YES'):
            newname=input("\nEnter your name (If you don't want then enter exit) :: ")
            if newname in e:
                print ('\nThanks..You Always Welcome ')
                exit()
            elif newname in checkname:
                print ('\nHey, You already Here !!\n###Enter Again###')
                exit()
            else:
                newpassword=input("\nEnter Password :: ")
                if newpassword in checkpassword:
                    print('###Please try another passowrd###')
                    exit()
                else:
                    conform=input('Are you sure to save (Yes/No):: ')
                    if conform in ('no','No'):
                        print ('\nThanks, please start again')
                        exit()
                    elif conform in ('Yes','yes'):
                        sheet1[np] = newname
                        sheet1[pp] = newpassword
                        xfile.save(path)
                        print('\nEntry Successfull !!!! \n\n....Please Restart....')
                        exit()
                    else:
                        print ('###ERROR###')
                        exit()
        else:
            print ('Invalid Entry !!\n####Try Again####')
            exit()

welcome(name)
