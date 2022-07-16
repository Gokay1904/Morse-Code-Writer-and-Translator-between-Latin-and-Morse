import numpy as np
import time
from pynput import keyboard


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


pressed_codes = []
unpress_time = 0
pressed = False
unpress = False
code = ""

release_time = time.time()
release_interval = 0

testcodes = ["* - -  -- *", " ** * * *"]
testcodes = [" ","        ", " *- *  *" ,"   ", "    -        * * *"]

def morse_decoder(codes):
    #REARANGING
    rearranged_code = []
    
    # check empty
    for code in codes:

        x = len(code)

        for i in range(x):
             if code[i] == " ":
                 if i == x-1:
                    codes.pop(codes.index(code))
             else:
                 break
                
    for code in codes:
        checking = True
        
        #after clearing list from empty objects find regular codes
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
  
print(morse_decoder(testcodes))

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

def on_press(key):
    global pressed
    global code
    global unpress
    global start_time
    global interval
    global release_time
    global pressed_codes

    if pressed == False:

        if key == keyboard.Key.space:
            pressed = True
            interval = 0
            start_time = time.time()
            release_interval = time.time() - release_time
           #print("Release time: ", release_interval)
            print("release interval",release_interval)
            print('{0} pressed'.format(key))

        if 0.5 <= release_interval <= 1.5:
            code += " "

        if release_interval >= 2.5:
            "NEW CODE"
            pressed_codes.append(code)
            code = ""
            print(pressed_codes)
            print("after clearified" ,convert_morse_to_letter(morse_decoder(pressed_codes)))



#print(morse_decoder(testcodes))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.space:
        global start_time
        global release_time
        global pressed
        global pressed_codes
        global interval
        global code

        if pressed == True:
            #print('{0} released'.format(key))
            pressed = False

            release_time = time.time()

            interval = time.time() - start_time
            print("interval", interval)

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


