import random

password_length = int(input("Please enter the length of the password required: "))
print("_____________________________________________________")

def rand_pass_gen(n):
    empty_string = ""
    for i in range(1, n + 1):
        a = chr(random.randint(65, 90))
        b = chr(random.randint(97, 122))
        c = str(int(random.random() * 10))
        d = [a, b, c, "#", "@", "$", "&"]
        empty_string += random.choice(d)
    print("\n\n", "The generated password is:   ", empty_string)


rand_pass_gen(password_length)
