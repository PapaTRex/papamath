#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import time

import pandas as pd


def repeat(questioner, times):
    """
    Ask questions and verify answers
    提出times道问题并验证答案
    """
    exits = ['q', 'quit', 'exit', 'wtf?', '退出', '老子不做了']  # Lowercase exit codes
    summary = pd.DataFrame(columns=['question', 'answer', 'correct', 'spent'])

    for i in range(times):
        question, solution = next(questioner)

        start = time.time()
        answer = input(f'[{i+1}/{times}]: {question}').strip().lower()
        end = time.time()

        while answer not in [str(solution), *exits]:
            summary.loc[len(summary)] = (question, answer, False, end-start)
            print('好像不对，再试试？')  # Hmm..., try it again?

            start = time.time()
            answer = input(f'[{i+1}/{times}]: {question}').strip().lower()
            end = time.time()
        if answer in exits:
            print('不做了？真的吗？')  # Quit? Really?
            break
        summary.loc[len(summary)] = (question, answer, True, end-start)
        print('回答正确，太棒啦！')  # Great job

    return summary
