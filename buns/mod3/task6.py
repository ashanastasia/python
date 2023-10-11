string = input()
result = ''.join([word[-1] for word in string.split()])
print(result)
