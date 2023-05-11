a = 0
while a < 6:
    a += 1
    print(f"!{a}")
    print(a % 2)
    if not a % 2:
        continue
    print(a)