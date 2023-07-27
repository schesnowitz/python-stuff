import requests, hashlib


def get_user_input():
    response = 'password'
    hash_pass_prep_for_api(response)
    return response

def hash_pass_prep_for_api(user_text):
    hashed_password = hashlib.sha1(f"{user_text}".encode()).hexdigest().upper()
    first_5_hashed_password = hashed_password[0:5]
    tail_hashed_password = hashed_password[5:]

    call_the_api(first_5_hashed_password, tail_hashed_password, user_text)


def call_the_api(data_for_api, tail_of_hex_pass, original_pass):
    api_response = requests.get(f"https://api.pwnedpasswords.com/range/{data_for_api}")
    spliting_lines = api_response.text.splitlines()
    check_the_password(spliting_lines, tail_of_hex_pass, original_pass)



def check_the_password(the_api_response, hex_tail, original_pass):

    for line in the_api_response:
        line.split(":")
        # print(type(line))
        new_lines = []
        new_lines.append(line.split(':'))
        # print(type(new_lines))
        for hex, count in new_lines:
            if hex in hex_tail:
                print(hex, hex_tail)
                print(f"The password \"{original_pass}\" has been pawned {count} times")
                return f"The password \"{original_pass}\" has been pawned {count} times"
    print(f"There are no data breaches found for \"{original_pass}\" rock and roll!")    
    return f"There are no data breaches found for \"{original_pass}\" rock and roll!"         
       



get_user_input()
