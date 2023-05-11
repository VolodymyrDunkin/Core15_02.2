sum = 0
while sum <= 100:
    user_input = input(">>>")
    if user_input == ".":
        break
    try:
       sum += float(user_input)
    except ValueError:
        print(f"Sorry {user_input} not a number, try again") 
else:
    print(sum)