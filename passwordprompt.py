SECRET = "abc123"

pword = "a"
while pword != SECRET:
    pword = input("Enter password: ")
    if pword == SECRET:
        print("You got it")
        break
    print("Wrong one")