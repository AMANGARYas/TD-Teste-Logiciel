

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
	pass

def is_geometric_sequence(sequence):
	pass


