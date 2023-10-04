line = input()
numbers = ""

for i in range(len(line)):
    if line[i] == " ":
        numbers += line[i-1]
numbers += line[len(line)-1]

unique_numbers = set(numbers)
result = len(numbers) != len(unique_numbers)
print(result)
