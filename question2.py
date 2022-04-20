def solution(A, K):  
     """ 
     Check if value of K or length of A divide by K equal zero. 
     If equal to zero, return the value of A
     """
     if K == 0 or len(A)/K ==0:
          return A
     
     """ 
     Check if value of K is greater than length of A. 
     If Greater, set the value of K to K divide by length of A
     """
     if K > len(A):
           K = K/len(A)
     
     """  After Checking all the condition, We then create a list of Rotation """
     A = A[len(A)-K:len(A)] + (A[0:len(A)-K])
     return A


# Test Case #
A = [3, 8, 9, 7, 6]
K =3
print(solution(A, K))