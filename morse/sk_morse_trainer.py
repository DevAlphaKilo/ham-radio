#
#  Morse code trainer
#

import sys
import time
from gpiozero import Button

# Set Input 1 for GPIO
button = Button(21)  # GPIO Pin 40

# Script Timing Variables
# https://en.wikipedia.org/wiki/Morse_code#Timing
cw_gap_intra_char = 1    # 0.1 (Default)
cw_gap_short      = 3    # 3 (Default)
cw_gap_medium     = 7    # 7 (Default)
cw_interval       = cw_gap_intra_char * 0.15

# Change these values (in seconds) to suit your style (or 'fist')
dot_timeout = 0.15
dash_timeout = 1

# Track the key presses and generated morse
current_letter = ""
message = ""
space_added = False

# https://morsecode.world/international/morse.html

morse_alphanumeric = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    "-----": "0"
}

morse_punctuation = {
    ".-...": "&", ".----.": "'", ".--.-.": "@", "-.--.-": ")", "-.--.": "(",
    "---...": ":", "--..--": ",", "-...-": "=", ".-.-.-": ".", "-....-": "-",
    ".-.-.": "+", ".-..-.": "\"", "..--..": "?", "-..-.": "/",
    "-.-.--": "!" # "!" Not in ITU-R recommendation
}

morse_prosigns = {
    "AA": "\n",      # New Line
    "AR": "EOM",     # End of message
    "AS": "",        # Wait
    "BK": "",        # Break
    "BT": "\n\n",    # New paragraph
    "CL": "",        # Going off the air ("clear")
    "SK": ""         # End of transmission
}

print('Ready')

try:

    while True:

        # Wait for a keypress or until a letter has been completed
        #button.wait_for_press(dash_timeout)

        # Determine keypress value (Not Pressed)
        if button.is_pressed is False:

            print(".", end="", flush=True)

            # If we've timed out and there's been previous keypresses, show the letter
            if len(current_letter) > 0:

                # Check for alphanumeric values
                if current_letter in morse_alphanumeric:
                    message += morse_alphanumeric[current_letter]
                    print("Message: " + message)
                    space_added = False

                # Check for punctuation values
                elif current_letter in morse_punctuation:
                    message += morse_punctuation[current_letter]
                    print("Message: " + message)
                    space_added = False

                # No other valid characters found
                else:
                    print("Not recognised")

                current_letter = ""

        # Add space if message is started
#        elif button.is_pressed is False and len(message) > 0:
#            if not space_added:
#                message += " "
#                print("Message: " + message)
#                space_added = True

        # Determine keypress value (Pressed)
        elif button.is_pressed:

            # The key has been pressed, work out if it's a dot or a dash
            print("=", end='', flush=True)
#            button_down_time = time.time()
#            button.wait_for_release()
#            button_up_time = time.time()
#            button_down_length = button_up_time - button_down_time

            # Was it a dot or dash?
#            if button_down_length > dot_timeout:
#                print('-', end='', flush=True)
#                current_letter += '-'

#            else:
#                print('.', end='', flush=True)
#                current_letter += '.'

        time.sleep(cw_interval)

except KeyboardInterrupt:
    print("\nStopping...")
    print(message)
    exit(0)