import time

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
alphabet = alphabet + [" "]

# hello world
main_text = ''


def typetext(char, text):

    global main_text

    the_text = text
    for i in alphabet:
        print(the_text + i)
        time.sleep(0.02)
        if i == char:
            main_text = main_text + i
            break


for i in range(1, 12):
    if i == 1:
        typetext('h', main_text)
    elif i == 2:
        typetext('e', main_text)
    elif i == 3:
        typetext('l', main_text)
    elif i == 4:
        typetext('l', main_text)
    elif i == 5:
        typetext('o', main_text)
    elif i == 6:
        typetext(' ', main_text)
    elif i == 7:
        typetext('w', main_text)
    elif i == 8:
        typetext('o', main_text)
    elif i == 9:
        typetext('r', main_text)
    elif i == 10:
        typetext('l', main_text)
    elif i == 11:
        typetext('d', main_text)
