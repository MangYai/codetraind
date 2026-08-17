def count_even(numbers: list) -> int:
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += 1
            
    return result
        
print(count_even([1,2,3,4,5,6]))