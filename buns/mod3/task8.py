phone_number = input() 
phone_number = '+' + ''.join(filter(str.isdigit, phone_number))
print(phone_number)
