from math import gcd

def phi(n):
    m = 0        
    for j in range(1, n + 1):
        if gcd(n, j) == 1:
            m += 1
    return m

def magic_number(base,phi,m): 
    return base**(phi-m)

def get_indices(gs,bs):
    for j in range(len(gs)): 
        for i in range(len(bs)):
            if bs[i] == gs[j]: 
                return (i , j)  

    return None