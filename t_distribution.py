import numpy as np # Numerical operation libraries
import math

# Creates transition matrix
def T_matrix(n): 
    s = 2*n+1
    matrix = np.zeros((s, s), dtype=object)
    for i in range(1, s - 1):
        matrix[i-1, i] = 1/2   # sub-diagonal
        matrix[i+1, i] = 1/2   # super-diagonal
    return matrix

# Creates initial state vector
def P0(n):
    P0_list = []
    for k in range(n+1):
        P0_list.append(float(math.comb(n, k) / (2**n))) 
        if k != n:  
            P0_list.append(0)
    return np.array(P0_list, dtype=object).reshape(-1, 1)

# Creates extraction vector
def e(n): 
    e = [0 for _ in range(2*n+1)]
    e[0] = 1
    e[-1] = 1
    return np.array(e, dtype=object).reshape(-1, 1)

# Computes the probability of meeting at step k
def Pr(n, k): 
    if k < n or (k-n) % 2 != 0: # Impossible starting conditions
        return 0
    
    # Create transition matrix
    T = T_matrix(n)

    # Create initial state vector
    P = P0(n)

    # Create extraction vector
    E = e(n)

    return ((np.linalg.matrix_power(T, k-n) @ P).T @ E)[0,0] # Computing the probabilities of valid paths using (T^(k-n) * P0) · e

# Computes T-distribution for specific n, up to step k=200
def t_distribution(n, length=200):
    return np.array([Pr(n, k) for k in range(length+1)], dtype=object)

if __name__ == "__main__":
    n = 10  # Example value for n

    distribution = t_distribution(n) # Computed T-distribution

    # Example visualization
    import matplotlib.pyplot as plt

    plt.plot(range(len(distribution)), distribution, marker='.', linestyle='-', color='blue', markersize=1)
    plt.xlabel('k (steps)')
    plt.ylabel('Probability')
    plt.title(f'T-distribution for n = {n}')
    plt.show()