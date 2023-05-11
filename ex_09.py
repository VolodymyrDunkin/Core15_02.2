result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input(">>>")
    
    if user_input == '=':
        print(result)
        break
    
    if wait_for_number:
        try:
            operand = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"{user_input} not a number")
            continue
    else:
        if user_input in '-+*/':
            operator = user_input
            wait_for_number = True
        else:
            print(f"{user_input} not operator")
            continue
    
    if not result:
        result = operand
        operand = None
        continue
    
    if operand and operator:
        if operator == "+":
            result += operand
        if operator == "-":
            result -= operand
        if operator == "*":
            result *= operand
        if operator == "/":
            result /= operand
    
        operator = None
        operand = None