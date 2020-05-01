check={'Sabyasachi Dhara','Pallab Mahapatra','Jit bhattacharya','Suman Adhikary','Sumit Nayek'}

name = input('What is your name :: ')

def welcome(n):
    if n in check:
        print ('Welcome Home..')
    else:
        print ('!!!!...Invalid user...!!!!')
        print ('Please Sign in First, Then Try..')

welcome(name)
