def find_range(start: int, end: int) -> list:
    result = []
    for i in range(start,end + 1):
        result.append(i)
    return result
        


print(find_range(3,7))