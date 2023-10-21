def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algorithm(b, a % b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


gcd = euclidean_algorithm(a, b)
print("Наибольший общий делитель чисел", a, "и", b, ":", gcd)
