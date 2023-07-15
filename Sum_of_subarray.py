def sum_of_subarray_sums(A):
    N = len(A)
    total_sum = 0

    for i in range(N):
        current_sum = 0
        for j in range(i, N):
            current_sum += A[j]
            total_sum += current_sum

    return total_sum
A = list(map(int,input().split()))
result = sum_of_subarray_sums(A)
print("Sum of all subarray sums:", result)
