def prime_numbers_in_range(start: int, end: int) -> tuple:
    if start > end:
        return ([], 0)
    
    is_prime_list = [True] * (end + 1)
    is_prime_list[0] = False
    if end >= 1:
        is_prime_list[1] = False
        
    for i in range(2, int(end ** 0.5) + 1):
        if is_prime_list[i]:
            for j in range(i * i,end + 1 , i):
                is_prime_list[j] = False
                
    primes = [n for n in range(start, end + 1)if is_prime_list[n]]
    
    return(primes, sum(primes))

print(prime_numbers_in_range(10,20))
#uotput ([11, 13, 17, 19], 60)