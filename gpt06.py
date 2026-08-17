def find_min(numbers: list) -> int:
    result = numbers[0]
    for i in numbers:
        if i < result:
            result = i
    return result


print(find_min([3,8,2,10,5]))