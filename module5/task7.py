""" Task 5.7*
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
mod_c imports mod_b and changes vatiable x from it.
Then x from it is imported in a module.

Try to change x to a list `[1,2,3]`. Explain the result.
Still 1000 is printed, because Python has dynamic typing
Try to change import to `from x import *` where x - module names. Explain the result.
New x variable in global scope of module is created and it odesnt matter is it marked as global or not.
"""


