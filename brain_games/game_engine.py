import prompt


ROUNDS_TO_WIN = 3


def play(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.TASK)

    rounds_count = 0
    while rounds_count < ROUNDS_TO_WIN:
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            rounds_count = rounds_count + 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break

    if rounds_count == ROUNDS_TO_WIN:
        print(f'Congratulations, {user_name}!')
