def count_number(numbers, target):
    
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)
    else:
        return count_number(numbers[1:], target)