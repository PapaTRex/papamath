#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import sys

from . import addition
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
    num, fails = quiz.repeat(addition.add_ints(limit), times=times)
    fail_num = len(fails)
    if fail_num == 0:
        summary = '全部计算正确，太棒了，再接再厉哦！'
    elif fail_num / num < 0.1:
        summary = f'有{fail_num}道没有做对，继续努力哦！'
    else:
        summary = f'做对了{num - fail_num}道，要加油哦！'
    print(f'你一共做了{num}道数学题，{summary}')  # Summary on exit


if __name__ == '__main__':
    main()
