# Things to do, chapter 15
import multiprocessing
import datetime
import time
from random import random
# from CustomImports import huh


# Because concurrency absolutely sucks in python, we have to move anything we don't want to run on EVERY process to
# the segment under if __name__ == "__main__":
# If you think that's weird, importing another file with top-level executions will do the same.
# Are you confused? Just uncomment the disabled import statement at the top of this file to see this in action

def wait_a_little():
    # Random.random() returns a float beteen 0 and 1
    time.sleep(random())
    print(datetime.datetime.now())


if __name__ == "__main__":

    # 15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between
    # zero and one, print the current time, and then exit.
    print("\n------ 15.1 ------")

    for n in range(4):
        p = multiprocessing.Process(target=wait_a_little)
        p.daemon = True
        p.start()
        p.join()
