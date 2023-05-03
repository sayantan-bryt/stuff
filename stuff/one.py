__doc__ = '''Do maths with python modules

ref: https://youtu.be/t863QfAOmlY

$ python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import one
>>> one + one
<module 'two'>
>>> import two
>>> one + two
<module 'three'>
>>> two ** two       
<module 'four'>
>>> import four
>>> four
<module 'four'>
>>>
'''


import sys
import types


name_to_num = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20 }
num_to_name = { v: k for k, v in name_to_num.items() }


def _save_module(val):
    if val == 1:
        return

    with open(__name__ + '.py', 'r') as src, open(num_to_name[val] + '.py', 'w') as dest:
        for line in src:
            dest.write(line)


class _Foo(types.ModuleType):

    def __add__(self, other):
        val = name_to_num[__name__] + name_to_num[other.__name__]
        _save_module(val)
        return _Foo(num_to_name[val])

    def __sub__(self, other):
        val = name_to_num[__name__] - name_to_num[other.__name__]
        _save_module(val)
        return _Foo(num_to_name[val])

    def __mul__(self, other):
        val = name_to_num[__name__] * name_to_num[other.__name__]
        _save_module(val)
        return _Foo(num_to_name[val])

    def __floordiv__(self, other):
        val = name_to_num[__name__] // name_to_num[other.__name__]
        _save_module(val)
        return _Foo(num_to_name[val])

    def __pow__(self, other):
        val = name_to_num[__name__] ** name_to_num[other.__name__]
        _save_module(val)
        return _Foo(num_to_name[val])


sys.modules[__name__] = _Foo(__name__, __doc__)

