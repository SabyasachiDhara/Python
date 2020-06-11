import numpy as np
import matplotlib.pyplot as plt
 
#(Q1-Q2) creating a numpy array
A = np.arange(1,31)
B = np.arange(5,35)

# printing arrays
print("Array A: ", A)
print("Array B: ", B)



#(Q3-Q4) reshaped to matrix(2d array)
AM = np.reshape(A, (5, 6))
BM = np.reshape(B, (6, 5))

# printing reshaped matrix
print("\nAM matrix :")
print(AM)
print("\nBM matrix :")
print(BM)



#(Q5) plotting A and B
plt.plot(A, B)
plt.show()



#(Q6) A Multiply B and save as CM 
CM = np.dot(AM,BM)
print("\nMatrix multiplication:")
print(CM)



#(Q7) Save CM in data.txt
file = open("data.txt", "w+")
data = str(CM)
file.write(data)
file.close()
file = open("data.txt", "r")
data = file.read()
#printing saved file as data.txt 
print("\nContent in data.txt:\n", data)
file.close()




#(Q8) checking each element Whether it is greater than 100 or not and saving the results as true/false in a matrix PM
PM = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
for a in range(len(CM)):
      for b in range(len(CM[a])):
               if CM[a][b] > 100:
                    PM[a][b] = 'True'
               else:
                    PM[a][b] = 'False'

print('\nTrue/False matrix ::')
print(np.matrix(PM))
