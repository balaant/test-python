import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(cm_timer_1.__name__, time.time() - self.start)

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print(cm_timer_2.__name__, time.time() - start)

def main():
    with cm_timer_2():
        time.sleep(5.5)
    with cm_timer_1():
        time.sleep(5.5)


if __name__ == "__main__":
    main()