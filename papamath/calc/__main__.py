#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import datetime as dt
import sys

from . import addition
from . import subtraction
from ..eval import quiz


def main():
    """
    Run this program with limit and times
    使用最大值和题目数作为参数来调用程序
    e.g. python3 -m papamath.calc
         python3 -m papamath.calc 20
         python3 -m papamath.calc 20 50
    """
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    times = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    summary = quiz.repeat(
        [addition.add_ints(limit), subtraction.sub_ints(limit)], times=times)
    num = len(summary['question'].unique())
    if num > 0:
        total_time = summary['spent'].sum()
        average_time = total_time / num

        print(f'你一共做了{num}道数学题，用时{str(dt.timedelta(seconds=total_time))}，'
              f'每题平均{str(dt.timedelta(seconds=average_time))}，继续加油！')


if __name__ == '__main__':
    main()
