
# ***************
# SYSTEM MESSAGES
# ***************

def welcomeMessage():
    print("")
    print("    •   Launching Reverse Polish Notation Calculator ")
    print("")
    print("    •   Version 1.0 ")
    print("")
    print("    •   This version currently handles + - * / operators ")
    print("")
    print("    •   CLEAR: c     QUIT: q     HELP: h ")
    print("")

def exitMessage():
    print("")
    print("  < Thank you, have a nice day >")
    print("")
    print("  < Exiting the calculator >")


def helpRequested():
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
    print("        [10]")
    print("        [10, 4]")
    print("        [10, 4, 3]")
    print("        [10, 4, 3, 2]")
    print("        [10, 4, 3, 2, 1]")
    print("2+1=3              | /")
    print("        [10, 4, 3, 3]")
    print("3+3=6           | /")
    print("        [10, 4, 6]")
    print("6+4=10       | /")
    print("        [10, 10]")
    print("10/10=1   | /")
    print("        [1.0]")
    print("")
    print("        ◦◦◦ RESULT ◦◦◦")
    print("  1.0 ")
    print("")
    print("        ◦◦◦ CHECK STATUS ◦◦◦")
    print("")
    print("To check the status of your expression, simply submit an empty input")
    print("")
    print("        ◦◦◦ GENERAL TIPS ◦◦◦")
    print("")
    print("Your expressions will carry over, so if you want to start fresh input: c")
    print("")


# **************
# ERROR MESSAGES
# **************

def emptyInput():
    print("""User Input was empty: Checking Status

If this was an error, please input NUMBERS or + - * / operators separated by a space.
""")

def divideByZero():
    print("")
    print("This expression attempted to divide by zero.")
    print("")
    print("Please try another expression.")
    print("")

def invalidSpacing():
    print("")
    print("Please do not start or end your input with a space.")
    print("")
    print("Also, please only use a single space between valid inputs.")
    print("")
    print("Please retry your expression.")
    print("")

def mixingValidInputs():
    print("")
    print("Please separate valid inputs with a space.")
    print("")
    print("Please retry your expression.")
    print("")

def tooManyOperators():
    print("")
    print("You must have two or more operands to use an operator")
    print("")
    print("Valid operators are + - * /")
    print("")
    print("Valid operands are numbers")
    print("")

def tryFailed():
    print("")
    print("I wasn't able to process your request:")
