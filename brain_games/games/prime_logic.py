from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    question = randint(1, 100)
    if question != 2 and question % 2 == 0:
        correct_answer = 'no'
    dividers = []
    for divider in range(1, question + 1):
        if question % divider == 0:
            dividers.append(divider)
    if len(dividers) > 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
