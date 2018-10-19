#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import string, random
from loc import Locale, LocDict


def rnd_str(length):
    return "".join(random.sample(string.ascii_letters, length))


def measure_elapse(n_word, n_test):
    data = {
        Locale.en_US: [rnd_str(32) for _ in range(n_word)],
        Locale.zh_CN: [rnd_str(32) for _ in range(n_word)],
    }
    ld = LocDict(data=data)

    total_words = list()
    current_locale = None
    for locale, values in data.items():
        current_locale = locale
        total_words.extend(values)
        break

    word_list = [random.choice(total_words) for _ in range(n_test)]
    st = time.clock()
    for word in word_list:
        ld.trans_to(word, dst_loc=Locale.zh_CN, src_loc=current_locale)
    elapse = time.clock() - st
    return elapse


def run_benchmark():
    """
    Conclusion: linearly increase.
    """
    for n_test in [100, 1000, 10000]:
        elapse = measure_elapse(n_word=1000, n_test=n_test)
        print("elapse={:.6f}, n_test={}".format(elapse, n_test))


if __name__ == "__main__":
    run_benchmark()
