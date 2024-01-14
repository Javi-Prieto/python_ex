words = []


def get_words():
    with open('palabras.txt', 'r') as file:
        for line in file:
            words.append(line)
    return words


def show_words():
    i = 0
    i20 = 20
    while True:

        print('You are seeing ' + str(i) + ' to ' + str(i20) + ' words')
        while i < i20:
            if i >= len(words) - 1:
                print('No more words')
                break
            else:
                print(words[i])
                i += 1
        if i >= len(words) - 1:
            break
        elif input('If you want to keep reading press enter if you do not just type something: ') == '':
            i20 += 20
        else:
            break


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
