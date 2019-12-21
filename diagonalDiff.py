

#find diagonal differences.

class Solution:

  def diagonalDifference(arr):

    total_1, total_2 = 0,0
    revIn = len(arr) -1
    
    for i,x in enumerate(arr):
        #print( i + index)
        total_1 += arr[i][i]
        total_2 += arr[i][revIn - i]

    return abs( total_1 - total_2)
