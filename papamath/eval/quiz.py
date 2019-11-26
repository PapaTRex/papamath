#!/usr/bin/env python3
# --*-- encoding=utf-8 --*--


def repeat(questioner, times):
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
