# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":

    count = 0
    for line in sys.stdin:
        count += 1

    # print goes to sys.stdout
    sys.stdout.write(str(count))

