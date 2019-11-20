#!/usr/bin/env python3
#--*-- encoding=utf-8 --*--

import sys

from random import randint

def questions(limit):
    '''
    Generate questions and answers for addition
    Each addend would be less than limit
    limit以内加法的生成器
    '''
    while True:
        left, right = (randint(0, limit-1) for _ in range(2))
        yield f'{left} + {right} = ', left + right


def quiz(asker, times):
    '''
    Ask questions and verify answers
    提出times道问题并验证答案
    '''
    exits = ['q', 'quit', 'exit', 'wtf?', '退出', '老子不做了'] # Lowercase exit codes
    for _ in range(times):
        question, solution = next(asker)
        answer = input(question).strip().lower()
        while answer not in [str(solution), *exits]:
            print('好像不对，再试试？') # Hmm..., try it again?
            answer = input(question).strip().lower()
        if answer in exits:
            print('不做了？真的吗？') # Quit? Really?
            break
        print('回答正确，太棒啦！') # Great job


def main():
    '''
    Run this program with limit and times
    使用最大值和题目数作为参数来调用程序
    e.g. python3 ./addition.py
         python3 ./addition.py 20
         python3 ./addition.py 20 50
    '''
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    times = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    quiz(questions(limit), times=times)
    print('干得不错，再接再厉哦！拜拜~') # See you next time
    
    
if __name__ == '__main__':
    main()