#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import datetime as dt
import sys

import numpy as np

from ..eval import quiz


def sub_ints(limit):
    """
    Generate questions and answers for subtraction of two integers
    Each addend would be less than limit
    limit以内减法的生成器
    """
    while True:
        operands = np.random.randint(0, limit, size=2)
        yield f'{max(operands)} - {min(operands)} = ', max(operands) - min(operands)


def main():
    """
    Run this program with limit and times
    使用最大值和题目数作为参数来调用程序
    e.g. python3 ./subtraction.py
         python3 ./subtraction.py 20
         python3 ./subtraction.py 20 50
    """
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    times = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    summary = quiz.repeat(sub_ints(limit), times=times)
    num = len(summary['question'].unique())
    if num > 0:
        total_time = summary['spent'].sum()
        average_time = total_time / num

        print(f'你一共做了{num}道数学题，用时{str(dt.timedelta(seconds=total_time))}，'
              f'每题平均{str(dt.timedelta(seconds=average_time))}，继续加油！')


if __name__ == '__main__':
    main()
