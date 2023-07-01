from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_1, number_2):
    dividers = []
    for divider in range(1, min(number_1, number_2) + 1):
        if number_1 % divider == 0 and number_2 % divider == 0:
            dividers.append(divider)
    result = str(max(dividers))
    return result


def get_question_answer():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = f'{random_number_1} {random_number_2}'
    correct_answer = find_gcd(random_number_1, random_number_2)
    return question, correct_answer
