import re

class Calculator:

    def calculate(self, expression):
        global stack
        expressionList = expression.split(" ")
        while user_input.upper() not in ["EXIT", "QUIT", "STOP", "Q", "CLOSE", "HELP", "H", "CLEAR", "C", "^D"]:
            invalidCharacters = re.search('[^\r\n 0-9\.\+\-\*\/\^D]', user_input)
            anyCharacter = re.search('^$', user_input)
            mixedValid = re.search('(?:[0-9]+[+\-*\/]|[+\*\/]+[0-9])', user_input)
            validSpacing = re.search('^\S((?!.*  ).*\S)?$', user_input)
            try:
                for element in expressionList:
                    if anyCharacter != None:
                        print("")
                        print("User Input was empty: Checking Status ")
                        print("")
                        print(f"Expression in progress is: { stack }")
                        print("")
                        print("If this was an error, please input NUMBERS or + - * / operators separated by a space.")
                        print("")
                    elif element == '+' and len(stack) > 1:
                        stack.append(stack.pop() + stack.pop())
                    elif element == '*' and len(stack) > 1:
                        stack.append(stack.pop() * stack.pop())
                    elif element == '-' and len(stack) > 1:
                        el2 = stack.pop()
                        el1 = stack.pop()
                        stack.append(el1 - el2)
                    elif element == '/' and len(stack) > 1:
                        el2 = stack.pop()
                        if el2 == 0:
                            print("")
                            print("This expression attempted to divide by zero.")
                            print("")
                            print("Please try another expression.")
                            print("")
                            print(f"Expression in progress is: { stack }")
                            print("")
                        else:
                            el1 = stack.pop()
                            dividend = (el1 / el2)
                            stack.append(round(dividend, 4))
                    elif not validSpacing:
                        print("")
                        print("Please do not start or end your input with a space.")
                        print("")
                        print("Also, please only use a single space between valid inputs.")
                        print("")
                        print("Please retry your expression.")
                        print("")
                        print(f"Expression in progress is: { stack }")
                        print("")
                    elif mixedValid:
                        print("")
                        print("Please separate valid inputs with a space.")
                        print("")
                        print("Please retry your expression.")
                        print("")
                        print(f"Expression in progress is: { stack }")
                        print("")
                    elif element in ['+', '-', '*', '/'] and len(stack) < 2:
                        print("")
                        print("You must have two or more operands to use an operator")
                        print("")
                        print("Valid operators are + - * /")
                        print("")
                        print("Valid operands are numbers")
                        print("")
                        print(f"Expression in progress is: { stack }")
                        print("")
                    elif invalidCharacters != None:
                        print("")
                        print("User Input = " + user_input)
                        print("")
                        print("Please only input NUMBERS or + - * / operators separated by a space.")
                        print("")
                        print(f"Expression in progress is: { stack }")
                        print("")
                    else:
                        if "." not in element:
                            number = int(element)
                        else:
                            number = float(element)
                        stack.append(number)
                    # print(stack)
                if len(stack) > 0:
                    # print(user_input)
                    return stack[-1]
                else:
                    return "You have a clean slate"
            except:
                print("")
                print("I wasn't able to process your request:")
                print("")
                print("Invalid Input = " + user_input)
                print("")
                print("Please only input numbers or + - * / operators separated by a space.")
                print("")

print("")
print("    •   Launching Reverse Polish Notation Calculator ")
print("")
print("    •   Version 1.0 ")
print("")
print("    •   This version currently handles + - * / operators ")
print("")
print("    •   CLEAR: c     QUIT: q     HELP: h ")
print("")
calc = Calculator()
user_input = ""
stack = []
while user_input.upper() not in ["EXIT", "QUIT", "STOP", "Q", "CLOSE", "^D"]:
    if user_input.upper() in ["HELP", "H"]:
        print("          ◦◦◦ HELP ◦◦◦ ")
        print("")
        print("  ◦ Reverse Polish Notation is also known as 'postfix' notation ")
        print("")
        print("  ◦ This means your operator symbols + - * / are written AFTER your numerical operands ")
        print("")
        print("        ◦◦◦ EXAMPLE ◦◦◦")
        print("")
        print("  ◦ For example: '2 2 +' will result in '4'")
        print("")
        print("  ◦ This also means '2 + 2' is an invalid input")
        print("")
        print("        ◦◦◦ ANOTHER EXAMPLE ◦◦◦")
        print("")
        print("  ◦ '2 2 2 + +' will result in '6' ")
        print("")
        print("  ◦ In the event of - or /, an RPN calculator will take the 2nd to last entry and subtract of divide by the last entry ")
        print("")
        print("  ◦ After each operator symbol is executed, the resulting value is put back in the list")
        print("")
        print("        ◦◦◦ MORE COMPLICATED EXAMPLE ◦◦◦")
        print("")
        print("      10 4 3 2 1 + + + /")
        print("")
        print("        ◦◦◦ PROCESS ◦◦◦")
        print("")
        print("      [10]")
        print("      [10, 4]")
        print("      [10, 4, 3]")
        print("      [10, 4, 3, 2]")
        print("      [10, 4, 3, 2, 1]")
        print("2+1=3            | /")
        print("      [10, 4, 3, 3]")
        print("3+3=6         | /")
        print("      [10, 4, 6]")
        print("6+4=10     | /")
        print("      [10, 10]")
        print("10/10=1 | /")
        print("      [1.0]")
        print("")
        print("        ◦◦◦ RESULT ◦◦◦")
        print("  1.0 ")
        print("")
        print("        ◦◦◦ CHECK STATUS ◦◦◦")
        print("")
        print("To check the status of your expression, simply submit an empty input")
        print("")
        user_input = input("> ")
        output = calc.calculate(user_input)
        # print(output)
    elif user_input.upper() in ["CLEAR", "C"]:
        stack = []
        print("Clear input")
        user_input = input("> ")
        output = calc.calculate(user_input)
    else:
        user_input = input("> ")
        output = calc.calculate(user_input)
        print(output)

else:
    print("")
    print("  < Thank you, have a nice day >")
    print("")
    print("  < Exiting the calculator >")



