def count_odd(numbers: list) -> int:
    result = 0
    for i in numbers:
        if i % 2 != 0:
            result += 1
    return result


print(count_odd({1,2,3,4,5,6}))