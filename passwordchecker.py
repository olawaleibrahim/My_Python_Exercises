import requests
import hashlib
import sys


def request_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check API and try again')
    print(f'This is res {res}')
    return res


def get_password_leak_counts(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    print(sha1password, first5, tail)
    response = request_api(first5)
    return get_password_leak_counts(response, tail)


def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f'The password was found {count} times')
        else:
            print('Password is safe. You are good to go')
        return ('Done')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
