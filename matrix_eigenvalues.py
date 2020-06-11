import numpy as np
B = np.array([[4, -1, 6], [2, 1, 5], [2, -1,0]]) # Given Matrix
char_equ = np.poly(B) #Finding characteristic equation
print (np.poly1d(char_equ))

print (np.roots(char_equ)) #eigen values
