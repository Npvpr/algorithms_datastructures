from typing import List

def longestConsecutiveNumbers(nums: List[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_chain = 0

    for num in num_set:
        # If the current number is the smallest number in its chain, search for the length of its chain.
        # Time complexity of finding a number(in/not in) from a set is constant(O(1))
        # Because the set is stored in the form of a hash table
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
        # Continue to find the next consecutive numbers in the chain.
            while (current_num + 1) in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    return longest_chain
        
def main():
    print(longestConsecutiveNumbers([1, 2, 3, 4, 5])) # 5
    print(longestConsecutiveNumbers([])) # 0
    print(longestConsecutiveNumbers([1])) # 1
    print(longestConsecutiveNumbers([1, 1, 1])) # 1
    print(longestConsecutiveNumbers([1, 3, 2, 6, 9, 5, 7, 8])) # 5

main()