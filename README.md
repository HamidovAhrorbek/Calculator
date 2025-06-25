Python Calculator

A simple command-line calculator built in Python that can perform addition, subtraction, multiplication, and division. It allows continuous calculations by using the previous result or starting fresh.

Features
Add, subtract, multiply, and divide numbers.

Interactive prompt for input and operation selection.

Ability to chain calculations (use the previous answer for the next calculation).

Restart the calculation anytime.

How to Use
Run the script.

Enter the first number.

Choose an operation (+, -, *, /).

Enter the next number.

View the result.

Decide if you want to continue calculating with the result or start a new calculation.

Repeat or exit.

Example
csharp
Copy
Edit
Welcome to the calculator!
You can add (+), subtract (-), multiply (*) or divide (/) numbers.
What is the first number?: 10
+
-
*
/
Pick an operation: *
What is the next number?: 4
10 * 4 = 40
Type 'y' to continue calculating with 40, or type 'n' to start a new calculation: n
How It Works
Four math functions (add, subtract, multiply, divide) handle the calculations.

These functions are stored in a dictionary with keys representing the operators.

User inputs guide the program flow to perform the desired operations.

Recursive calls enable restarting the calculator without exiting the program.
