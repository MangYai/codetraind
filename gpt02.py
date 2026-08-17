def count_greater_than_10(numbers: list) -> int:
    result = 0
    for i in numbers:
        if i > 10:
            result += 1
    return result

print(count_greater_than_10([5,12,8,20,15]))