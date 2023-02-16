# String Manipulation

Here's a simple Python function that takes a string to be manipulated as an input and returns a  manipulated string.

 ```python

 def string_manipulation(input_string: str) -> str:
    input_string = input_string.lower().replace(" ", "")
    return input_string[::-1]
 ```

## TODO

- Completing `string_manipulation.py`

## Requirements

- Use only the following arithmetic operators in your solution: +, -, \*, /, //, %, \*\*
- The program should take one argument, an integer n (1 <= n <= 10^4), and print the output to the console.
- No modules can be imported.



