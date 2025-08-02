import numpy as np # Numerical operations library

# Creates transition tensor
def T_tensor(n):
    T = np.zeros((n, n, n, n))
    for k in range(n):
        for l in range(n):
            new_i = [(k - 1) % n, (k + 1) % n]
            new_j = [(l - 1) % n, (l + 1) % n]
            for i in new_i:
                for j in new_j:
                    T[i, j, k, l] += 0.25
    for k in range(n): # Consider seaparate case for k = l
        for i in range(n):
            for j in range(n):
                T[i,j,k,k] = 0
        T[k,k,k,k] = 1
    return T

# Creates Initial State Matrix
def S0(n, x0A, x0B): 
    S0 = np.zeros((n, n))
    S0[x0A, x0B] = 1    # Start at position frog 1: x0A, frog 2: x0B 
    return S0

# Computes V distribution
def v_distribution(n, x0A, x0B): 
    # Invalid starting conditions
    if n%2==0 and (x0A-x0B) % 2 != 0: 
        raise ValueError('Impossible due to parity conditions')
    elif x0A >= n or x0A <= -1 or x0B >= n or x0B <= -1: 
        raise ValueError('Invalid bounds')

    # Create Initial State Matrix
    S = S0(n, x0A, x0B)

    # Create transition tensor
    T = T_tensor(n)

    # Flatten tensor T to matrix T_m
    T_m = np.reshape(T, (n**2, n**2))

    # Compute T_m_inf, the limit of (T_m)^k as k approaches infinity
    eigenvalues, P = np.linalg.eig(T_m) # Compute eigenvalues and eigenvectors of T_m
    P_inv = np.linalg.inv(P) # Compute inverse of P
    D_inf = np.diag([1 if abs(1 - i) < 1e-8 else 0 for i in eigenvalues]) # D_inf (if eigenvalue=1 then keep as is becasue 1^inf=1, else 0)
    T_m_inf = P @ D_inf @ P_inv # P * D_inf * P_inv = T_m_inf in matrix form, (T_m)^k as k approaches infinity

    # Expand T_m_inf to 4D tensor T_inf
    T_inf = np.reshape(T_m_inf, (n, n, n, n))

    # Compute V distribution for starting state S, given by S_inf
    S_inf = np.einsum('ijkl,kl->ij', T_inf, S)

    distribution = [0.0 for _ in range(n)]
    for i in range(n): 
        distribution[i] = round(S_inf[i, i], 12)

    return distribution

if __name__ == "__main__":
    n = 11  # Example value for n
    x0A = 0  # Starting position of frog A
    x0B = 1  # Starting position of frog B

    distribution = v_distribution(n, x0A, x0B) # Computed V-distribution
    
    # Example visualization
    import matplotlib.pyplot as plt

    plt.bar(range(n), distribution, color='skyblue')
    plt.xlabel('Position')
    plt.ylabel('Probability')
    plt.title(f'V Distribution (n={n}, X_0^A={x0A}, X_0^B={x0B})')
    plt.show()