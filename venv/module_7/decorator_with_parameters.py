from time import time
from functools import wraps
import io
import random
import unittest
import unittest.mock
import sys
from module_5.multiples_of_three_and_five import several_for_loops

N = 300000000
threshhold_test = 10

def timeit(threshhold=None):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if threshhold is None:
                print(f'Elapsed time:{random.randint(0, 100)} sec')
            else:
                start = time()
                func = function(*args, **kwargs)
                end = time()
                elapsed_time = end - start
                if elapsed_time > threshhold:
                    print(f'Elapsed time: {elapsed_time}')
        return wrapper
    return real_decorator

@timeit()
def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res

class TestTimeItDecoratorWithoutArgument(unittest.TestCase):

    def test_assert_stdout(self):
        range_var = range(0, 100)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        several_for_loops()
        sys.stdout = sys.__stdout__
        self.assertEqual(f'Elapsed time:{random.randint(0, 100)} sec',
               capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
