# Dictionary Operations

Here's a simple Python function that takes a dictionary to be manipulated as an input and returns a  manipulated dictionary.

```python
def dictionary_operations(input_dict: dict) -> dict:
    
    input_dict["new_key"] = "new_value"
    input_dict.pop("remove_key", None)
    return input_dict
 ```

## TODO

- Completing `dictionary_operations.py`

## Requirements

- Use only the following arithmetic operators in your solution: +, -, \*, /, //, %, \*\*
- The program should take one argument, an integer n (1 <= n <= 10^4), and print the output to the console.
- No modules can be imported.
