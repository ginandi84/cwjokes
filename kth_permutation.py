def kth_permutation(A, k):
    n = len(A)
    fact = [1] * n
    
    # Calculate factorials
    for i in range(1, n):
        fact[i] = i * fact[i-1]
    
    # Generate the kth permutation
    k -= 1
    res = []
    for i in range(n, 0, -1):
        idx = k // fact[i-1]
        k %= fact[i-1]
        res.append(A[idx])
        A = A[:idx] + A[idx+1:]
    
    return res
