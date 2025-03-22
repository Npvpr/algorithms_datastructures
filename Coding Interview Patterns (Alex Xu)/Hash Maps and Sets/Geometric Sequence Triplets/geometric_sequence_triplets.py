def solution(inputArr, r):
    leftMap = {}
    rightMap = {}
    for i in inputArr:
        # you can use 'defaultdict' to ensure the default value of 0 is returned when accessing a key that doesn’t exist in the hash map.
        # I prefer doing manually
        if i not in rightMap.keys():
            rightMap[i] = 1
            # not to get index when leftMap[x//r] for new ints
            leftMap[i] = 0
        else:
            rightMap[i] += 1
    count = 0
    for x in inputArr:
        # remove current int from right
        # technically, removing x before count doesn't matter because finding x*r in rightMap will never count x (unless r is 1)
        # but conceptually, current number should not be included inside the array right side of the number
        rightMap[x] -= 1

        if x % r == 0:
            if x//r in leftMap.keys() and x*r in rightMap.keys():
                count += leftMap[x//r] * rightMap[x*r]

        # add current int to the left
        leftMap[x] += 1
            
    return count

def main():
    # Original sample test case:
    print(solution([2, 1, 2, 4, 8, 8], 2))  # Expected output: 5

    # Edge Case 1: Empty Array
    print(solution([], 2))  # Expected output: 0

    # Edge Case 2: Single Element Array
    print(solution([1], 2))  # Expected output: 0

    # Edge Case 3: Two Elements Only
    print(solution([1, 2], 2))  # Expected output: 0

    # Edge Case 4: All Identical Elements with r = 1
    print(solution([1, 1, 1, 1], 1))  # Expected output: 4

    # Edge Case 5: Larger Set of Identical Elements with r = 1
    print(solution([1, 1, 1, 1, 1], 1))  # Expected output: 10

    # Edge Case 6: No Valid Triplets (Different Ratio)
    print(solution([1, 2, 3, 4, 5], 3))  # Expected output: 0

    # Edge Case 7: Valid Triplets with Mixed Order and Duplicates
    print(solution([1, 3, 9, 9, 27, 81], 3))  # Expected output: 6

    # Edge Case 8: Case with r = 0
    # Here, we catch and print the exception.
    try:
        print(solution([0, 0, 0], 0))
    except Exception as e:
        print("Error for r=0:", e)

    # Edge Case 9: Negative Numbers with a Negative Ratio
    print(solution([1, -1, 1, -1, 1], -1))  # Expected output: Depends on array order

    # Edge Case 10: Duplicates in a Non-r = 1 Geometric Progression
    print(solution([2, 2, 2, 4, 4, 8], 2))  # Expected output: 6
    
main()