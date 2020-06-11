def mssele(A,B):
      
     
     A = set(A)
     B = set(B)
  
     if len(A) > len(B):
         print (list(A-B))
     else:
         print (list(B-A))
  
# Driver
if __name__ == "__main__":
    A = [1, 4, 5, 7, 8, 9, 15]
    B = list(range(1,21))
    print("missing elements are :: ")
    mssele(A,B)
