import numpy as np

def siamese_method(n):
    if n % 2 == 0:
        raise ValueError("Siamese method only works for odd n")
    
    magic_square = np.zeros((n,n), dtype=int)
    i, j = 0, n//2
    
    for num in range(1, n*n+1):
        magic_square[i,j] = num
        newi, newj = (i-1) % n, (j+1) % n
        if magic_square[newi,newj]:
            i = (i+1) % n
        else:
            i, j = newi, newj
    return magic_square

def doubly_even_method(n):
    if n % 4 != 0:
        raise ValueError("Doubly even method requires n divisible by 4")
    
    pattern = np.zeros((n,n), dtype=bool)
    for i in range(n):
        for j in range(n):
            pattern[i,j] = (i % 4 == j % 4) or (i % 4 + j % 4 == 3)
    
    magic_square = np.arange(1, n*n+1).reshape(n,n)
    magic_square[pattern] = n*n + 1 - magic_square[pattern]
    return magic_square

def singly_even_method(n):
    if n % 2 == 0 and n % 4 != 2:
        raise ValueError("Singly even method requires n = 4k+2")
    
    k = n//2
    A = siamese_method(k)
    B = A + k*k
    C = A + 2*k*k
    D = A + 3*k*k
    
    swap_cols = k//2
    A[:,:swap_cols], D[:,:swap_cols] = D[:,:swap_cols], A[:,:swap_cols]
    
    mid_col = k//2
    A[:,mid_col], D[:,mid_col] = D[:,mid_col], A[:,mid_col]
    
    if k > 1:
        A[swap_cols,:swap_cols], D[swap_cols,:swap_cols] = D[swap_cols,:swap_cols], A[swap_cols,:swap_cols]
    

    return np.vstack((np.hstack((A,B)), np.hstack((C,D))))

def generate_magic_square(n):
    if n % 2 == 1:  
        return siamese_method(n)
    elif n % 4 == 0:  
        return doubly_even_method(n)
    else:  
        return singly_even_method(n)

def verify_magic_square(square):
    n = square.shape[0]
    magic_constant = n * (n**2 + 1) // 2
    
    if not all(np.sum(square, axis=0) == magic_constant):
        return False
    if not all(np.sum(square, axis=1) == magic_constant):
        return False
    
    if np.sum(np.diag(square)) != magic_constant:
        return False
    if np.sum(np.diag(np.fliplr(square))) != magic_constant:
        return False
    
    return True

def print_magic_square(square):
    n = square.shape[0]
    print(f"\n{n}×{n} Magic Square (Magic Constant = {n*(n**2+1)//2}):")
    print(square)
    print(f"Verification: {'Valid' if verify_magic_square(square) else 'Invalid'}")

for n in range(4, 9):
    magic_square = generate_magic_square(n)
    print_magic_square(magic_square)