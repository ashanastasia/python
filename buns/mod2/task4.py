string = input().strip()

if not string.isdigit():
    print("Неверный ввод")
else:
    number = int(string)
    binary = ""
    octal = ""
    hexadecimal = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    number = int(string)
    while number > 0:
        octal = str(number % 8) + octal
        number //= 8

    number = int(string)
    while number > 0:
        remainder = number % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        number //= 16

    print(binary + ", " + octal + ", " + hexadecimal)
