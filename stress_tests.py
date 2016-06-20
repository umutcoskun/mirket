#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

from mirket import Mirket

if __name__ == "__main__":
    mirket = Mirket()
    URL = "http://etsy.com"
    repeats = 5

    start = time.time()

    for i in range(repeats):
        stats = mirket.get_stats(URL)
        print("{}: {}".format(i + 1, list(stats.keys())))

    end = time.time()

    print("Finished. {} repeats took {} seconds."
          .format(repeats, end - start))
