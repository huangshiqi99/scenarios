# String Manipulation

Here's a simple Python function that takes a string to be manipulated as an input and returns a  manipulated string.

```python
def string_manipulation(input_string: str) -> str:
    input_string = input_string.lower().replace(" ", "")
    return input_string[::-1]
```


## Requirements
1. Convert the string to lowercase.
2. Remove all whitespaces from the string.
3. Reverse the string.
4. Return the final string.