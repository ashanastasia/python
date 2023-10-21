def check_numbers(numbers):
    if all(num == numbers[0] for num in numbers):
        return "Все числа равны"

    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"

    else:
        return "Есть равные и неравные числа"

numbers = input("Введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]

result = check_numbers(numbers)
print(result)
