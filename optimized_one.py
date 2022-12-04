import time

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i)
                                                            for i in range(ord('A'), ord('Z')+1)]
alphabet = alphabet + [" "]
# desired_text = 'Hello World'
desired_text = 'Hey My name is sajad'
main_text = ''


def typetext(char, text):

    global main_text

    the_text = text
    for i in alphabet:
        print(the_text + i)
        time.sleep(0.001)
        if i == char:
            main_text = main_text + i
            break


for character in desired_text:
    typetext(character, main_text)
