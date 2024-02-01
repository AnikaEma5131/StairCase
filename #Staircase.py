#Staircase

def staircase(n):
        for i in range(1, n + 1):
            space = n - i
            character = i
            print(" " * space + "#" * character)


def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - (max(arr))
    max_sum = total_sum - (min(arr))
    return min_sum, max_sum