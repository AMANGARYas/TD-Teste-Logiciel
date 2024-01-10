

def max_three(lst):
    return sorted(lst, reverse=True)[:3]
    

def min_n(lst, n):
    return sorted(lst)[:n]

	
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    
def is_arithmetic_sequence(sequence):
    if len(sequence) < 2:
        return True 
    common_difference = sequence[1] - sequence[0]

    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != common_difference:
            return False

    return True
    

def is_geometric_sequence(sequence):
    if len(sequence) < 2:
        return True  

    common_ratio = sequence[1] / sequence[0]

    for i in range(2, len(sequence)):
        if sequence[i] / sequence[i - 1] != common_ratio:
            return False

    return True



