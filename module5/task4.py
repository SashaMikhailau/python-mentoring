""" Task 5.4
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
a = "I am local variable!" -> global a
2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
a = "I am local variable!" -> nonlocal a
"""

from modules.legb import enclosing_funcion

func = enclosing_funcion()
func()
