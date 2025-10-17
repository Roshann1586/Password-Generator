import random
import string

n = int(input("Enter the number of required characters for password (Not less than 4) : "))

if n < 4:
    print('Required number of characters must be at least 4.')

else:

    spl_ch = '!@#$%^&*()_+-=[{]}|:;./?><,~`'
    digits = '123456789'


    n_spl = random.choice(range(1, n-2))
    spaces_left = n - n_spl

    n_cap = random.choice(range(1, spaces_left - 1))
    spaces_left = n - n_spl - n_cap

    n_dig = random.choice(range(1, spaces_left))
    spl = random.choices(spl_ch, k = n_spl)

    n_sml = n - n_spl - n_cap - n_dig

    dig = random.choices(digits, k = n_dig)
    cap = random.choices(string.ascii_uppercase, k = n_cap)
    sml = random.choices(string.ascii_lowercase, k = n_sml)


    password_list = spl + dig + cap + sml
    random.shuffle(password_list)

    password = "".join(password_list)

    print("Generated Password : ", password)