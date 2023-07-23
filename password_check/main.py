import requests
import hashlib


def request_api(chars):
    url = f"https://api.pwnedpasswords.com/range/{chars}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"There was a problem with the API request, it returned Request Error Code: {response.status_code}")

    else:
        return response


request_api('AAAAB')


def check_api_for_passwords(passwords):
    print(hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper())
    sha_one_pass = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    return sha_one_pass 
check_api_for_passwords('passwords')