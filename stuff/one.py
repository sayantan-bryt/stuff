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

name_to_num = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'twenty_one': 21, 'twenty_two': 22, 'twenty_three': 23, 'twenty_four': 24, 'twenty_five': 25, 'twenty_six': 26, 'twenty_seven': 27, 'twenty_eight': 28, 'twenty_nine': 29, 'thirty': 30, 'thirty_one': 31, 'thirty_two': 32, 'thirty_three': 33, 'thirty_four': 34, 'thirty_five': 35, 'thirty_six': 36, 'thirty_seven': 37, 'thirty_eight': 38, 'thirty_nine': 39, 'forty': 40, 'forty_one': 41, 'forty_two': 42, 'forty_three': 43, 'forty_four': 44, 'forty_five': 45, 'forty_six': 46, 'forty_seven': 47, 'forty_eight': 48, 'forty_nine': 49, 'fifty': 50, 'fifty_one': 51, 'fifty_two': 52, 'fifty_three': 53, 'fifty_four': 54, 'fifty_five': 55, 'fifty_six': 56, 'fifty_seven': 57, 'fifty_eight': 58, 'fifty_nine': 59, 'sixty': 60, 'sixty_one': 61, 'sixty_two': 62, 'sixty_three': 63, 'sixty_four': 64, 'sixty_five': 65, 'sixty_six': 66, 'sixty_seven': 67, 'sixty_eight': 68, 'sixty_nine': 69, 'seventy': 70, 'seventy_one': 71, 'seventy_two': 72, 'seventy_three': 73, 'seventy_four': 74, 'seventy_five': 75, 'seventy_six': 76, 'seventy_seven': 77, 'seventy_eight': 78, 'seventy_nine': 79, 'eighty': 80, 'eighty_one': 81, 'eighty_two': 82, 'eighty_three': 83, 'eighty_four': 84, 'eighty_five': 85, 'eighty_six': 86, 'eighty_seven': 87, 'eighty_eight': 88, 'eighty_nine': 89, 'ninety': 90, 'ninety_one': 91, 'ninety_two': 92, 'ninety_three': 93, 'ninety_four': 94, 'ninety_five': 95, 'ninety_six': 96, 'ninety_seven': 97, 'ninety_eight': 98, 'ninety_nine': 99, 'one_hundred': 100 }
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

