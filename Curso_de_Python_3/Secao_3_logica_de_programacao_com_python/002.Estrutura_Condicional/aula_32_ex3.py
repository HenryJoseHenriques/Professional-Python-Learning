name = input("What's your name?\n")

numName = len(name)

if numName > 1:
    if numName <=4:
        print("Your name is short.\n")
    elif numName >= 5 and numName <= 6:
        print("Your name is normal.\n")
    else:
        print("Your name is long.\n")
else:
    print("You name is very short.\n")
