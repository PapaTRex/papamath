#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--

import time

from types import GeneratorType

import numpy as np
import pandas as pd

_EXITS = ['q', 'quit', 'exit', 'wtf?', '退出', '老子不做了']  # Lowercase exit codes
_COLS = ['question', 'answer', 'correct', 'spent']  # Columns of answer summary


def repeat(questioners, times):
    """
    Ask questions and verify answers
    提出times道问题并验证答案
    :param questioners: question generators
    :param times: repeat times for questioner
    """
    summary = pd.DataFrame(columns=_COLS)

    for i in range(times):
        questioner = questioners if isinstance(questioners, GeneratorType)\
            else questioners[np.random.randint(0, len(questioners))]
        question, solution = next(questioner)

        start = time.time()
        answer = input(f'[{i + 1}/{times}]: {question}').strip().lower()
        end = time.time()

        while answer not in [str(solution), *_EXITS]:
            summary.loc[len(summary)] = (question, answer, False, end - start)
            print('好像不对，再试试？')  # Hmm..., try it again?

            start = time.time()
            answer = input(f'[{i + 1}/{times}]: {question}').strip().lower()
            end = time.time()
        if answer in _EXITS:
            print('不做了？真的吗？')  # Quit? Really?
            break
        summary.loc[len(summary)] = (question, answer, True, end - start)
        print('回答正确，太棒啦！')  # Great job

    return summary
