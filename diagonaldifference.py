def diagonalDifference(arr):
    # Write your code here
    finish = len(arr)
    sumA = 0
    sumB = 0
    for i in range(len(arr[0])):
        sumA += arr[i][i]
        sumB += arr[i][finish-1]
        finish -= 1
    return abs(sumA-sumB)