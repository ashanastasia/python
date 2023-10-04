string = input()
result = ""

for i in range(len(string)):
    if string[i] == " ":
        result += string[i-1]
result += string[len(string)-1]
print(result)
