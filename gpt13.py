def is_prime(n: int) -> bool:
    count = 0
    for i in range(1,n + 1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False    
    
    
print(is_prime(7))
print(is_prime(10))