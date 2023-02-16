# List Operations

Here's a simple Python function that takes a list of integers to be manipulated as an input and returns a  manipulated list.

```python
def list_operations(input_list: list) -> list:
    
    input_list = list(set(input_list))
    input_list.sort()
    return input_list
 ```

## TODO

- Completing `list_operations.py`

## Requirements

- Use only the following arithmetic operators in your solution: +, -, \*, /, //, %, \*\*
- The program should take one argument, an integer n (1 <= n <= 10^4), and print the output to the console.
- No modules can be imported.