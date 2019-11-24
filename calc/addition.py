#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import sys

import numpy as np


def questions(limit):
    """
    Generate questions and answers for addition
    Each addend would be less than limit
    limit以内加法的生成器
    """
    while True:
        left, right = np.random.randint(0, limit, size=2)
        yield f'{left} + {right} = ', left + right


def quiz(questioner, times):
    """
    Ask questions and verify answers
    提出times道问题并验证答案
    """
    exits = ['q', 'quit', 'exit', 'wtf?', '退出', '老子不做了']  # Lowercase exit codes
    i, fails = 0, {}
    for i in range(times):
        question, solution = next(questioner)
        answer = input(f'[{i + 1}/{times}]: {question}').strip().lower()
        while answer not in [str(solution), *exits]:
            print('好像不对，再试试？')  # Hmm..., try it again?
            fails[question] = fails.get(question, 0) + 1
            answer = input(f'[{i + 1}/{times}]: {question}').strip().lower()
        if answer in exits:
            print('不做了？真的吗？')  # Quit? Really?
            break
        print('回答正确，太棒啦！')  # Great job

    return i, fails


def main():
    """
    Run this program with limit and times
    使用最大值和题目数作为参数来调用程序
    e.g. python3 ./addition.py
         python3 ./addition.py 20
         python3 ./addition.py 20 50
    """
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    times = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    num, fails = quiz(questions(limit), times=times)
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
