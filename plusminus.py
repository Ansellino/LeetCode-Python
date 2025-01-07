def plusMinus(arr):
    # Write your code here
    posVal = 0
    posNeg = 0
    posZero = 0
    for num in arr:
        if(num==0):
            posZero += 1
        elif(num<0):
            posNeg += 1
        else:
            posVal += 1
    print(posVal/len(arr))
    print(posNeg/len(arr))
    print(posZero/len(arr))