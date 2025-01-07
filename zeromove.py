def zeroMoveNim(p):
    # Compute the XOR sum of the piles
    xor_sum = 0
    for pile in p:
        xor_sum ^= pile
    
    # Count the number of piles with more than 1 item
    multiple_item_piles = sum(1 for pile in p if pile > 1)
    
    # If xor_sum is 0 or no multiple-item piles are available, John loses
    if xor_sum == 0 or multiple_item_piles == 0:
        return 'L'
    else:
        return 'W'

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())  # Number of games

    for g_itr in range(g):
        n = int(input().strip())  # Number of piles
        p = list(map(int, input().rstrip().split()))  # Pile configurations

        result = zeroMoveNim(p)

        fptr.write(result + '\n')

    fptr.close()
