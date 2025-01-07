def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(len(a)):
        if(a[i-1] > b[i-1]):
            alice += 1
        elif(a[i-1] < b[i-1]):
            bob += 1
    return (alice, bob)