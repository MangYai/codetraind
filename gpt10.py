def find_non_multiples(start: int, end: int) -> list: 
    result = []
    for i in range(start,end + 1):
        if not i % 3 == 0 and not i % 4 == 0 and not i % 5 == 0:  # or if i % _ != 0
            result.append(i)
    return result


print(find_non_multiples(1,10))