def max_in(A):
    if len(A) == 1:
        return A[0]
    else:
        return max(max_in(A[:-1]), A[-1])

print(max_in([1,2,3,4,5,6,7,9]))