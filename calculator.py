

class Calculator:

    def calculate(self, s):

        result = 0
        current = 0

        return result + current

print("Launching Calculator Application...")
calc = Calculator()
user_input = ""
while user_input not in ["exit", "quit", "stop", "q", "close"]:
    user_input = input("> ")
    output = calc.calculate(user_input)
    print(output)
print("Exiting the calculator...")
