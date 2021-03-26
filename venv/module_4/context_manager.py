import time

class timer:

    def __init__(self, name):
        self.name = name
        self.start = None

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        duration = round(end - self._start, 2)
        print(f"block  '{self.name}' executed in {duration} sec")

with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
