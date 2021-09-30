import printedMessages
import re

# Calculator Internal Functionality
# *********************************

def statusUpdate():
    print(f"Expression in progress is: { stack }")
    print("")

def verifyInput():
    print("")
    print("Invalid Input = " + user_input)
    print("")
    print("Please only input numbers or + - * / operators separated by a space.")
    print("")


class Calculator:

    def calculateRPN(self, expression):
        global stack
        expressionList = expression.split(" ")

        while user_input.upper() not in ["EXIT", "QUIT", "STOP", "Q", "CLOSE", "HELP", "H", "CLEAR", "C", "^D"]:
            invalidCharacters = re.search('[^\r\n 0-9\.\+\-\*\/\^D]', user_input)
            inputEmpty = re.search('^$', user_input)
            mixedValid = re.search('(?:[0-9]+[+\-*\/]|[+\*\/]+[0-9])', user_input)
            validSpacing = re.search('^\S((?!.*  ).*\S)?$', user_input)

            try:
                for element in expressionList:

                    if inputEmpty != None:
                        printedMessages.emptyInput()
                        statusUpdate()

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
                            printedMessages.divideByZero()
                            statusUpdate()
                        else:
                            el1 = stack.pop()
                            dividend = (el1 / el2)
                            stack.append(round(dividend, 4))

                    elif not validSpacing:
                        printedMessages.invalidSpacing()
                        statusUpdate()
                        break

                    elif mixedValid:
                        printedMessages.mixingValidInputs()
                        statusUpdate()
                        break

                    elif element in ['+', '-', '*', '/'] and len(stack) < 2:
                        printedMessages.tooManyOperators()
                        statusUpdate()
                        break

                    elif invalidCharacters != None:
                        verifyInput()
                        statusUpdate()
                        break

                    else:
                        if "." not in element:
                            number = int(element)
                        else:
                            number = float(element)
                        stack.append(number)
                    # To troubleshoot uncomment below
                    # print(stack)

                if len(stack) > 0:
                    return stack[-1]
                else:
                    return "You have a clean slate"
            except:
                printedMessages.tryFailed()
                verifyInput()

#  User Experience
# ****************

printedMessages.welcomeMessage()
calc = Calculator()
user_input = ""
stack = []
while user_input.upper() not in ["EXIT", "QUIT", "STOP", "Q", "CLOSE", "^D"]:

    if user_input.upper() in ["HELP", "H"]:
        printedMessages.helpRequested()
        user_input = input("> ")
        output = calc.calculateRPN(user_input)
        print(output)

    elif user_input.upper() in ["CLEAR", "C"]:
        stack = []
        print("Clear input")
        user_input = input("> ")
        output = calc.calculateRPN(user_input)
        print(output)


    else:
        user_input = input("> ")
        output = calc.calculateRPN(user_input)
        print(output)

else:
    printedMessages.exitMessage()




