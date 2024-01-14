from random import *

words = []


def select_word():
    return words[randint(0, len(words) - 1)]


def play_game():
    lives = 6
    selected_word = select_word()
    solution = ''
    for i in range(len(selected_word)):
        solution += '_'
    while lives > 0 and solution != selected_word:
        print('The actual word is')
        print(solution)
        answer = str(input('Which letter do you think the word contains? '))
        if answer in selected_word:
            print('Correct!')
            new_solution = ''
            for i in range(len(selected_word)):
                if selected_word[i] == answer:
                    new_solution += answer
                else:
                    new_solution += solution[i]
            solution = new_solution
        else:
            lives -= 1
            print('Im sorry, you fail. You have got: ' + str(lives) + ' lives left')

    if solution == selected_word:
        print('YOU WIN!!!!!!!!')
    else:
        print('I am sorry you lose, the word was ' + selected_word)



with open('palabras.txt', 'r') as file:
    for line in file:
        line = line[0:-1]
        words.append(line)

keyPressed = ''
while keyPressed != '0':
    print("""
            1- Play
            0- Exit
            """)
    keyPressed = str(input('What do you want to do?: '))
    match keyPressed:
        case '1':
            play_game()

        case '0':
            print('Thanks for using!')
            break
        case _:
            print('No option')
