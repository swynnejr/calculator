

class Calculator:

    def calculate(self, expression):
        stack = []
        for element in expression:
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
                stack.append(el1 / el2)
            else:
                stack.append(element)
            print(stack)
        return stack.pop()

print("Launching Calculator Application...")
calc = Calculator()
user_input = ""
while user_input not in ["exit", "quit", "stop", "q", "close"]:
    user_input = input("> ")
    output = calc.calculate(user_input)
    print(output)
print("Exiting the calculator...")
