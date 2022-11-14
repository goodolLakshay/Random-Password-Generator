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


if password_length < 11:
    print("For your own safety",
          "The suggested length is >= 12")
    confirmation = input("Do you still wish to continue? y/n:  ")
    if confirmation == "y":
        rand_pass_gen(password_length)
    else:
        print("Thank you for trying out the Random-Password-Generator")
        exit()
else:
    rand_pass_gen(password_length)
