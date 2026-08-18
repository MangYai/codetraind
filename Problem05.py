from typing import List

def find_divisors(n: int) -> List[int]:
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

n = int(input('Number: '))
print(find_divisors(n))
# output Number: 10
#[1, 2, 5, 10]