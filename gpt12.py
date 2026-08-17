from typing import List
def find_divisors(n: int) -> List[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print(find_divisors(20))