def can_form_palindrome(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    if odd_count > 1:
        return False
    
    palindrome = ""
    
    for char, count in char_count.items():
        palindrome += char * (count // 2)
    
    odd_char = ""
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_char = char
            break
    
    palindrome += odd_char + palindrome[::-1]
    
    return palindrome


input_string = input("Введите строку: ")
result = can_form_palindrome(input_string)
if result:
    print("Можно составить палиндром:", result)
else:
    print("Невозможно составить палиндром из данной строки.")

