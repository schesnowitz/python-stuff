name_pass = input('enter name and pass separated by a space ')
split_name_pass = name_pass.split()
name = split_name_pass[0]
password = split_name_pass[1]

password_length = len(password)
hidden_password = '*' * password_length


print(f"Hey {name} your password is {hidden_password} and is {password_length} characters long ")