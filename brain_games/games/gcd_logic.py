from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def game_logic():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = f'{random_number_1} {random_number_2}'
    dividers = []
    for divider in range(1, min(random_number_1, random_number_2) + 1):
        if random_number_1 % divider == 0 and random_number_2 % divider == 0:
            dividers.append(divider)
    correct_answer = str(max(dividers))
    return question, correct_answer
