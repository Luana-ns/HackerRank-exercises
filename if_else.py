import math
import os
import random
import re
import sys


def main(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    return


if __name__ == '__main__':
    n = main(24)


# Test cases: n = 3; n = 24
