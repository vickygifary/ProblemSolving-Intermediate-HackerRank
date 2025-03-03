import bisect

MOD = 10**9 + 7

def sortedSum(a):
    sorted_list = []  # Maintains the sorted order of elements
    prefix_sums = []  # Maintains the prefix sums of the sorted list
    total_sum = 0     # Stores the final result
    weighted_sum = 0  # Maintains the current weighted sum

    for num in a:
        # Find the insertion position for the current number
        idx = bisect.bisect_left(sorted_list, num)

        # Insert the number into the sorted list
        sorted_list.insert(idx, num)

        # Update the prefix sums
        if idx == 0:
            prefix_sums.insert(idx, num)
        else:
            prefix_sums.insert(idx, prefix_sums[idx - 1] + num)

        # Update the prefix sums for elements after the inserted index
        for j in range(idx + 1, len(prefix_sums)):
            prefix_sums[j] += num

        # Compute the weighted sum incrementally
        # Contribution of the new element: (idx + 1) * num
        weighted_sum += (idx + 1) * num

        # Contribution of elements after the new element: sum of elements after idx
        if idx + 1 < len(sorted_list):
            weighted_sum += prefix_sums[-1] - prefix_sums[idx]

        weighted_sum %= MOD

        # Update the total sum
        total_sum = (total_sum + weighted_sum) % MOD

    return total_sum

# Reading input
n = int(input())
a = [int(input()) for _ in range(n)]

# Printing the result
print(sortedSum(a))
