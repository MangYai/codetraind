def find_pair_with_product(nums: list, target: int) -> list:
    result = []
    for i in range(len(nums)):
        for b in range(i + 1,len(nums)):
            if nums[i] * nums[b] == target:
                result.append([nums[i],nums[b]])
    return result


print(find_pair_with_product([1, 2, 3, 4, 5, 6], 6))
print(find_pair_with_product([2, 4, 5, 7], 14))
print(find_pair_with_product([3, 5, 9, 10], 25))
print(find_pair_with_product([1, 2, 3, 4, 5], 20))
