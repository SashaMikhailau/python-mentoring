""" Task 5.5
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

```python
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
 "Last result = 'None'"
 "Current result = 'ab'"
sum_list("abc", "cde")
 "Last result = 'ab'"
 "Current result = 'abccde'"
sum_list(3, 4, 5)
 "Last result = 'abccde'"
 "Current result = '12'"
"""


def remember_result(func):
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result = {last_result}")
        last_result = func(*args)
        return last_result

    return wrapper


@remember_result
def sum_list(*args):
    result = args[0]
    for i in range(1, len(args)):
        result += args[i]
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)
