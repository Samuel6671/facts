import randfacts as rf

print('Random Facts')
x = ''

while x == '':
    print('Press Enter for Facts')
    x = input()
    fact = rf.get_fact()
    print(fact)