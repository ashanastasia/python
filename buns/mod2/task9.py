vowels = 'аеёиоуыэюя' 
consonants = 'бвгджзйклмнпрстфхцчшщ'  
text = input().lower()  
vowels_count = 0  
consonants_count = 0  
for letter in text:
    if letter in vowels:
        vowels_count += 1
    elif letter in consonants:
        consonants_count += 1
print(vowels_count, consonants_count)
