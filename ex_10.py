text = "Python. "


for i in text:
    if "a" <= i <= "z":
        print('lower')
    elif "A" <= i <= "Z":
        print('upper')
    else:
        print(ord(i))