entrada = input("What time is it?\n")

try:
    time = int(entrada)
    if time >=0 and time <=11:
        print("Good morning")
    elif time >=12 and time <=17:
        print("Good afternoon")
    elif time >=18 and time <=23:
        print("Good evening")
    else:
        print("invalid valor.\n")
except:
    print("Error. Please, digit a time valid.\n ")
