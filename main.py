
import time
from pynput import keyboard

pressed_codes = []

ITmorsecode_latin = {"A": "* -" ,"B": "- * * *","C": "- * - *" ,"D": "- * *" ,
"E": "*" ,"F": "* * - *","G": "- - *" ,"H": "* * * *" ,
"I": "* *" ,"J": "* - - -","K": "- * -" ,"L": "* - * *" ,
"M": "- -" ,"N": "- *","O": "- - -" ,"P": "* - - *" ,
"Q": "- - * -" ,"R": "* - *","S": "* * *" ,"T": "-" ,
"U": "* * -" ,"V": "* * * -","W": "* - -" ,"X": "- * * -" ,
"Y": "- * - -" ,"Z": "- - * *",
"1": "* - - - -" ,"2": "* * - - -","3": "* * * - -",
"4": "* * * * -" ,"5": "* * * * *","6": "- * * * *",
"7": "- - * * *" ,"8": "- - - * *","9": "- - - -*",
"0": "- - - - -" }


start_time = time.time()
interval = 0
code = ""
pressed = False

introText = r"""
  __  __                        _____                          _            
 |  \/  |                      / ____|                        | |           
 | \  / | ___  _ __ ___  ___  | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
 | |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |  | | (_) | |  \__ \  __/ | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
 |_|  |_|\___/|_|  |___/\___|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   """



infoText = r"""                                                    
                                                      | |            | |           | |  
  _ __  _ __ ___  ___ ___   ___ _ __   __ _  ___ ___  | |_ ___    ___| |_ __ _ _ __| |_ 
 | '_ \| '__/ _ \/ __/ __| / __| '_ \ / _` |/ __/ _ \ | __/ _ \  / __| __/ _` | '__| __|
 | |_) | | |  __/\__ \__ \ \__ \ |_) | (_| | (_|  __/ | || (_) | \__ \ || (_| | |  | |_ 
 | .__/|_|  \___||___/___/ |___/ .__/ \__,_|\___\___|  \__\___/  |___/\__\__,_|_|   \__|
 | |                           | |                                                      
 |_|                           |_|                                                      """

print("Currently only writing mode is enabled")

print(introText)

print("__________________________________________________________________________________________________")
print(infoText)


def on_press(key):
    global pressed
    if key == keyboard.Key.space and pressed == False:
        print('{0} pressed'.format(key))
        global start_time
        global interval
        start_time = time.time()
        pressed = True


   # try:
   #     print('alphanumeric key {0} pressed'.format(key.char))


   # except AttributeError:
   #     print('special key {0} pressed'.format(key))


testcodes = ["* -" , "- * * *"]
def morse_decoder(codes):
    #REARANGING
    rearranged_code = []

    for code in codes:
        checking = True

        while checking == True:
            x = len(code)

            for i in range(x):
                if (i == (x - 1)):
                    checking = False

                if i == 0:
                    if code[i] == " ":
                        code = code[1 :]
                        break

                elif i != 0:

                    if i == (x - 1):
                        if code[i] == " ":
                            code = code[0:i]
                            break

                    if code[i] == " ":
                        j = 0
                        if code[i+1] == " ":
                             j+=1
                             while True:

                                 if code[i+j] == " ":
                                     if (i + j) != (x-1):
                                         j += 1

                                 if (i + j) == (x-1):
                                    if code[i + j] == " ":
                                        code = code[0: i:] + code[(i + j)::]
                                        print(code)

                                    elif code[i+j] != " ":
                                        code = code[0: i:] + code[(i + j - 1)::]
                                        print(code)
                                        checking = False
                                    break

                                 elif code[i+j] != " ":
                                     code = code[0: i:] + code[(i+j-1): :]
                                     print(code)
                                     break
                             break
                        elif code[i] != " ":
                            i+=1

        rearranged_code.append(code)


    return rearranged_code


def convert_morse_to_letter(rearranged_codes):
    print("__________________________________________________________________________________________________")
    letters= []

    # seperate keys and values of morse letter
    values = [ITmorsecode_latin[i] for i in ITmorsecode_latin]
    keys = [i for i in ITmorsecode_latin.keys()]

    for code in rearranged_codes:
        for value in values:
            if code == value:
                letters.append(keys[values.index(value)])


    return letters


code = ""

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.space:
        global start_time
        global pressed
        global pressed_codes
        global interval
        global code

        print('{0} released'.format(key))
        pressed = False

        interval = time.time() - start_time
        #print(f"Seconds since epoch = {interval}")

        if (4 > interval > 2):
            pressed_code = "-"
            code += pressed_code
            print(code)

        elif (2 > interval > 1):
            pressed_code = "*"
            code += pressed_code
            print(code)

        elif (interval < 1):
            pressed_code = " "
            code += pressed_code
            print(code)

        elif (interval >= 5):
            pressed_codes.append(code)
            code = ""
            print(pressed_codes)
            print(convert_morse_to_letter(morse_decoder(pressed_codes)))

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()
