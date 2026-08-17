def count_even_numbers(nums: list) -> int:
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += 1
    return result
print(count_even_numbers([1,2,3,4,5,6]))
print(count_even_numbers([1, 3, 5, 7]))
print(count_even_numbers([2, 4, 6, 8]))