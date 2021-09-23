class Calculator:

    def calculate(self, expression):
        global stack
        expressionList = expression.split(" ")
        try:
            for element in expressionList:
                if element == '+':
                    stack.append(stack.pop() + stack.pop())
                elif element == '*':
                    stack.append(stack.pop() * stack.pop())
                elif element == '-':
                    el2 = stack.pop()
                    el1 = stack.pop()
                    stack.append(el1 - el2)
                elif element == '/':
                    el2 = stack.pop()
                    el1 = stack.pop()
                    dividend = (el1 / el2)
                    stack.append(round(dividend, 4))
                else:
                    if "." not in element:
                        number = int(element)
                    else:
                        number = float(element)
                    stack.append(number)
                print(stack)
            return stack[-1]
        except:
            print("")
            print("I wasn't able to process your request:")
            print("")
            print("Invalid Input = " + user_input)
            print("")
            print("Please only input numbers and + - * / operators separated by a space.")

print("")
print("  < Launching Reverse Polish Notation Calculator >")
print("")
print("  < Version 1.0 >")
print("")
print("  < This version currently handles + - * / operators >")
print("")
calc = Calculator()
user_input = ""
stack = []
while user_input.lower() not in ["exit", "quit", "stop", "q", "close", "help", "h"]:
    user_input = input("> ")
    output = calc.calculate(user_input)
    print(output)
if user_input.lower() in ["help", "h"]:
    print("  ◦◦◦ HELP ◦◦◦ ")
    print("")
    print("  ◦ Reverse Polish Notation is also known as 'postfix' notation ")
    print("")
    print("  ◦ This means your operator symbols + - * / are written AFTER your numerical operands ")
    print("")
    print("  ◦ For example: '2 2 +' will result in '4'")
    print("")
    print("  ◦ This also means '2 + 2' is an invalid input")
    print("")
    print("      < ANOTHER EXAMPLE >")
    print("")
    print("  ◦ '2 2 2 + +' will result in '6' ")
    print("")
    print("  ◦ In the event of - or /, an RPN calculator will 2nd to last entry and subtract of divide by the last entry ")
    print("")
    print("  ◦ After each operator symbol is executed, the resulting value is put back in the list")
    print("")
    print("      < MORE COMPLICATED EXAMPLE >")
    print("  10 4 3 2 1 + + + /")
    print("")
    print("      < PROCESS >")
    print("  [10]")
    print("  [10, 4]")
    print("  [10, 4, 3]")
    print("  [10, 4, 3, 2]")
    print("  [10, 4, 3, 2, 1]")
    print("  [10, 4, 3, 3]")
    print("  [10, 4, 6]")
    print("  [10, 10]")
    print("  [1.0]")
    print("")
    print("      < RESULT >")
    print("  1.0 ")
    










else:
    print("")
    print("  < Thank you, have a nice day >")
    print("")
    print("  < Exiting the calculator >")



