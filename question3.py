def solution(A):
     """ Count the length of key created """
     distinct_value = {}
    
     """ Update the the empty dictionary with the value as key after looping throug the array"""
     for value in A:
         distinct_value[value] = True
   
     """Return the length of distinct values in the array"""
     return len(distinct_value.keys())



# Test Case
A = [2, 1, 1, 2, 3, 1]
print(solution(A))