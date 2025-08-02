import numpy as np # Numerical operation libraries
import math

# Creates transition matrix
def T_matrix(n): 
    s = 2*n+1
    matrix = np.zeros((s, s), dtype=object)
    for i in range(1, s - 1):
        matrix[i-1, i] = 1   # sub-diagonal
        matrix[i+1, i] = 1   # super-diagonal
    return matrix

# Creates initial state vector
def c0(n):
    c0_list = []
    for k in range(n+1):
        c0_list.append(int(math.comb(n, k)))
        if k != n:  
            c0_list.append(0)
    return np.array(c0_list, dtype=object).reshape(-1, 1)

# Creates extraction vector
def e(n): 
    e = [0 for _ in range(2*n+1)]
    e[0] = 1
    e[-1] = 1
    return np.array(e, dtype=object).reshape(-1, 1)

# Computes the number of valid paths at step k
def paths(n, k): 
    if k < n or (k-n) % 2 != 0: # Impossible starting conditions
        return 0
    
    # Create transition matrix
    T = T_matrix(n)

    # Create initial state vector
    C = c0(n)

    # Create extraction vector
    E = e(n)

    return ((np.linalg.matrix_power(T, k-n) @ C).T @ E)[0,0] # Computing the number of valid paths using (T^(k-n) * c0) · e

# Computes the probability of meeting at step k
def Pr(n, k): 
    return 2**(-k) * paths(n, k) # Implements equation (2)

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
