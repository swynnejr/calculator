

class Calculator:

    def calculate(self, expression):
        stack = []
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
                # print(stack)
            return stack.pop()
        except:
            print("I wasn't able to process your request:")
            print(user_input)
            print("Please only input numbers and + - * / operators separated by a space.")

print("")
print("  < Launching Reverse Polish Notation Calculator >")
print("")
print("  < Version 1.0 >")
print("")
print("  < This version currently handles + - * / operators >")
print("")
calc = Calculator()
user_input = input("> ")
if user_input.lower() not in ["exit", "quit", "stop", "q", "close"]:
    output = calc.calculate(user_input)
    print(output)
else:
    print("")
    print("  < Thank you, have a nice day >")
    print("")
    print("  < Exiting the calculator >")
