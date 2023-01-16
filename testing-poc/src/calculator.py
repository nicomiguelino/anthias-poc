import time

class Calculator:
    def sum(self, a, b, sleep=False):
        if sleep:
            time.sleep(10)
        return a + b
