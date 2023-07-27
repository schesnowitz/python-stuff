import requests
# https://pypi.org/project/requests/
import hashlib
# https://docs.python.org/3/library/hashlib.html
import sys
# https://docs.python.org/3/library/sys.html

def request_api(chars):
    url = f"https://api.pwnedpasswords.com/range/{chars}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"There was a problem with the API request, it returned Request Error Code: {response.status_code}")
    return response



def get_pwd_leaks_count(hashes, hash_2_check):
    # print(hashes.text)
    hashes = (line.split(':') for line in hashes.text.splitlines()) 
    # print(hashes)
    for h, count in hashes:
        if h == hash_2_check:
            return count
    return 0
        # print(h, count)
        

def check_api_for_passwords(passwords):
    # print(hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper())
    sha_one_pass = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    first_5, six_to_end = sha_one_pass[:5], sha_one_pass[5:]
    # print(first_5, six_to_end)
    response = request_api(first_5)
    return get_pwd_leaks_count(response, six_to_end)


def main(password):
    # for password in args:
    count = check_api_for_passwords(password)
    if count:
        if_result = f"{password} was found {count} times, this is not a great password"
        # print(if_result)
        return if_result
    else:
        else_result = f"{password} was not found, looks like you are good to go!"
        # print(else_result)
        return else_result
    # return "Program has completed and closed"
# main("ShitHead")
