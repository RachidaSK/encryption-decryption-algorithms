# A python program to illustrate Caesar Cipher Technique
def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)

        # if it's a number,shift its actual value
        elif (char.isdigit()):
            result += str(int(char) - s) % 10

        else:
            result += char

    return result


# check the above function
text = "Mj li leh ercxlmrk gsrjmhirxmep xs wec, li avsxi mx mr gmtliv, xlex mw, fc ws glerkmrk xli svhiv sj xli pixxivw sj xli eptlefix, xlex rsx e asvh gsyph fi qehi syx."
s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + decrypt(text, s))
