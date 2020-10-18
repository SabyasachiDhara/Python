import xlrd
import openpyxl

check={'admin'}

wb = xlrd.open_workbook(r'C:\Users\sabya\Documents\database.xlsx')

sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(sheet.nrows):
    imp=sheet.cell_value(i,0)
    check.add(imp)

l = len(check)
p='A'+str(l)

name = input('\nWhat is your name :: ')

def welcome(n):
    if n in check:
        print ('\nWelcome Home..')
    else:
        print ('\n\n!!!!...Invalid user...!!!!')

welcome(name)
