input_str = input().strip()

dot1_index = input_str.find('.')
str1 = input_str[:dot1_index]

dot2_index = input_str.rfind('.')
str2 = input_str[dot1_index+1:dot2_index]

str3 = input_str[dot2_index+1:]

print(str3)
print(str2)
print(str1)
