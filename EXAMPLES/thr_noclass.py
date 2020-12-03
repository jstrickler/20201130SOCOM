#!/usr/bin/env python

import threading
import random
import time

stdout_lock = threading.Lock()

class DoIt:
    def __init__(self, num):
        self._num = num

    def __call__(self):
        time.sleep(random.randint(1, 3))
        # with stdout_lock:
        #     print("Hello from thread {}".format(self._num))
        self.result = 10 * self._num

    # def foo(self):
    #     time.sleep(random.randint(1, 3))
    #     # with stdout_lock:
    #     #     print("Hello from thread {}".format(self._num))
    #     self.result = 10 * self._num

def doit(num):  # <1>

    # stdout_lock.acquire()
    # stdout_lock.release()
    with stdout_lock:
        print("Hello from thread {}".format(num))


results = []
for i in range(10):
    # t = threading.Thread(target=doit, args=(i,))  # <2>
    di = DoIt(i)
    t = threading.Thread(target=di)  # <2>
    t.start()  # <3>
    results.append((t, di))  # add both Thread and DoIt objects to results

print("Done.")  # <4>

for t, d in results:
    t.join()
    print(d.result)
