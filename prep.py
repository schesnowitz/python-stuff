import requests, hashlib


hashed_password = hashlib.sha1(b"password").hexdigest()
first_5_of_password = hashed_password[0:5].upper()
rest_of_hp = hashed_password[5:].upper()
# print(hashed_password)                
# print(first_5_of_password)


api_response = requests.get(f"https://api.pwnedpasswords.com/range/{first_5_of_password}")

# print(api_response.text.splitlines())
split_lines = api_response.text.splitlines()
# print(type(split_lines))
# print(api_response.text)
for line in split_lines:

    line.split(":")
    # print(type(line))
    new_lines = []
    new_lines.append(line.split(':'))
    # print(type(new_lines))
    for hex, count in new_lines:
        # print(count)
        # print(rest_of_hp)
        if hex in rest_of_hp:
            
            print(count)

