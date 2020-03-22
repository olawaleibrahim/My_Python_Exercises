import re

with open('Scared.txt', mode='r') as word:
    words = (word.read())
    print(words)

a = re.findall('the', words)
pattern = re.compile('She')
print(a)

b = pattern.findall(words)
print(b)

pattern1 = re.compile(r"([a-zA-Z]).([e])")
c = pattern1.search(words)
print(c)
print(c.group(1))

# password checker
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d$")
password = input('Input your password: ')

if re.match(r'[a-zA-Z0-9$%#@]{8,}', password):
    print('Match!')
else:
    print('Unmatched!')

check = pattern2.fullmatch(password)
print(check)


