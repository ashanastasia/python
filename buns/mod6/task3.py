def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum
def get_armstrong_numbers():
    num = 153
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1
# Пример использования
gen = get_armstrong_numbers()
for i in range(8):
    print(next(gen), end=' ')
