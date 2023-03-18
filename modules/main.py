import this
import time
import math
import datetime
import sys
import greet

# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line


def wait(seconds):
    time.sleep(seconds)


def my_sin(x):
    y = math.sin(x)
    return y


def iso_now():
    x = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    return x


def platform():
    return sys.platform


def supergreeting_wrapper(i):
    return greet.supergreeting(i)


if __name__ == "__main__":
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("hmert"))
