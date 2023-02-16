# List Operations

Here's a simple Python function that takes a list of integers to be manipulated as an input and returns a  manipulated list.

```python
def list_operations(input_list: list) -> list:
    input_list = list(set(input_list))
    input_list.sort()
    return input_list
```


## Requirements
1. Sort the list in ascending order.
2. Remove duplicates from the list.
3. Return the final list.