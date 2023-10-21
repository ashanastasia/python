def count_letters(filename):
    char_count = {}
    
    with open(filename, 'r') as file:
        content = file.read()
        
        for char in content:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    
    sorted_count = sorted(char_count.items(), key=lambda x: x[1])
    
    result_filename = "result.txt"
    with open(result_filename, 'w') as result_file:
        for char, count in sorted_count:
            result_file.write(f"{char}: {count}\n")
    
    print(f"Статистика букв сохранена в файле {result_filename}")

input_filename = input("Введите имя файла: ")
count_letters(input_filename)
