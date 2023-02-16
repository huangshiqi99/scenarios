# Tuple Operations

Here's a simple Python function that takes a tuple to be manipulated as an input and returns a  manipulated tuple.

```python
def tuple_operations(input_tuple: tuple) -> tuple:
    
    input_list = list(input_tuple)
    input_list.sort()
    return tuple(input_list)
 ```

## TODO

- Completing `tuple_operations.py`

## Requirements

- Use only the following arithmetic operators in your solution: +, -, \*, /, //, %, \*\*
- The program should take one argument, an integer n (1 <= n <= 10^4), and print the output to the console.
- No modules can be imported.
