# CLI Reverse Polish Notation Calculator

This is a RPN Calculator deisgned using Python 3 to receive input and display output from the command line.

## Installation

You will need to have any version of [Python 3](https://www.python.org/downloads/) installed.

There are two files available in this repository and you will want to have both in the same folder.

calculator.py

printedMessages.py

## Usage

User will want to use python to run calculator.py

In a Windows Terminal:
```bash
D:\calculator> python calculator.py

    •   Launching Reverse Polish Notation Calculator

    •   Version 1.0

    •   This version currently handles + - * / operators

    •   CLEAR: c     QUIT: q     HELP: h
```

## Thoughts from the programmer

I created a Calculator class with an RPN function in case I wanted to expand the calculators functionality later. I also tried really hard to consider the user experience. Currently invalid inputs are handled with error messages, many using the Regular Expression library: re. I tried to handle any errors with thoughtful error messages that don't exit the program and allow the user to try again. In an upcoming version, I would like to create some logic to fix obvious errors automatically and prevent the user from having to fix it themseleves. My most glaring bug is that if the user starts or ends a line with spaces, or puts too many spaces bewteen valid inputs the error message repeats itself once for each misused space. However, this doesnt compound with tabs in the same way. Any feedback is welcome. In an effort to match the example test cases, I left the program printing the most recent input. It can be misleading at times, so I made it so simply returning a blank input shows you what is currently in your stack.
