def calculate_sum_and_average() -> None:
    numbers = []
    for i in range(5):
        number = float(input(f'Enter number {i + 1}: '))
        numbers.append(number)
        
    print(f"Sum: ", sum(numbers))
    print(f"Average: ", sum(numbers) / len(numbers))
    
calculate_sum_and_average()
#output Enter number 1: 10
#Enter number 2: 20
#Enter number 3: 30
#Enter number 4: 40
#Enter number 5: 50
#Sum:  150.0
#Average:  30.0