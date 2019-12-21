

#find diagonal differences.

class Solution:

  def diagonalDifference(self,arr):

    total_1, total_2 = 0,0
    revIn = len(arr) -1
    
    for i,x in enumerate(arr):
        #print( i + index)
        total_1 += arr[i][i]
        total_2 += arr[i][revIn - i]

    return abs( total_1 - total_2)

  
  
if __name__ == '__main__':
  
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    
    
    print(diagonalDifference(arr))
