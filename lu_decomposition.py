def GEO (A):

    n=len(A)
    L=[[0 for x in range (n)] for y in range (n)]
    U=[[0 for x in range (n)] for y in range (n)]
    
    for i in range(n):
        sum = 0
        for k in range(i, n):
            sum = 0
            for j in range(i,n):
                U[i][k] = A[i][k] - sum
                sum += (L[i][j] * U[j][k])
        
        for k in range(i, n):
            if (i == k):
                L[i][i] = 1 
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])

                L[k][i] = int((A[k][i] - sum) / U[i][i])

    #Not using numpy
    print("Lower Triangular\t\t\tUpper Triangular")
    for i in range(n):
        #Lower
        for j in range(n):
            print(L[i][j], end="\t")
        print("", end="\t")

        # Upper
        for j in range(n):
            print(U[i][j], end="\t")
        print("")
               
A = [[2, -1, 0, 0],[-1, 2, -1, 0],[0, -1, 2, -1],[0, 0, -1, 2]]

GEO (A)
