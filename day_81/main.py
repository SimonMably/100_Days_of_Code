morse_code_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
                   "f": "..-.", "g": "--.", "h": "....", "i": "..",
                   "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                   "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
                   "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
                   "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
                   "0": "-----", "1": ".----", "2": "..---", "3": "...--",
                   "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                   "8": "---..", "9": "----.", "!": "-.-.--", '"': ".-..-.",
                   "&": ".-...", "(": "-.--.", ")": "-.--.-", "-": "-....-",
                   "=": "-...-", "+": ".-.-.", "/": "-..-.", ":": "---...",
                   ".": ".-.-.-", ",": "--..--", " ": "/"}

continue_converting = True

while continue_converting:
    converted_morse_code = ""
    non_morse_characters = ""

    user_input = input("\nType a message to convert into morse code: ")

    for char in user_input:
        if char.lower() in morse_code_dict.keys():
            converted_morse_code += morse_code_dict[char.lower()] + " "
        elif char not in morse_code_dict.keys():
            non_morse_characters += char + " "

    print(f"Text: {user_input}\n"
          f"Unable to convert to Morse code: {non_morse_characters}\n"
          f"Morse Code: {converted_morse_code}")

    # Will keep asking the user if they want to convert messages until they
    # type 'y' or 'n' into the prompt
    while True:
        convert_another_message = input("\nWould you like to convert another "
                                        "message to Morse code? y/n: ").lower()

        if convert_another_message == "n":
            continue_converting = False
            break
        elif convert_another_message == "y":
            break
        else:
            continue
