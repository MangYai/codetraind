def check_prime(n: int) -> str:
    if n <= 1 :
        return "is not prime"
    for i in range(2, n):
        if n % i == 0:
            return "is not prime"
    return "is prime"

number = int(input('Number: '))
print(check_prime(number))
#output Number: 7
#is prime
#Number: 8
#is not prime