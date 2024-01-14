import pprint
words = {}


def get_words():
    with open('palabras.txt', 'r') as file:
        for line in file:
            line = line[0:-1]
            if line not in words:
                words[line] = 1
            else:
                words[line] += 1
    return words


def show_words():
    print('Palabra ', '|', ' num veces')
    for key, value in words.items():

        print(key, ' | ',value)




keyPressed = ''
while keyPressed != '0':
    print("""
            1- Import words
            2- Show words
            0- Exit
            """)
    keyPressed = str(input('What do you want to do?: '))

    match keyPressed:
        case '1':
            get_words()

        case '2':
            show_words()
        case '0':
            print('Thanks for using!')
            break
        case _:
            print('No option')
