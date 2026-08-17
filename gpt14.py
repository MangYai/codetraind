def prime_numbers_in_range(start: int, end: int) -> tuple:
    primes = []
    total = 0
    for i in range(start, end):
        if i > 1:
            is_prim = True
        for j in range(2, i):
            if i % j == 0:
                is_prim = False
                break
        
        if is_prim:
            primes.append(i)
            total += i
            
    return (primes,total)


print(prime_numbers_in_range(10,20))